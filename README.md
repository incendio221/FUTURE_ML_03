🤖 **AI-Powered Customer Support Chatbot**
24/7 Virtual Assistant Using Dialogflow \& Streamlit

*A GIF demonstrating the complete Streamlit-based chatbot interface appears here*

## Overview

This project is a fully functional **customer support chatbot** that leverages Google Dialogflow ES for natural language understanding and Streamlit to deliver an engaging web interface. Inspired by the virtual agents deployed by leading e-commerce and service platforms (e.g., Amazon, Flipkart, Zomato), it is designed to answer customer questions, track orders, and manage various customer intents automatically and efficiently.

### What Makes This Chatbot Effective?

- **Always Available:** Provides instant, round-the-clock responses to customer queries.
- **Smart Intent Detection:** Understands diverse topics covering order tracking, returns, refunds, shipping, payments, and more.
- **Natural Conversations:** Handles greetings, context-aware replies, and provides graceful fallback messages as needed.
- **User-Friendly UI:** Modern Streamlit interface ensures a fast and responsive chat experience.
- **Scalable Architecture:** Easily extendable for integration with databases, human handoff, and ticket creation systems.


## Tech Stack

| Layer | Tool/Service |
| :-- | :-- |
| NLP Backend | Google Dialogflow ES |
| Frontend | Streamlit (Python) |
| Language | Python 3.8+ |
| Libraries | `google-cloud-dialogflow`, `streamlit` |

## Folder Structure

```plaintext
.
├── customer-support-bot/         # Dialogflow agent export
│   ├── intents/                  # Intent JSON files
│   └── agent.json                # Agent configuration
├── .gitignore
├── dialogflow_service_account.json # Service account (secure; DO NOT COMMIT)
├── dialogflow_utils.py           # Dialogflow API helper functions
├── requirements.txt              # Python package requirements
└── streamlit_app.py              # Streamlit application script
```


## Getting Started

### Prerequisites

- Python 3.8 or newer
- A Google Cloud Platform (GCP) account and project
- Basic familiarity with Dialogflow and Streamlit


### 1. Clone the Repository

```bash
git clone https://github.com/incendio221/FUTURE_ML_01
cd customer-support-chatbot
```


### 2. Set Up Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Configure Dialogflow

1. **Create Agent:** Visit the [Dialogflow ES Console](https://dialogflow.cloud.google.com/) to create your agent.
2. **Import Intents:** In agent settings (⚙️), under **Export and Import**, select **Restore from ZIP**. Upload a zipped copy of the `customer-support-bot` directory.
3. **Service Account Setup:**
    - Go to **IAM \& Admin > Service Accounts** at Google Cloud Console.
    - Create/select a service account and grant **Dialogflow API Client** role.
    - Download the key as JSON, rename to `dialogflow_service_account.json`, and move it to the project root.
    - **Security tip:** Ensure this file is in `.gitignore`!

### 5. Start the Application

```bash
streamlit run streamlit_app.py
```

Open [http://localhost:8501](http://localhost:8501) to use your chatbot.

## How the System Works

1. **Streamlit Frontend:** `streamlit_app.py` manages the chat UI, session state, and user input.
2. **Backend Integration:** Upon message submission, the chat is routed to `detect_intent_texts` in `dialogflow_utils.py`.
3. **Dialogflow NLU:** This function sends conversations to Dialogflow, which interprets user intent and extracts any entities (e.g., order numbers).
4. **Bot Response:** Dialogflow provides a suitable, pre-configured response, which appears immediately in the Streamlit app.

## Ideas for Future Enhancements

- **Database Connectivity:** Link with a SQL/NoSQL system to serve real customer/order data.
- **Seamless Human Escalation:** Automatically pass complex or unresolved tickets to live agents.
- **Contextual Memory:** Maintain conversational context for multi-turn chats (e.g., remember user’s order number).
- **Analytics Dashboard:** Implement real-time monitoring of usage stats, intent popularity, and satisfaction rates.
- **CI/CD Pipeline:** Adopt GitHub Actions or similar tools for automated testing and deployment.

## 👤 Author

**Developed by:**

- Ankur Yadav
- [LinkedIn](https://www.linkedin.com/in/ankur-yadav-0403bb2a9)
- [GitHub](https://github.com/incendio221)
