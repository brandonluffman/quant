# import http.client
from tickerlist import tickers
# import json
# import time 

# conn = http.client.HTTPSConnection("seeking-alpha.p.rapidapi.com")

# headers = {
#     'x-rapidapi-key': "8a89d73f28msh006e40650ff24fcp1f96d9jsn5892db4744cb",
#     'x-rapidapi-host': "seeking-alpha.p.rapidapi.com"
# }

# transcript_data = {}
# ticker_length = len(tickers)
# i = 1
# for ticker in tickers:
#     conn.request("GET", f"/transcripts/v2/list?id={ticker.lower()}&size=20&number=1", headers=headers)
#     res = conn.getresponse()
#     data = res.read()

#     json_data = data.decode("utf-8")
#     response_data = json.loads(json_data)

#     transcripts = response_data.get("data", [])
    
#     ticker_transcripts = []
#     for transcript in transcripts:
#         transcript_id = transcript.get("id")
#         title = transcript.get("attributes", {}).get("title")
#         link = transcript.get("links", {}).get("self")
#         link = 'https://seekingalpha.com' + link
#         conn.request("GET", f"/transcripts/v2/get-details?id={transcript_id}", headers=headers)

#         response = conn.getresponse()
#         response_data = response.read()
#         jjson_data = response_data.decode("utf-8")
#         rresponse_data = json.loads(jjson_data)
#         content = rresponse_data.get("data", {})
#         attributes = content.get("attributes", {})
#         trans = attributes.get("content")
#         audio = attributes.get("transcriptPath")
#         ticker_transcripts.append({"id": transcript_id, "title": title, "link": link, "transcript": trans, "audio": audio})


#     # Save transcript data for the ticker to the dictionary
#     transcript_data[ticker] = ticker_transcripts
#     print(f'Ticker number: {i} of {ticker_length}')
#     time.sleep(1)
#     i+=1


# with open("transcript_data.json", "w") as file:
#     json.dump(transcript_data, file)

# print("Transcript data saved to transcript_data.json")


import asyncio
import aiohttp
import json
import time

# async def fetch_transcript(session, ticker, headers):
#     url_list = f"https://seeking-alpha.p.rapidapi.com/transcripts/v2/list?id={ticker.lower()}&size=20&number=1"
#     async with session.get(url_list, headers=headers) as response:
#         data = await response.json()
#         transcripts = data.get("data", [])
#         ticker_transcripts = []
#         for transcript in transcripts:
#             transcript_id = transcript.get("id")
#             title = transcript.get("attributes", {}).get("title")
#             link = 'https://seekingalpha.com' + transcript.get("links", {}).get("self")
#             url_details = f"https://seeking-alpha.p.rapidapi.com/transcripts/v2/get-details?id={transcript_id}"
#             async with session.get(url_details, headers=headers) as response:
#                 data = await response.json()
#                 content = data.get("data", {}).get("attributes", {})
#                 trans = content.get("content")
#                 audio = content.get("transcriptPath")
#                 ticker_transcripts.append({"id": transcript_id, "title": title, "link": link, "transcript": trans, "audio": audio})
#         print(f"Fetched transcripts for ticker {ticker}")
#         return ticker, ticker_transcripts


import aiohttp
import asyncio
import json

async def fetch_transcript(session, ticker, headers, semaphore):
    url_list = f"https://seeking-alpha.p.rapidapi.com/transcripts/v2/list?id={ticker.lower()}&size=20&number=1"
    async with semaphore:
        async with session.get(url_list, headers=headers) as response:
            data = await response.json()
            transcripts = data.get("data", [])
            ticker_transcripts = []
            for transcript in transcripts:
                transcript_id = transcript.get("id")
                title = transcript.get("attributes", {}).get("title")
                link = 'https://seekingalpha.com' + transcript.get("links", {}).get("self")
                # url_details = f"https://seeking-alpha.p.rapidapi.com/transcripts/v2/get-details?id={transcript_id}"
                # async with session.get(url_details, headers=headers) as response:
                #     data = await response.json()
                #     content = data.get("data", {}).get("attributes", {})
                #     trans = content.get("content")
                #     audio = content.get("transcriptPath")
                ticker_transcripts.append({"id": transcript_id, "title": title, "link": link, "transcript": trans, "audio": audio})
            print(f"Fetched transcripts for ticker {ticker}")
            return ticker, ticker_transcripts

async def main(tickers):
    headers = {
        'x-rapidapi-key': "8a89d73f28msh006e40650ff24fcp1f96d9jsn5892db4744cb",
        'x-rapidapi-host': "seeking-alpha.p.rapidapi.com"
    }
    transcript_data = {}
    semaphore = asyncio.Semaphore(3)  # Limit to 5 concurrent requests
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_transcript(session, ticker, headers, semaphore) for ticker in tickers]
        completed = await asyncio.gather(*tasks)
        for ticker, ticker_transcripts in completed:
            transcript_data[ticker] = ticker_transcripts

    with open("transcript_data_official.json", "w") as file:
        json.dump(transcript_data, file)

if __name__ == "__main__":
    asyncio.run(main(tickers))


# async def fetch_transcript(session, ticker, headers):
#     url_list = f"https://seeking-alpha.p.rapidapi.com/transcripts/v2/list?id={ticker.lower()}&size=20&number=1"
#     try:
#         async with session.get(url_list, headers=headers) as response:
#             data = await response.json()
#             transcripts = data.get("data", [])
#             ticker_transcripts = []
#             for transcript in transcripts:
#                 transcript_id = transcript.get("id")
#                 title = transcript.get("attributes", {}).get("title")
#                 link = 'https://seekingalpha.com' + transcript.get("links", {}).get("self")
#                 url_details = f"https://seeking-alpha.p.rapidapi.com/transcripts/v2/get-details?id={transcript_id}"
#                 async with session.get(url_details, headers=headers) as response:
#                     data = await response.json()
#                     content = data.get("data", {}).get("attributes", {})
#                     trans = content.get("content")
#                     audio = content.get("transcriptPath")
#                     ticker_transcripts.append({"id": transcript_id, "title": title, "link": link, "transcript": trans, "audio": audio})
#             print(f"Fetched transcripts for ticker {ticker}")
#             return ticker, ticker_transcripts
#     except Exception as e:
#         print(f"Error fetching transcripts for ticker {ticker}: {e}")
#         return ticker, []

# async def main(tickers):
#     headers = {
#         'x-rapidapi-key': "8a89d73f28msh006e40650ff24fcp1f96d9jsn5892db4744cb",
#         'x-rapidapi-host': "seeking-alpha.p.rapidapi.com"
#     }
#     transcript_data = {}
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch_transcript(session, ticker, headers) for ticker in tickers]
#         completed = await asyncio.gather(*tasks)
#         for ticker, ticker_transcripts in completed:
#             transcript_data[ticker] = ticker_transcripts

#     with open("transcript_data.json", "w") as file:
#         json.dump(transcript_data, file)

# if __name__ == "__main__":
#     asyncio.run(main(tickers))

