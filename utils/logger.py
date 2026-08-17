# utils/logger.py
# LoggingMixin - adds structured logging to any class

class LoggingMixin:
    """
    Mixin that adds logging to any class.
    Usage : class MyAgent(LoggingMixin, BaseAgent):....
    No __init__ - mixins should not conflict with other constructors
    """
    _all_logs = []
    