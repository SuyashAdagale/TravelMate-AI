from tavily import TavilyClient
from langchain_core.tools import tool

def get_tavily_tool(tavily_key: str):
    tavily_client = TavilyClient(api_key=tavily_key)

    @tool
    def web_search(query: str) -> str:
        """Search for real-time travel information, prices, hotels, and attractions."""
        try:
            results = tavily_client.search(query, max_results=3)
            
            formatted_results = []
            for r in results.get('results', []):
                content = r.get('content', 'No content')
                url = r.get('url', 'No URL')
                formatted_results.append(f"- {content}\n  (Source: {url})")
            
            return "\n\n".join(formatted_results)
            
        except Exception as e:
            return f"Error executing search: {str(e)}"

    return web_search