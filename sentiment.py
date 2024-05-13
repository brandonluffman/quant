## Transformers
# from transformers import pipeline

# # Load pre-trained sentiment analysis model
# sentiment_classifier = pipeline("sentiment-analysis")

# # Example usage
# text = "I love this movie!"
# result = sentiment_classifier(text)

# # Print result
# for res in result:
#     print(f"label: {res['label']}, with score: {res['score']}")


### spaCy ###

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from earnings_call import text

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")
doc = nlp(text)

print('-1-1 Sentiment:', doc._.blob.polarity)
# -0.125

print('0-1 Factual vs. Opinion:', doc._.blob.subjectivity)
# 0.9

# print(doc._.blob.sentiment_assessments.assessments)