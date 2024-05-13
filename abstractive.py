# from transformers import pipeline
from earnings_call import text

# def abstractive_summarization(text):
#     # Load pre-trained model for summarization
#     summarizer = pipeline("summarization")

#     # Generate abstractive summary
#     summary = summarizer(text, max_length=1000, min_length=300, do_sample=False)[0]['summary_text']
#     return summary


# summary = abstractive_summarization(text)
# print(summary)

from transformers import pipeline


summarizer = pipeline("summarization")

long_text = text
chunk_size = 1000
chunks = [long_text[i:i+chunk_size] for i in range(0, len(long_text), chunk_size)]

# Generate summary for each chunk
generated_summaries = []
for chunk in chunks:
    summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
    generated_summaries.append(summary[0]['summary_text'])

# Concatenate the generated summaries to obtain the final summary
final_summary = " ".join(generated_summaries)
print(final_summary)
