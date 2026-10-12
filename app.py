import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from io import StringIO

st.set_page_config(page_title="AI Customer Feedback Analyzer", page_icon="💬", layout="wide")

analyzer = SentimentIntensityAnalyzer()

st.title("💬 AI-Powered Customer Feedback Analyzer")
st.caption("A beginner-friendly demo that classifies English customer feedback and flags negative reviews.")

def analyze_feedback(text):
    scores = analyzer.polarity_scores(str(text))
    compound = scores["compound"]
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    words = [w.strip(".,!?;:()[]{}\"'").lower() for w in str(text).split()]
    stop_words = {
        "the","a","an","and","or","but","is","are","was","were","to","of","for","in",
        "on","it","this","that","i","we","you","my","our","your","with","very","not",
        "be","have","has","had","they","them","their","at","as","so","too"
    }
    keywords = sorted({w for w in words if len(w) > 3 and w.isalpha() and w not in stop_words})
    return sentiment, round(compound, 3), ", ".join(keywords[:8]), sentiment == "Negative"

tab1, tab2 = st.tabs(["Analyze feedback", "Analyze CSV file"])

with tab1:
    feedback = st.text_area(
        "Enter customer feedback (English works best)",
        placeholder="Example: The delivery was late and customer support did not help.",
        height=130
    )
    if st.button("Analyze feedback", type="primary"):
        if not feedback.strip():
            st.warning("Please enter feedback first.")
        else:
            sentiment, score, keywords, flagged = analyze_feedback(feedback)
            c1, c2, c3 = st.columns(3)
            c1.metric("Sentiment", sentiment)
            c2.metric("Sentiment score", score)
            c3.metric("Needs human review", "Yes" if flagged else "No")
            st.write("**Keywords:**", keywords if keywords else "No keywords found")
            if flagged:
                st.warning("This feedback is negative. Consider sending it to a support team for review.")
            else:
                st.success("No negative-feedback flag was triggered.")
            st.caption("Demo limitation: this is a lightweight sentiment model, not a perfect understanding of customer intent.")

with tab2:
    st.write("Upload a CSV file with a column named `feedback`.")
    uploaded = st.file_uploader("Choose CSV", type=["csv"])
    if uploaded is not None:
        try:
            df = pd.read_csv(uploaded)
            if "feedback" not in df.columns:
                st.error("Your CSV must contain a column named `feedback`.")
            else:
                results = df["feedback"].fillna("").astype(str).apply(analyze_feedback)
                df[["sentiment", "score", "keywords", "needs_review"]] = pd.DataFrame(
                    results.tolist(), index=df.index
                )
                st.dataframe(df, use_container_width=True)
                st.metric("Rows analyzed", len(df))
                st.metric("Negative feedback flagged", int((df["needs_review"] == True).sum()))
                csv_data = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "Download analyzed CSV",
                    data=csv_data,
                    file_name="analyzed_feedback.csv",
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"Could not read this file. Please check the CSV format. Details: {e}")

st.divider()
st.markdown("**How it works:** VADER sentiment analysis → sentiment label → negative-feedback flag → downloadable CSV report.")
