import pickle
from supabase_py import create_client

# Initialize Supabase client
supabase_url = 'https://kuiqsgbpmuyoefnrmqvp.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt1aXFzZ2JwbXV5b2VmbnJtcXZwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDU5NTU3OTAsImV4cCI6MjAyMTUzMTc5MH0._Vg07aKIl7SF2pUnqpFc8hiLDXU-ejUeMmIFrvNHxmI'
supabase = create_client(supabase_url, supabase_key)

# Load pickled data
with open('tfidf_matrix.pickle', 'rb') as f:
    tfidf_matrix = f.read()

with open('vectorizer.pickle', 'rb') as f:
    vectorizer = f.read()

# List of company IDs
ids = [10005, 9436, 9785, 9538, 9790, 976, 3414, 4382]

# Insert pickled data into the table for each company ID
for company_id in ids:
    response = supabase.table('tfidf_data').insert([{'tfidf_matrix': tfidf_matrix, 'vectorizer': vectorizer, 'company_id': company_id}])

    if response.error:
        print(f"Failed to insert pickled data for company ID {company_id}: {response.error}")
    else:
        print(f"Pickled data inserted for company ID {company_id} successfully!")
