from transformers import pipeline

def run_sentiment_demo():
    sentiment_pipeline = pipeline("sentiment-analysis")
    text = "This flight delay is very frustrating!"
    result = sentiment_pipeline(text)
    print("Input:", text)
    print("Prediction:", result)

if __name__ == "__main__":
    run_sentiment_demo()
