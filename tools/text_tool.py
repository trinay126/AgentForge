# tools/ text_tool.py
# Text processing tool with multiple operations.

from core.base_tool import BaseTool

class TextTool(BaseTool):
    """
    Performs text analysis: word count, sentiment, reversal, summary.
    """
    POSITIVE_WORDS = {
       "good","great","excellent","amazing","wonderful","fantastic",
        "superb","best","awesome","love","brilliant","helpful","fast",
        "easy","clean","clear","perfect","happy","success","win",
   } 

    NEGATIVE_WORDS = {
        "bad","terrible","awful","worst","horrible","poor","hate",
        "slow","broken","difficult","hard","confusing","fail","error",
    }

    @property
    def name(self):
        return "text_analyser"

    @property
    def description(self):
        return "Analyse text: word count, sentiment, keywords, reverse. Input: any text"

    def run(self, input_text):
        """Detect what kind of analysis is needed and run it."""
        lower = input_text.lower()

        if "reverse" in lower or "backwards" in lower:
            return self._reverse(input_text)

        if "sentiment" in lower or "feeling" in lower or "tone" in lower:
            return self._sentiment(input_text)

        if "count" in lower or "words" in lower or "lenght" in lower:
            return self._word_stats(input_text)

        if "keyword" in lower or "important" in lower:
            return self._keywords(input_text)

        #default: FUll analysis
        return self._full_analysis(input_text)


    