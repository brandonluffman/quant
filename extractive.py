import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from heapq import nlargest
from earnings_call import text

def summarize_text(text, num_sentences=30):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize the text into words
    words = word_tokenize(text)

    # Filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Calculate word frequency distribution
    word_freq = FreqDist(words)

    # Assign score to each sentence based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_freq[word]
                    else:
                        sentence_scores[sentence] += word_freq[word]

    # Select top 'num_sentences' sentences with highest scores
    summarized_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Combine selected sentences to form the summary
    summary = ' '.join(summarized_sentences)
    return summary


summary = summarize_text(text)
print(summary)
