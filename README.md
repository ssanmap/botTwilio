# WhatsApp Bot with Twilio and Groq - Django Application

![License](https://img.shields.io/github/license/your-repo/your-project)
![Python Version](https://img.shields.io/badge/python-3.12-blue)

## 🚀 Project Overview

This project integrates a WhatsApp bot using Django, Twilio, and Groq API. The bot listens to incoming WhatsApp messages, sends the message to the Groq API to generate a response, and then sends it back to the user through WhatsApp using Twilio's API.

## 🛠️ Setup and Installation

### Prerequisites

Make sure you have the following installed:
- **Python 3.12** or higher
- **Django** framework
- **Twilio API** setup
- **Groq API** credentials

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
pip install -r requirements.txt

GROQ_API_KEY=xxx
TWILIO_ACCOUNT_SID=xx
TWILIO_AUTH_TOKEN=xx
. Start Ngrok
Expose your local server using ngrok to handle incoming WhatsApp webhook requests:
ngrok http 8000

