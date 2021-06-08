class Word:
    def __init__(self, pos, tag, lemma):
        self.pos = pos
        self.lemma = lemma
        self.tag = tag

    def get_lemma(self):
        return self.lemma

    def get_pos(self):
        return self.pos

    def get_tag(self):
        return self.tag

    def get_word(self):
        return self.pos + " - " + self.tag + " - " +self.lemma
