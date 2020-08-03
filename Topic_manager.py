from Topic import word_uniformization, compare_words

class Topic_manager:
    def __init__(self, topics = [], discarded_words = [], similarity_threshold = 0.8):
        self.topics = topics
        self.topics_names = []
        for t in topics:
            self.topics_names.append(t.name)
        self.discarded_words = discarded_words
        self.similarity_threshold = similarity_threshold

    def is_topic(self, name):
        return name in self.topics_names

    def add_single_topic(self, topic):
        if topic.name not in self.topics_names:
            self.topics.append(topic)
            self.topics_names.append(topic.name)
        else:
            print("Nothing added, there is already a topic with this name")

    def add_topics(self, topics):
        if type(topics) == list:
            for t in topics:
                self.add_single_topic(t)
        else:
            self.add_single_topic(topics)

    def get_topic_list(self):
        return self.topics_names

    def print_topic_list(self):
        for t in self.topics_names:
            print(t)

    def rm_single_topic(self, name):
        if name in self.topics_names:
            self.topics_names.remove(name)
            for t in self.topics:
                if t.name == name:
                    self.topics.remove(t)
                    break

    def rm_topics(self, names):
        if type(names) == list:
            for n in names:
                self.rm_single_topic(n)
        else:
            self.rm_single_topic(names)

    def get_scores(self, sentence):
        scores, words_present, words_absent_temp = [], [], []
        for t in self.topics:
            s, wp, wa = t.get_score(sentence, self.similarity_threshold)
            scores.append(s)
            words_present.append(wp)
            words_absent_temp.append(wa)
        words_present_list = list(set([i for it in words_present for i in it]))
        words_absent_temp = list(set([i for it in words_absent_temp for i in it]))
        words_absent = []
        for w in words_absent_temp:
            if w not in words_present_list:
                if w not in self.discarded_words:
                    words_absent.append(w)
                    
        return scores, words_present, words_absent

    def add_word_2_topic(self, word, topic_name):
        if not self.is_topic(topic_name):
            print("%s is not a topic currently" % topic_name)
            return -1

        for t in self.topics:
            if t.name == topic_name:
                t.add_keyword(word)
                return 1

    def rm_word_from_topic(self, word, topic_name):
        if not self.is_topic(topic_name):
            print("%s is not a topic currently" % topic_name)
            return -1

        for t in self.topics:
            if t.name == topic_name:
                t.rm_keyword(word)
                return 1

    def is_discarded(self, word):
        w2 = word_uniformization(word)
        for w in self.discarded_words:
            if compare_words(w2, w) > self.similarity_threshold:
                return True
        return False

    def discard(self, word):
        if self.is_discarded(word):
            return
        self.discarded_words.append(word_uniformization(word))

    def discard_list(self, word_list):
        for w in word_list:
            self.discard(w)
