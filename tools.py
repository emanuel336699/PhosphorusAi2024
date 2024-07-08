from exa_py import Exa
import os
import ast
from langchain.agents import tool

exa = Exa(api_key="ac366157-20f4-4a03-b59d-b727cd3bb881")

class ExaSearchTool:
    @tool
    def search(query: str):
        """Search for a webpage based on the query."""
        return ExaSearchTool._exa().search(query, use_autoprompt=True, num_results=3)

    @tool
    def find_similar(url: str):
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        """
        url = url.strip()
        if not url.startswith("http"):
            return f"Error: Invalid URL format: {url}"
        return ExaSearchTool._exa().find_similar(url, num_results=3)

    @tool
    def get_contents(ids: str):
        """Get the contents of a webpage.
        The ids must be passed in as a list, a list of ids returned from `search`.
        """
        try:
            ids = ast.literal_eval(ids)  # Use safer alternative to eval
        except Exception as e:
            return f"Error evaluating ids: {e}"
        
        if not isinstance(ids, list):
            return "Error: ids should be a list."
        
        try:
            contents = str(ExaSearchTool._exa().get_contents(ids))
        except Exception as e:
            return f"Error getting contents: {e}"
        
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)

    @staticmethod
    def tools():
        return [
            ExaSearchTool.search,
            ExaSearchTool.find_similar,
            ExaSearchTool.get_contents
        ]

    @staticmethod
    def _exa():
        api_key = os.environ.get('EXA_API_KEY')  # Ensure the correct environment variable name
        if not api_key:
            raise ValueError("API key for Exa not found in environment variables.")
        return Exa(api_key=api_key)
