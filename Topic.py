import re

from difflib import SequenceMatcher
import unicodedata

def word_uniformization(w):
    return unicodedata.normalize("NFKD", w).encode('ASCII', 'ignore').lower().decode("utf-8")

def list_uniformization(word_list):
    clean_word_list = []
    for w in word_list:
        w2 = word_uniformization(w)
        if w2 not in clean_word_list:
            clean_word_list.append(w2)
    return clean_word_list

def compare_words(w1, w2, uniformized = True):
    if not uniformized:
        w1, w2 = word_uniformization(w1), word_uniformization(w2)
    return SequenceMatcher(None, w1, w2).ratio()

def sentence_to_word_list(sentence):
    return re.findall(r"\w+", sentence)

class Topic:
    def __init__(self, name, keywords = []):
        self.name = name
        self.keywords = list_uniformization(keywords)

    def is_keyword(self, word):
        w = word_uniformization(word)
        return w in self.keywords

    def add_keyword(self, word):
        w = word_uniformization(word)
        if not self.is_keyword(w):
            self.keywords.append(w)

    def rm_keyword(self, word):
        w = word_uniformization(word)
        if w in self.keywords:
            self.keywords.remove(w)

    def get_score(self, sentence, similarity_threshold):
        s2 = sentence_to_word_list(sentence)

        words_present, words_absent = [], []
        for w in s2:
            w2 = word_uniformization(w)
            isIn = 0
            for r in self.keywords:
                if compare_words(w2, r) > similarity_threshold:
                    words_present.append(w2)
                    isIn = 1
                    break
            if isIn == 0:
                words_absent.append(w2)
        return len(words_present), words_present, words_absent
