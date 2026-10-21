def search_papers(query):
    papers = [
        {
            "title": "Machine Learning for Protein Structure Prediction",
            "abstract": "AI can predict protein structures and support drug discovery."
        },
        {
            "title": "Security Risks of Autonomous AI Agents",
            "abstract": "AI agents face prompt injection and unauthorized tool execution risks."
        }
    ]

    results = []

    for paper in papers:
        if query.lower() in (
            paper["title"] + " " + paper["abstract"]
        ).lower():
            results.append(paper)

    return results


query = input("What research topic are you interested in? ")

results = search_papers(query)

for paper in results:
    print(f"\nTitle: {paper['title']}")
    print(f"Abstract: {paper['abstract']}")

if not results:
    print("No matching papers found.")