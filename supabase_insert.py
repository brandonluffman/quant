import psycopg2
import json

# Connect to Supabase database
conn = psycopg2.connect(
    database="Venum",
    user="postgres.kuiqsgbpmuyoefnrmqvp",
    password="Venum10$!!!!",
    host="aws-0-us-east-1.pooler.supabase.com",
    port="5432"
)


cur = conn.cursor()

# Read transcript data from JSON file
with open("transcript_data.json", "r") as file:
    transcript_data = json.load(file)

# Iterate through transcript data and insert into earnings_calls table
for ticker, transcripts in transcript_data.items():
    for transcript in transcripts:
        # Extract data from transcript
        transcript_id = transcript["id"]
        title = transcript["title"]
        link = transcript["link"]
        transcript_text = transcript["transcript"]
        audio_link = transcript["audio"]

        # Insert data into earnings_calls table, including the ticker
        cur.execute("""
            INSERT INTO earnings_calls (transcript_id, title, link, transcript, audio, ticker)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (transcript_id, title, link, transcript_text, audio_link, ticker))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()