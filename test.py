from googlesearch import search

def google_search(query: str, limit: int = 5):
    return list(search(query, num_results=limit))

results = google_search("Best FastAPI documentation")

for i, url in enumerate(results, 1):
    print(f"{i}. {url}")