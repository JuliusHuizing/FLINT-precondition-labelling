import spacy
from spacy import displacy
from spacy.tokens import Span

class SpacyLabelVisualizer:
    """
    A class for visualizing semantic labels using Spacy's DisplaCy visualization tool.

    This class helps in visualizing text data where each word in the sentence is 
    tagged with a semantic label. It supports custom color coding for different 
    labels.

    Attributes:
        nil_label (str): The label used for words that do not have a specific semantic role.
        _label_color_dict (dict): A dictionary mapping labels to colors for visualization.
        _possible_labels (list): List of possible labels (extracted from the keys of `_label_color_dict`).
    """

    def __init__(self, 
                 label_color_dict: dict = {
                     "Recipient": "aquamarine",
                     "Object": "tomato",
                     "Actor": "pink",
                     "P": "yellow",  # Note: One-letter labels to reduce token usage.
                     "Action": "green",
                 }, 
                 nil_label: str = "O"):
        """
        Initializes SpacyLabelVisualizer with a dictionary for label colors and a default label for non-entities.

        Args:
            label_color_dict (dict, optional): A dictionary mapping semantic role labels to colors. Defaults to a predefined set of label-color pairs.
            nil_label (str, optional): The label to be used for non-entities or irrelevant words. Defaults to 'O'.
        """
        self.nil_label = nil_label
        self._label_color_dict = label_color_dict
        self._possible_labels = list(label_color_dict.keys())
        
    def create_displacy_dict(self, words, labels):
        """
        Creates a dictionary formatted for use with Spacy's displaCy render method.

        This method pairs words with their corresponding semantic labels and calculates
        the start and end indices for each word in the sentence.

        Args:
            words (list of str): The list of words in the sentence.
            labels (list of str): The list of semantic labels corresponding to each word.

        Returns:
            dict: A dictionary formatted for Spacy's displaCy visualization.
        """
        sentence = ' '.join(words)
        entities = []
        start = 0

        for word, label in zip(words, labels):
            end = start + len(word)
            if label != self.nil_label:
                entities.append({"start": start, "end": end, "label": label})
            start = end + 1

        return {"text": sentence, "ents": entities, "title": None}
    
    def display(self, words, labels):
        """
        Generates and returns HTML content for visualizing the semantic labels using Spacy's displaCy.

        This method calls `create_displacy_dict` to format the input data and then uses Spacy's displaCy
        to render the HTML content for visualization.

        Args:
            words (list of str): The list of words in the sentence.
            labels (list of str): The list of semantic labels corresponding to each word.

        Returns:
            str: HTML content for the rendered visualization.
        """
        displacy_dict = self.create_displacy_dict(words, labels)
        colors = self._label_color_dict
        html = displacy.render(displacy_dict, style="ent", manual=True, options={"colors": colors})
        return html
