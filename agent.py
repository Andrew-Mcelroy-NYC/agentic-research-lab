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

def test_ai_connection(query):
    research_tools = [{
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
    }]
    messages = [
    {
        "role": "user",
        "content": f"Use the search_papers tool to find research papers about {query}. List the titles you find."
    }
]
    response = chat(
        model="qwen3:4b",
        tools=research_tools,
        messages=messages,
        think=False,
        options={"temperature": 0}
    )
    messages.append(response.message)
    print("Tool requests:", response.message.tool_calls)
    for tool_call in response.message.tool_calls or []:
        if tool_call.function.name == "search_papers":
            query = tool_call.function.arguments.get("query")

            if isinstance(query, str) and query.strip():
                papers = search_papers(query)
                print("Tool results:", papers)
                
                messages.append({
                    "role": "tool",
                    "tool_name": "search_papers",
                    "content": json.dumps(papers)
                })
            else:
                print("Invalid search query")
        else:
            print("Blocked unauthorized tool:", tool_call.function.name)

    if response.message.tool_calls:
        final_response = chat(
            model="qwen3:4b",
            messages=messages,
            think=False,
            options={"temperature": 0}
        )

        print("\nFinal research answer:")
        print(final_response.message.content)
    else:
        print("Qwen3 did not request a tool.")


test_ai_connection(query)
