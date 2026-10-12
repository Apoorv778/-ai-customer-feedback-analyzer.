# AI-Powered Customer Feedback Analyzer

A beginner-friendly Python + Streamlit demo that analyzes English customer feedback, labels it Positive/Neutral/Negative, flags negative feedback for human review, and supports batch analysis from a CSV file.

## Features
- Analyze a single feedback message
- Show sentiment score and extracted keywords
- Flag negative feedback for human review
- Upload a CSV containing a `feedback` column
- Download the analyzed results as a CSV

## Tech stack
- Python
- Streamlit
- VADER sentiment analysis
- pandas

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   streamlit run app.py
   ```

## Example CSV
Create a file called `sample_feedback.csv`:

```csv
feedback
"The product is excellent and arrived early"
"Delivery was late and support was unhelpful"
"The package arrived today"
```

Upload it in the app's **Analyze CSV file** tab.

## Deploy online with Streamlit Community Cloud
1. Upload `app.py`, `requirements.txt`, and `README.md` to a GitHub repository.
2. Sign in to Streamlit Community Cloud using GitHub.
3. Create a new app and select your repository, branch, and `app.py`.
4. Deploy, then test the public link before sharing it.

## Important limitations
- This demo works best with English feedback.
- VADER is a lightweight sentiment tool; it can misread sarcasm, context, mixed-language text, and nuanced complaints.
- Negative flags should support human review, not replace a human decision.
- Do not upload real customer personal information to a public demo.

## Project status
Starter implementation. Test it and make improvements before describing it as production-ready.
