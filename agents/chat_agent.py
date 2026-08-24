# agents/chat_agent.py
# Conversational agent - handles general questions.

from core.base_agent import BaseAgent
from core.message import Message
from utils.logger import LoggingMixin

class ChatAgent(LoggingMixin, BaseAgent):
    """
    A general-purpose conversational agent.
    Inherits from both LoggingMixin and BaseAgent (multiple inhertance)
    """

    GREETINGS = {"hi", "hello", "hey", "greetings", "good morning", "good evening"}

    def __init__(self, name, model="gpt-4o", personality="helpful"):
        super().__init__(name, model)
        self.personality = personality
        self._info(f"ChatAgent '{name}' intialised", {"personality" : personality})

    @property
    def agent_type(self):
        return "chat"

    def run(self, user_input):
        """
        Process user input and generate a contextual response.
        This is where polymorphism lives - each agent type responds differently.
        """
        self._debug(f"Processing input", {"len": len(user_input)})
        lower = user_input.lower().strip()

        # Greeting detection
        if any(g in lower for g in self.GREETINGS):
            return self._greet(user_input)

        # Question detection
        if lower.endswith("?") or lower.startswith(("what", "how","why","when","who","where")):
            return self._answer_questions(user_input)

        # Tool usage
        if self._tools:
            best_tool = self._pick_tool(lower)
            if best_tool:
                self._info(f"Using tool", {"tool": best_tool})
                result = self.use_tool(best_tool, user_input)
                return f"I used the {best_tool} tool to help you: {result}"

        # Default response
        return self._default_response(user_input)
    