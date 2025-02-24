### Symptom Checker Chat Bot

This repository contains the code for a Symptom Checker Chat Bot built using Streamlit and the Groq API. The bot is designed to help users by providing potential medical conditions based on the symptoms they describe, and suggesting nearby hospitals for severe symptoms.

#### Features
- **API Integration**: Utilizes Groq's generative model API for intelligent symptom analysis and medical advice.
- **User-Friendly Interface**: A streamlined chat interface built with Streamlit for easy interaction.
- **Model Training**: The model is trained to act as a professional doctor, analyzing symptoms and offering possible conditions.
- **Hosting**: Hosted on Streamlit Cloud for easy accessibility.

#### Tech Stack
- **Languages**: Python
- **Frameworks**: Streamlit
- **APIs**: Groq API (llama3-70b-8192)

#### How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yousufmunna143/symptom-checker-chat-bot.git
   cd symptom-checker-chat-bot
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables in a `.env` file:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

#### Usage
Interact with the chatbot by describing your symptoms, and the bot will provide possible medical conditions and advice. For severe symptoms, it will suggest visiting nearby hospitals.

#### License
This project is licensed under the MIT License.

---

Feel free to adjust any parts as you see fit! This should give a clear overview of your project for anyone visiting your GitHub repository. 😊
