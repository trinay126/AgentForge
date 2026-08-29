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

    print(f"\nDunder methods: ")
    print(f" len(m)        = {len(m1)} words")
    print(f" bool(m1)      = {bool(m1)}")
    print(f" m1 == m2      = {m1 == m2}") 
    print(f" m1 == m2      = {m1 == m2} ")
    print(f" 'Hello' in m1 = {'Hello' in m1}")
    print(f" 'Bye' in m1   = {'Bye' in m1}")

    print(f"\nOperator overloading: ")
    combined = m1 + Message.user("How are you?")
    print(f" m1+m2 = {combined}")

    print(f"\nIteration:")
    print(f" Words in m1: {list(m1)}")

    print(f"\nAlternative constructors (@classmethod):")
    print(f" {repr(m3)}")
    print(f" {repr(m4)}")
    print(f" Total messages created: {Message.total_created()}")


def demo_tools():
    print("\n" + "="*60) 
    print("DEMO 2 - Tools (inheritance, __call__, duck typing)")
    print("="*60)

    calc = CalculatorTool()
    text = TextTool()
    search = SearchTool()

    print(f"\nTool string representations:")
    print(f"  {calc}")
    print(f"  {text}") 
    print(f" {search}") 

    print(f"\Calling tools(via__call__):")
    print(f" {calc('calculate 2 + 3 * 4')}")
    print(f" {calc('What is 100 / 4 + 5')}")
    print(f" {text('analyse: Python is great and amazing')}")
    print(f" {text('reverse these words: hello world')}")
    print(f" {search('tell me about fastapi')}")
    print(f" {search('what is oop')}")

    print(f'\nTool stats (after calls):')
    for tool in [calc, text, search]:
        print(f" {tool.name}: called {tool.call_count}x")

    print(f"\nDuck typing - tools stored in registry:")
    registry = Registry("tools")
    registry.register(calc)
    registry.register(text)
    registry.register(search)
    print(f" {registry}")
    print(f" 'calculator' in registry: {'calculator' in registry}")
    print(f"  Available: {registry.all_names()}")

def demo_agents():
    print("\n" + "="*60)
    print("DEMO 3 - Agents (composition, polymorphism, mixins)")
    print("="*60)

    # Create tools
    calc = CalculatorTool()
    text = TextTool()
    search = SearchTool()

    # create agents and add tools
    chat_agent = ChatAgent("chatBot", personality="friendly")
    (chat_agent
     .add_tool(calc)
     .add_tool(text)
     .add_tool(search))

    analyst_agent = AnalystAgent("DataBot")

    print(f"\nAgent info: ")
    print(f" {chat_agent}")
    print(f" {analyst_agent}")

    print(f"\nAgent magic methods: ")
    print(f" len(chat_agent)             = {len(chat_agent)} tools")
    print(f" 'calculator' in chat_agent  = {'calculator' in chat_agent}")
    print(f" 'nonexistent' in chat_agent = {'nonexistent' in chat_agent}")

    print(f"\nChat agent conversations: ")
    inputs = [
        "hello there!",
        "Calculate 150 * 3 + 250",
        "What is the sentiment of: python is amazing and great!",
        "What is python?",
    ]
    