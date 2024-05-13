from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_and_tokenize(description):
    # Tokenize the description

    tokens = word_tokenize(description.lower())
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]
    
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return ' '.join(tokens)


equity_descriptions = [
    "Tesla, Inc. designs, manufactures, and sells electric vehicles, solar panels, and energy storage products.",
    "NIO Inc. is a Chinese electric vehicle manufacturer, specializing in designing and developing electric autonomous vehicles.",
    "General Motors Company designs, manufactures, markets, and distributes vehicles and vehicle parts.",
    "Albemarle Corporation is a global specialty chemicals company, focusing on lithium, bromine, and refining catalysts.",
    "Ford Motor Company designs, manufactures, markets, and services a full line of cars, trucks, SUVs, electrified vehicles, and Lincoln luxury vehicles.",
    "FTAI Aviation Ltd. owns and acquires infrastructure and related equipment for the transportation of goods and people worldwide. It operates through two segments, Aviation Leasing and Aerospace Products. The Aviation Leasing segment owns and manages aviation assets, including aircraft and aircraft engines, which it leases and sells to customers. As of December 31, 2022, this segment owned and managed 330 aviation assets consisting of 106 commercial aircraft and 224 engines, including four aircraft and one engine that were located in Ukraine, and eight aircraft and seventeen engines that were located in Russia. The Aerospace Products segment develops, manufactures, repairs, and sells aircraft engines and aftermarket components for aircraft engines. The company was founded in 2011 and is headquartered in New York, New York.",
    "DatChat, Inc. a communication software company, develops mobile messaging application. The company offers DatChat Messenger & Private Social Network, a mobile application that gives users the ability to communicate with privacy and protection. It develops a blockchain-based decentralized communications platform that allows consumers and businesses to connect directly with each other. The company was formerly known as Yssup, Inc. and changed its name to DatChat, Inc. in September 2016. DatChat, Inc. was incorporated in 2014 and is based in New Brunswick, New Jersey.",
    "BurgerFi International, Inc., together with its subsidiaries, owns and franchises fast-casual and premium-casual dining restaurants. Its restaurants offer burgers, hot dogs, crispy chicken, frozen custard, hand-cut fries, shakes, beer, wine, pizza, coal fired chicken wings, homemade meatballs, and a variety of handcrafted sandwiches and salads. The company was formerly known as Opes Acquisition Corp. and changed its name to BurgerFi International, Inc. in December 2020. The company was founded in 2011 and is headquartered in Fort Lauderdale, Florida."
]

preprocessed_descriptions = [preprocess_and_tokenize(description) for description in equity_descriptions]

print(preprocessed_descriptions)
query = 'Looking for a company specializing in autonomous vehicles'
preprocessed_query = preprocess_and_tokenize(query)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_descriptions + [preprocessed_query] )
similarity = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[-1]).flatten()


sim_w_desc = list(zip(similarity, equity_descriptions))
sim_w_desc.sort(reverse=True)
for similarity, description in sim_w_desc:
    print(f"Similarity: {similarity:.2f}\nDescription: {description}\n")
