# agents/router_agent.py
# Router agent - receives a task and delegates to the right agent.

from core.base_agent import BaseAgent
from utils.logger import LoggingMixin

class RouterAgent(LoggingMixin, BaseAgent):
    """
    Orchestrator agent. Analyses the user input and routes it to
    the best specialised agent. Demonstrates polymorphism + duck typing.
    """

    # Routing keywords - maps keywords to agent types
    _ROUTING_TABLE = {
        "chat"     : ["hello","hi","hey","chat","talk","tell me","explain"],
        "analyst"  : ["analyse","analyze","statistics","average","mean","data","numbers","calculate statistics"],
        "search"   : ["search","find","what is","who is","define","lookup"],
    }

    def __init__(self, name, model="gpt-4o"):
        super().__init__(name,model)
        self._sub_agents = {}
        self._route_log = []
        self._info(f"RouterAgent '{name}' ready")

    @property
    def agent_type(self):
        return "router"

    def register_agent(self, agent_type, agent):
        """
        Register a sub-agent for a given type.
        Duck tpying - any object with .run() works.
        """
        if not hasattr(agent, "run"):
            raise TypeError("Registered agent must have a run() method")
        self._sub_agents[agent_type] = agent
        self._info(f"Registered agent", {"type": agent_type})
        return self

    def run(self, user_input):
        """ROute input to the best available agent."""
        agent_type = self._determine_route(user_input)
        self._route_log.append({"input": user_input[:40], "routed_to": agent_type})
        if agent_type not in self._sub_agents:
            self._warn(f"No agent got type '{agent_type}' ")
            if self._sub_agents:
                agent_type = list(self._sub_agents.keys())[0]
                self._info(f"Failing back to '{agent_type}' ")
            else :
                return f"No agents registered. Please register agents first."
        selected_agent = self._sub_agents[agent_type]
        self._info(f"Routing to agent", {
            "type"  : agent_type,
            "agent" : getattr(selected_agent, "name", "unknown")
        })

        #polymorphism : run() works differently per agent type
        return selected_agent.run(user_input)

    def routing_summary(self):
        """Summary of all routing decisions made."""
        counts = {}
        for entry in self._route_log:
            t = entry["ruted_to"]
            counts[t] = counts.get(t, 0) + 1
        return {
            "total_routed"     : len(self._route_log),
            "routes"           : counts,
            "registered_types" : list(self._sub_agents()),
        }