import requests

def fetch_papers(query):
    api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmode=json"
    response = requests.get(api_url)
    print(response.json())  # <-- Add this line to see the full response
    return response.json()

def fetch_papers(query):
    """Fetches papers from PubMed API based on a search query."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Fetch up to 10 results
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print("Error fetching data from PubMed API.")
        return []

    data = response.json()
    pmids = data.get("esearchresult", {}).get("idlist", [])
    return fetch_paper_details(pmids)

def fetch_paper_details(pmids):
    """Fetch paper details using PubMed IDs."""
    if not pmids:
        return []

    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json"
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return []

    data = response.json()
    result = []

    for pmid in pmids:
        paper = data.get("result", {}).get(pmid, {})
        result.append({
            "title": paper.get("title", "N/A"),
            "authors": ", ".join([a["name"] for a in paper.get("authors", [])]) if "authors" in paper else "N/A",
            "affiliation": paper.get("source", "N/A"),
            "journal": paper.get("fulljournalname", "N/A"),
            "doi": paper.get("elocationid", "N/A")
        })

    return result



