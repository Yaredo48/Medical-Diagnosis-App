import requests
from bs4 import BeautifulSoup

def search_pubmed(query: str, max_results: int = 3):
    """
    Searches PubMed for a query and returns titles and links.
    """
    # Step 1: Format the URL for PubMed search
    base_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={query}"
    
    try:
        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        results = []
        # Find all article titles on the page
        articles = soup.find_all('a', class_='docsum-title', limit=max_results)
        
        for art in articles:
            results.append({
                "title": art.get_text(strip=True),
                "link": "https://pubmed.ncbi.nlm.nih.gov" + art.get('href')
            })
            
        return results
    except Exception as e:
        return {"error": f"Search failed: {str(e)}"}