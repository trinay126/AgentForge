# core/base_agent.py
# Abstarct base class for all agents

from abc import ABC, abstractmethod
from core.memory import Memory
from core.message import Message

class BaseAgent(ABC):
    """
    Abstract base for every agent in AgentForge
    Every agent HAS - A Memory and a collection of tools.
    concrete agents implement run() differently - polymorphism
    """

    _agent_registry = {}
    def __init__(self, name, model="gpt-4o", max_memory=20):
        self._name = name
        self._model = model
        self._memory = Memory(max_size=max_memory)
        self._tools = {}
        self._run_count = 0
        BaseAgent._agent_registry[name] = self

    # -- Abstract methods - every agent must implement ---------------------------------
    @abstractmethod
    def run(self, user_input):
        """Process user input and return a response string."""
        pass

    @property
    @abstractmethod
    def agent_type(self):
        """Short label: 'chat', 'analyst', 'router', etc"""
        pass

    # -- Properties --------------------------------------------------------------------
    @property
    def name(self):
        return self._name

    @property
    def model(self):
        return self._model

    @property
    def memory(self):
        return self._memory

    @property
    def run_count(self):
        return self._run_count

    @property
    def tool_names(self):
        return list(self._tools.keys())

        