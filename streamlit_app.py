import streamlit as st
from agent import get_agent
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="TravelMate AI", page_icon="✈️", layout="wide")

st.title("✈️ TravelMate AI: Where to go just a click away?")
st.caption("made by suyash")

with st.sidebar:
    st.header("🔑 API Keys")
    google_key = st.text_input("Google Gemini Key", type="password")
    tavily_key = st.text_input("Tavily API Key", type="password")
    
    st.markdown("---")
    st.markdown("[Get Google Key](https://ai.google.dev/)")
    st.markdown("[Get Tavily Key](https://tavily.com/)")
    st.markdown("have fun")

col1, col2 = st.columns(2)
with col1:
    destination = st.text_input("Destination", "Kerala, India")
    days = st.number_input("Days", 1)
with col2:
    budget = st.text_input("Budget", "₹50,000") 
    interests = st.text_input("Interests", "Nature, Food, Relaxing")

if st.button("🚀 Plan My Trip"):
    if not google_key or not tavily_key:
        st.error("Please enter API keys.")
    else:
        try:
            with st.spinner("Generating your plan,pls wait"):
                agent = get_agent(google_key, tavily_key)
                
                query_text = f"Plan a {days}-day trip to {destination}. Budget: {budget} (Indian Rupees). Interests: {interests}."
                
                result = agent.invoke({
                    "messages": [
                        {"role": "user", "content": query_text}
                    ]
                })
                
                raw_content = result["messages"][-1].content
                
                if isinstance(raw_content, list):
                    final_response = raw_content[0]["text"]
                else:
                    final_response = raw_content

                st.markdown(final_response)
                
        except Exception as e:
            st.error(f"Error: {e}")