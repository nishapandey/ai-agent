from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
wiki_tool = Tool(
    name="wikipedia",
    func=wiki_tool.run,
    description="Useful for when you need to look up a topic on Wikipedia",
)
# Example usage:
# result = search_tool.run("Python programming language")
# print(result)
# wiki_result = wiki_tool.run("Artificial Intelligence")
# print(wiki_result)
# save_result = save_tool.run("This is a test research output.")
# print(save_result)
# Note: The above example usage lines are commented out to prevent execution during import.
