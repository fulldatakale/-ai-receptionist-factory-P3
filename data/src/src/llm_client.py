import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)


def answer_with_context(user_query: str, retrieved_faqs: list[dict]) -> str:
    context_lines = []
    for item in retrieved_faqs:
        context_lines.append(f"Q: {item['question']}\nA: {item['answer']}")
    context = "\n\n".join(context_lines)

    system_prompt = (
        "You are a polite factory receptionist. "
        "Answer using only the provided FAQs and policies. "
        "If you are not sure, ask the user to contact the human receptionist."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": (
                f"User question: {user_query}\n\n"
                f"Relevant FAQs:\n{context}"
            ),
        },
    ]

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=messages,
        temperature=0.2,
    )

    return response.choices[0].message.content
