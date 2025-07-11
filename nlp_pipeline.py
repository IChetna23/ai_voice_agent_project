from transformers import pipeline

# Load Hugging Face models
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

def run_nlp_pipeline(text):
    # Sentiment Analysis
    sentiment_result = sentiment_pipeline(text)[0]
    sentiment = sentiment_result['label']  # POSITIVE / NEGATIVE / NEUTRAL

    # MIXED Sentiment Logic
    lower_text = text.lower()
    if "maybe" in lower_text or "sometimes" in lower_text:
        sentiment = "MIXED"

    # Keyword extraction
    ner_results = ner_pipeline(text)
    keywords = list(set([ent['word'] for ent in ner_results]))

    return {
        "transcript": text,
        "sentiment": sentiment,
        "keywords": keywords
    }

# Example usage
if __name__ == "__main__":
    text = "Hi, I’m Alex. I have 2 years of experience in Python and Django. I'm based in Bangalore."
    result = run_nlp_pipeline(text)
    print("NLP Pipeline Output:")
    print(result)
