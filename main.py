# main.py -  AgentForge entry point
# Run with: python main.py

from core.message import Message
from core.pipeline import Pipeline
from utils.registry import Registry

from tools.calculator_tool import CalculatorTool
from tools.text_tool import TextTool
from tools.search_tool import SearchTool

from agents.chat_agent import ChatAgent
from agents.analyst_agent import AnalystAgent
from agents.router_agent import RouterAgent

def demo_message():
    print("\n" + "="*60)
    print("DEMO 1 - Message class (dunders + operator overloading)")
    print("="*60)

    m1 = Message.user("Hello, AgentForge!")
    m2 = Message.assistant("Hello! How can I help?")
    m3 = Message.system("You are a helpful assistant.")
    m4 = Message.tool_result("Calculator", "42")

    
