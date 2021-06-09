class Word:
    def __init__(self, pos, tag, lemma, dep):
        self.pos = pos
        self.lemma = lemma
        self.tag = tag
        self.dep = dep

    def get_lemma(self):
        return self.lemma

    def get_pos(self):
        return self.pos

    def get_tag(self):
        return self.tag

    def get_dep(self):
        return self.dep

    def get_word(self):
        return self.pos + " - " + self.tag + " - " + self.lemma + " - " + self.dep
