
---

## 3️⃣ `ai-receptionist-factory/README.md`

```markdown
# AI Receptionist & Factory Visitor Copilot  
AIレセプショニスト／工場ビジター・コパイロット

## 🌍 Overview (EN)

This project is a small **AI receptionist** for a manufacturing plant.

It:

- Stores FAQs in `data/faqs.csv`
- Uses **TF-IDF** to retrieve relevant FAQs for a user question
- Sends the top FAQs as context to **Azure OpenAI** to generate a polite answer in Japanese
- Exposes a FastAPI endpoint `/ask`

---

## 🌏 概要（日本語）

本プロジェクトは、製造工場向けの簡易 **AIレセプショニスト** です。

- `data/faqs.csv` にFAQを保存  
- TF-IDF によるFAQ検索で、ユーザー質問に関連するQ&Aを取得  
- 上位FAQをコンテキストとして Azure OpenAI に渡し、日本語で丁寧な回答を生成  
- FastAPI の `/ask` エンドポイントから利用可能  

---

## 🗂 Structure / 構成

```text
ai-receptionist-factory/
  README.md
  requirements.txt
  .gitignore
  .env.example
  data/
    faqs.csv
  src/
    retriever.py
    llm_client.py
    api.py
