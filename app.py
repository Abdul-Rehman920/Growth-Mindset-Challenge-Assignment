import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(
    page_title="Growth Mindset Challenge",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #ced4da;
    }
    .css-1aumxhk {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# App header
st.title("🧠 Growth Mindset Challenge")
st.subheader("Develop your abilities through dedication and hard work")

# Navigation
tab1, tab2, tab3, tab4 = st.tabs(["Introduction", "Assessment", "Progress Tracker", "Resources"])

with tab1:
    st.header("What is a Growth Mindset?")
    st.write("""
    A growth mindset is the belief that your abilities and intelligence can be developed through hard work, 
    perseverance, and learning from your mistakes. This concept was popularized by psychologist Carol Dweck.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://miro.medium.com/v2/resize:fit:1400/1*K8L6Bz5zZvqmqzWQ5nVh5A.png", 
                 caption="Fixed vs Growth Mindset", width=300)
    
    with col2:
        st.write("""
        **Why Adopt a Growth Mindset?**
        - Embrace challenges as opportunities
        - Learn from mistakes and feedback
        - Persist through difficulties
        - Celebrate effort, not just results
        - Stay curious and open to learning
        """)
    
    st.markdown("---")
    st.header("How to Practice Growth Mindset")
    st.write("""
    1. **Set Learning Goals**: Focus on developing new skills rather than just outcomes.
    2. **Reflect Regularly**: Think about what you've learned from successes and failures.
    3. **Seek Feedback**: Use constructive criticism to improve.
    4. **Stay Positive**: Believe in your capacity to grow.
    """)

with tab2:
    st.header("Growth Mindset Assessment")
    st.write("Rate how much you agree with each statement (1 = Strongly Disagree, 5 = Strongly Agree)")
    
    questions = [
        "I believe my intelligence can be developed with effort.",
        "I view challenges as opportunities to grow.",
        "I persist when I encounter difficulties.",
        "I learn from criticism and feedback.",
        "I feel inspired by the success of others."
    ]
    
    responses = []
    for i, question in enumerate(questions):
        response = st.slider(f"{i+1}. {question}", 1, 5, 3)
        responses.append(response)
    
    if st.button("Calculate My Growth Mindset Score"):
        total_score = sum(responses)
        st.session_state.score = total_score
        
        st.subheader(f"Your Growth Mindset Score: {total_score}/25")
        
        if total_score <= 10:
            st.warning("You lean toward a fixed mindset. Consider focusing more on learning and growth opportunities.")
        elif total_score <= 20:
            st.info("You have a developing growth mindset. Keep working on embracing challenges!")
        else:
            st.success("You have a strong growth mindset! Keep up the great attitude toward learning.")
        
        # Plot the results
        fig, ax = plt.subplots()
        sns.barplot(x=np.arange(1,6), y=responses, palette="viridis", ax=ax)
        ax.set_title("Your Responses Breakdown")
        ax.set_xlabel("Question Number")
        ax.set_ylabel("Score (1-5)")
        ax.set_ylim(0, 5)
        st.pyplot(fig)

with tab3:
    st.header("Progress Tracker")
    
    if 'habits' not in st.session_state:
        st.session_state.habits = []
    
    new_habit = st.text_input("Add a new growth mindset habit to track (e.g., 'Reflect on mistakes daily')")
    
    if st.button("Add Habit") and new_habit:
        st.session_state.habits.append({"habit": new_habit, "progress": 0})
        st.success("Habit added!")
    
    st.subheader("Your Growth Habits")
    
    for i, habit in enumerate(st.session_state.get('habits', [])):
        col1, col2, col3 = st.columns([4, 3, 1])
        with col1:
            st.write(f"{i+1}. {habit['habit']}")
        with col2:
            progress = st.slider(
                "Progress", 
                0, 100, 
                habit['progress'], 
                key=f"progress_{i}"
            )
            st.session_state.habits[i]['progress'] = progress
        with col3:
            if st.button("❌", key=f"delete_{i}"):
                st.session_state.habits.pop(i)
                st.rerun()
    
    if st.session_state.habits:
        progress_values = [h['progress'] for h in st.session_state.habits]
        avg_progress = sum(progress_values) / len(progress_values)
        
        st.metric("Average Progress", f"{avg_progress:.1f}%")
        
        fig, ax = plt.subplots()
        ax.barh(
            [h['habit'] for h in st.session_state.habits],
            [h['progress'] for h in st.session_state.habits],
            color=sns.color_palette("viridis", len(st.session_state.habits))
        )
        ax.set_title("Your Growth Habits Progress")
        ax.set_xlim(0, 100)
        st.pyplot(fig)

with tab4:
    st.header("Growth Mindset Resources")
    
    st.subheader("Recommended Reading")
    st.write("""
    - *Mindset: The New Psychology of Success* by Carol Dweck
    - *Grit: The Power of Passion and Perseverance* by Angela Duckworth
    - *The Growth Mindset Playbook* by Annie Brock and Heather Hundley
    """)
    
    st.subheader("Videos")
    st.video("https://www.youtube.com/watch?v=hiiEeMN7vbQ")  # Carol Dweck's TED Talk
    
    st.subheader("Daily Growth Mindset Affirmations")
    st.write("""
    1. "I am capable of learning anything with effort and persistence."
    2. "Mistakes help me improve and grow."
    3. "Challenges are opportunities to become stronger."
    4. "My potential is unlimited with dedication."
    5. "I celebrate the success of others as inspiration."
    """)
    
    st.subheader("Journal Prompt")
    journal_prompt = st.text_area(
        "Reflect on this prompt:", 
        "Write about a time you faced a challenge. How did you respond? "
        "What would you do differently with a growth mindset?"
    )
    
    if st.button("Save Journal Entry"):
        st.success("Reflection saved! Consider revisiting this in a month to see your growth.")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ for the Growth Mindset Challenge")
