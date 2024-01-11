import spacy
from spacy import displacy
from spacy.tokens import Span


class SpacyLabelVisualizer:
    def __init__(self, 
                 label_color_dict: dict = {
                     "Recipient": "aquamarine",
                     "Object": "tomato",
                        "Actor": "pink",
                        "P": "yellow", # note that the number of tokens we generate influences costs, so ideally we use one letter labels.
                        "Action": "green",
                     
                     }, 
                 nil_label: str = "O"):
        self.nil_label = nil_label
        self._label_color_dict = label_color_dict
        self._possible_labels = list(label_color_dict.keys())
        
    def create_displacy_dict(self, words, labels):
        # Join the words into a single string (sentence)
        sentence = ' '.join(words)

        # Initialize the list of entities
        entities = []
        start = 0

        for word, label in zip(words, labels):
            end = start + len(word)  # Calculate end index of the word
            if label != self.nil_label:  # Assuming 'O' is the label for non-entities
                entities.append({"start": start, "end": end, "label": label})
            start = end + 1  # Update start index for next word (+1 for space)

        # Create the dictionary in the required format
        displacy_dict = {
            "text": sentence,
            "ents": entities,
            "title": None
        }

        return displacy_dict    
    
    def display(self, words, labels):
        displacy_dict = self.create_displacy_dict(words, labels)
        colors = self._label_color_dict
        html = displacy.render(displacy_dict, style="ent", manual=True, options={"colors": colors})
        return html



