import streamlit as st
import pickle
import string
import nltk
import random

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in nltk.corpus.stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return ' '.join(y)

# Load the pre-trained model
tfidf = pickle.load(open('models/vectorizer.pkl', 'rb'))
model = pickle.load(open('models/model.pkl', 'rb'))

# --- Modern CSS Styling ---
st.markdown("""
    <style>
    body {
        background-color: #f7f9fa;
    }
    .main {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 2rem 2rem 1rem 2rem;
        box-shadow: 0 4px 24px 0 rgba(34, 139, 230, 0.08);
        max-width: 600px;
        margin: auto;
    }
    .stTextArea textarea {
        border-radius: 8px;
        border: 1px solid #dbeafe;
        font-size: 1.1rem;
        padding: 1rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #228be6 0%, #4fd1c5 100%);
        color: white;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 0.7rem 2rem;
        border: none;
        margin-top: 1rem;
    }
    .result-spam {
        color: #e53e3e;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 1.5rem;
    }
    .result-ham {
        color: #38a169;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

spam_examples = [
    "WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only.",
    "Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030",
    "I'm gonna be home soon and i don't want to talk about this stuff anymore tonight, k? I've cried enough today.",
    "SIX chances to win CASH! From 100 to 20,000 pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+ TsandCs apply Reply HL 4 info",
    "URGENT! You have won a 1 week FREE membership in our £100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD POBOX 4403LDNW1A7RW18",
    "I've been searching for the right words to thank you for this breather. I promise i wont take your help for granted and will fulfil my promise. You have been wonderful and a blessing at all times.",
    "I HAVE A DATE ON SUNDAY WITH WILL!!",
    "XXXMobileMovieClub: To use your credit, click the WAP link in the next txt message or click here>> http://wap. xxxmobilemovieclub.com?n=QJKGIGHJJGCBL",
    "Oh k...i'm watching here:)"
]

def set_random_spam():
    st.session_state.input_sms = random.choice(spam_examples)

with st.container():
    st.markdown(
        "<h2 style='text-align: center; color: #228be6; margin-bottom: 0.5rem;'>📮SpamSense</h2>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; color: #6b7280; margin-bottom: 2rem;'>AI-powered spam prediction for your marketing campaigns.<br>Enter your strategy email below to check if it might land in the spam folder.</p>",
        unsafe_allow_html=True
    )

    # Dice icon button at bottom right of text area
    cols = st.columns([8, 1])
    with cols[1]:
        st.button("🎲", help="Try a random spam message", key="dice_btn", on_click=set_random_spam)

    # Text area with session state for dynamic update
    input_sms = st.text_area(
        "Your campaign email:",
        height=180,
        key="input_sms"
    )

    result_html = ""
    if st.button("Predict"):
        if input_sms.strip() == "":
            result_html = '<div style="color:#e53e3e; font-weight:bold; margin-top:1.5rem;">⚠️ Please enter your email content.</div>'
        else:
            transform_sms = transform_text(input_sms)
            vector_input = tfidf.transform([transform_sms])
            result = model.predict(vector_input)[0]
            if result == 1:
                result_html = '<div class="result-spam">🚫 This message is <b>Spam</b></div>'
            else:
                result_html = '<div class="result-ham">✅ This message is <b>Not Spam</b></div>'
    if result_html:
        st.markdown(result_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)