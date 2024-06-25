from crewai_tools import SerperDevTool
from .config import SERPER_API_KEY

search_tool = SerperDevTool(api_key=SERPER_API_KEY)

tools = {
    "search_tool": search_tool
}
