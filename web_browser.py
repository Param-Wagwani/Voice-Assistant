import webbrowser

def google_search(query):
    query = '+'.join(query.split())
    url = f"https://www.google.com/search?q={query}"
    return url

def open_browser(query):
    url = google_search(query)
    print(f"Opening Google search results for: {query}")
    webbrowser.open(url)
