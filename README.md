# TravelMate AI ✈️

**TravelMate AI 🌍 Next-Gen AI Travel Planner built with Streamlit**

An intelligent, personalized, and visually immersive travel companion that harnesses the power of Generative AI. TravelMate AI provides a seamless interface for users to generate custom itineraries, visualize potential destinations, and identify landmarks—all within a clean web interface powered by Streamlit.

✨ [Live Demo](https://your-demo-link.com) 

| 📸 <img width="1920" height="926" alt="Screenshot 2025-11-27 143251" src="https://github.com/user-attachments/assets/fd6e4821-aeb1-41ec-882b-0f7a4146f198" />







## 🚀 Key Features

* **AI Itinerary Planner:** Generate detailed, day-by-day travel itineraries based on your budget, interests, and duration using models like Google Gemini.
* **Destination Visualizer (Text-to-Image):** Unsure where to go? Describe your dream vacation vibe, and the AI will generate stunning previews of potential destinations.
* **Landmark Scout (Image-to-Text):** Upload a photo of a monument or location, and the AI will identify it and provide historical context and travel tips.
* **Budget Estimator:** Get real-time cost estimations for flights, hotels, and activities.
* **Responsive Design:** Works smoothly on both desktop and mobile browsers for planning on the go.
* **Secure API Handling:** Uses Streamlit's secrets management to keep your API keys safe.

## 🛠️ Technology Stack

* **Frontend:** Streamlit
* **Backend Logic:** Python
* **AI Models:**
    * Google Gemini Pro (for itinerary planning and logic)
    * Gemini Pro Vision (for landmark identification)
    * Groq API (for high-speed recommendations)
    * Image Gen Models (e.g., Stable Diffusion/DALL-E)
* **Deployment:** Streamlit Cloud

## ⚙️ Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

* Python 3.9 or higher
* Git for cloning the repository

### Local Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/SuyashAdagale/TravelMate-AI.git](https://github.com/SuyashAdagale/TravelMate-AI.git)
    cd TravelMate-AI
    ```

2.  **Create and activate a virtual environment:**

    * **For Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **For macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    * Create a file named `.env` in the root directory of the project.
    * Add your API keys to this file:
        ```env
        GEMINI_API_KEY="your_gemini_api_key_here"
        GROQ_API_KEY="your_groq_api_key_here"
        # Add other keys if used (e.g., Maps API, OpenAI)
        ```

5.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

The application will now be running on `http://localhost:8501`.

## 🚢 Deployment

This application is built to be easily deployed on Streamlit Cloud.

1.  Push your code to a GitHub repository.
2.  Log in to [Streamlit Cloud](https://streamlit.io/cloud) and connect your GitHub account.
3.  Click "New app", select your repository, and configure the main file path to `app.py`.
4.  **Important:** Add your API keys in the "Secrets" section under "Advanced settings". **Do not push your `.env` file to GitHub.**

## 🗺️ Project Roadmap

- [x] AI Itinerary Generation (Gemini) - **Done!**
- [x] used langchain travily websearch
- [x] day to day planner 
- [x] info about transportation
- [x] Currency Converter & Budget Calculator - **Done**

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.






