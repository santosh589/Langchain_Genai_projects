Create a chatbot with both paid and open source LLM models.

Paid:
-- OpenAI API

Open Source LLM:
-- OLlama 

2. API

--- Create API for production grade deployment efficiently using langserve
-- along with use FastAPI,
-- with swaggerui which is already in langserve.
# 🧠 LangChain FastAPI + Streamlit Demo

This project demonstrates how to build a simple language generation web application using **LangChain**, **FastAPI**, **Ollama**, **OpenAI**, and **Streamlit**.

## 🚀 Features

- 🌐 **FastAPI** backend with:
  - `/essay` endpoint: Generates an essay using OpenAI.
  - `/poem` endpoint: Generates a children's poem using LLaMA2 via Ollama.
- 🧪 **Swagger UI** for API testing at `http://localhost:8000/docs`
- 🧾 **Streamlit** frontend to interact with both APIs.
- 🔐 Environment variable loading with `dotenv`.

---