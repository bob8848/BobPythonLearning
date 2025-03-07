# func_py_text_sentiment_analysis.py
from textblob import TextBlob

def func_py_text_sentiment_analysis(text):
    return TextBlob(text).sentiment.polarity

print(func_py_text_sentiment_analysis("I love Python!"))
