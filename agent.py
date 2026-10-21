import json
from ollama import chat

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

def test_ai_connection():
    response = chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": "/no_think What is protein structure prediction? Answer in one sentence."
            }
        ],
        think=False,
        options={"temperature": 0}
    )

    print("\nQwen3 response:")
    print(response.message.content)


test_ai_connection()

research_tools = [
    {
        "type": "function",
        "function": {
            "name": "search_papers",
            "description": "Search locally stored scientific research papers by topic or keyword.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The research topic to search for."
                    }
                },
                "required": ["query"]
            }
        }
    }
]