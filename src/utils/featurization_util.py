import re, nltk, spacy
import pandas as pd
from textblob import TextBlob


class Featurization_Util:
    def __init__(self, data) -> None:
        self.nlp = spacy.load("en_core_web_sm")
        self.data = data
        pass

    def check_nlp_library(self):
        try:
            nltk.data.find('punkt')
        except LookupError:
            nltk.download('punkt')

        try:
            nltk.data.find('averaged_perceptron_tagger')
        except LookupError:
            nltk.download('averaged_perceptron_tagger')

    def normalize_text(self, text_input):
        text_input = text_input.lower()
        pattern = '[^\w\s]' #Remove puncutations
        text_input = re.sub(pattern, '', text_input) 
        pattern = '\w*\d\w*' # Removing words with numbers in between
        text_input = re.sub(pattern, '', text_input) 
        return text_input
    
    def lemmmatize_text(self, text_input):
        sent = []
        doc = self.nlp(text_input)
        for token in doc:
            sent.append(token.lemma_)
        return " ".join(sent)
    
    def get_POS_tags(self, text_input):
        sent = []
        blob = TextBlob(text_input)
        sent = [word for (word,tag) in blob.tags if tag=='NN']
        return " ".join(sent)
    
    def featurize_data(self):
        print("Starting featurization")

        print("...normalizing complaint_what_happened")
        self.data = pd.DataFrame(self.data['complaint_what_happened'].apply(self.normalize_text))
        print("...Finished normalizing complaint_what_happened")

        print("...lemmatizing complaint_what_happened. This can take awhile")
        self.data["complaint_lemmatized"] = self.data["complaint_what_happened"].apply(self.lemmmatize_text)
        print("...Finished lemmatizing complaint_what_happened")

        print("...Removing POS from complaint_what_happened. This can take awhile")
        self.data["complaint_POS_removed"] = self.data["complaint_what_happened"].apply(self.get_POS_tags)
        self.data['complaint_clean'] = self.data['complaint_POS_removed'].str.replace('-PRON-', '')
        print("...Finished removing POS from complaint_what_happened.")

        self.data = self.data[['complaint_what_happened', 'complaint_clean']]