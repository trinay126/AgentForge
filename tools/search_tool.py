# tools/search_tool.py
# simulated search tool - returns relevant mock results based on query

from core.base_tool import BaseTool

class SearchTool(BaseTool):
    """
    Simulates a web search. Uses a built-in knowledge base to return.
    context - relevant results. In a real system, this would call an API.
    """

    #class - level knowledge base (simulated search index)
    _KNOWLEDGE_BASE = {
        "python"             : "Python is a high-level, interpreted language known for readability. Latest version: 3.12.",
        "oop"                : "Object-Oriented Programming uses classes, objects, inheritance, encapsulation, and polymorphism.",
        "fastapi"            : "FastAPI is a modern Python web framework for building APIs, based on type hints.",
        "langchain"          : "LangChain is a framework for building applications with large language models (LLMs).",
        "machine learning"   : "ML enables computers to learn patterns from data without being explicitly programmed.",
        "data engineering"   : "Data Engineering involves building pipelines to collect, store, and process large data.",
        "sql"                : "SQL (Structured Query Language) is used to manage and query relational databases.",
        "api"                : "API (Application Programming Interface) allows different systems to communicate.",
        "recursion"          : "Recursion is a function calling itself with a smaller input until a base case is reached.",
        "big o"              : "Big O notation describes algorithm efficiency. O(1) constant, O(n) linear, O(log n) logarithmic.",
        "agent"              : "An AI agent perceives its environment, reasons, and takes actions to achieve goals.",
        "default"            : "No specific result found. Please search for: python, oop, fastapi, langchain, sql, or api."
    }

    
