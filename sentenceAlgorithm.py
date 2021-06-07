import spacy

nlp = spacy.load("de_core_news_sm")


def sentence_detection(sentence):
    global token
    for token in sentence:
        upos = token.pos_
        tag = token.tag_
        check_word(upos, tag)
        # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)


def check_word(upos, tag):
    if upos == "AUX":
        pass  # print("Der UPOS-Tag "" + upos + "" ist rausgeflogen.")
    elif upos == "PUNCT":
        pass  # print("Der UPOS-Tag "" + upos + "" ist rausgeflogen.")
    else:
        check_specific(tag)


def check_specific(tag):
    if tag == "PPER":
        pass  # print("Der Tag "" + tag + "" ist rausgeflogen.")
    elif tag == "ART":
        pass  # print("Der Tag "" + tag + "" ist rausgeflogen.")
    elif tag == "ADJD":
        pass  # print("Der Tag "" + tag + "" ist rausgeflogen.")
    elif tag == "PROAV":
        pass  # print("Der Tag "" + tag + "" ist rausgeflogen.")
    else:
        print(str(token) + " - " + spacy.explain(tag))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Successfully executed!")
