import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from earnings_call import text
import spacy
from collections import Counter

from sklearn.feature_extraction.text import TfidfVectorizer
# Create a TF-IDF vectorizer with n-gram range (e.g., bi-grams and tri-grams)
tfidf_vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 3))  # Adjust ngram_range as needed

# Fit the vectorizer and transform the text
tfidf_matrix = tfidf_vectorizer.fit_transform([text])

# Get the feature names (words and phrases)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Calculate the TF-IDF scores for each word/phrase
word_scores = tfidf_matrix.sum(axis=0)

# Create a dictionary of word/phrase and corresponding score
word_scores_dict = {}
for word, score in zip(feature_names, word_scores.tolist()[0]):
    word_scores_dict[word] = score

# Sort the words/phrases by their TF-IDF scores in descending order
sorted_words = sorted(word_scores_dict.items(), key=lambda x: x[1], reverse=True)

# Print the top 10 most important words/phrases
print("Top 10 most important words/phrases:")
for word, score in sorted_words[:10]:
    print(f"{word}: {score}")
