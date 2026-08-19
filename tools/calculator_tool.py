# tools/calculator_tool.py
# A Calculator tool - parses and evaluates basic math expressions.

from core.base_tool import BaseTool

class CalculatorTool(BaseTool):
    """
    Evaluates mathematical expressions from text input.
    Supports: +, -, *, /, //, %
    """

    # -- Abstract properties implemented -----------------------------------
    @property
    def name(self):
        return "calculator"

    @property
    def description(self):
        return "Evaluate math expressions. Input: '2+3*4'. Output: result"

    def run(self, input_text):
        """Parse and evaluates a math expression"""
        expression = self._extract_expression(input_text)
        if not expression:
            return "No valid math expression found in input"
        result = self._safe_eval(expression)
        return f"Result of '{expression}' = {result}"

    # -- Private helpers ------------------------------------------------------
    def _extract_expression(self, text):
        """Extract a math expression from natural language"""
        # Keywords that signal a mth problem
        math_triggers = [
            "calculate", "compute", "evaluate", "what is",
            "solve", "find", "=", "+", "-", "*", "/"
        ]

        text_lower = text.lower()
        for trigger in math_triggers:
            if trigger in text_lower:
                #Try to isolate the expression
                for part in text.split():
                    if any(c in part for c in "0123456789"):
                        return self._clean_expression(text)
        return None

    