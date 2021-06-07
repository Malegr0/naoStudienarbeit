import spacy

nlp = spacy.load("de_core_news_sm")


def initialize_array(array_length):
    global found_words

    found_words = [["0" for i in range(array_length)] for j in range(14)]
    all_tags = ["ADJ","ADP","ADV","CONJ","CCONJ","DET","INTJ","NOUN","NUM","PART","PRON","PROPN","SCONJ","VERB"]
    for x in range(14):
        found_words[x] = all_tags[x]
        #print(type(found_words[i]))


def sentence_detection(sentence):
    global token

    initialize_array(len(sentence))
    for token in sentence:
        token.lemma_ = token.lemma_.lower()
        check_word()

        #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)


def check_word():
    if token.pos_ == "AUX":
        pass  # print("Der UPOS-Tag "" + upos + "" ist rausgeflogen.")
    elif token.pos_ == "PUNCT":
        pass  # print("Der UPOS-Tag "" + upos + "" ist rausgeflogen.")
    else:
        check_specific()


def check_specific():
    if token.tag_ == "PPER":
        pass  # print("Der Tag "" + tag + "" ist rausgeflogen.")
    elif token.tag_ == "ART":
        pass  # print("Der Tag "" + tag + "" ist rausgeflogen.")
    elif token.tag_ == "ADJD":
        pass  # print("Der Tag "" + tag + "" ist rausgeflogen.")
    elif token.tag_ == "PROAV":
        pass  # print("Der Tag "" + tag + "" ist rausgeflogen.")
    else:
        for i in range(14):
            if token.pos_ == found_words[i] and found_words[i][0] != "0":
                word = str(token.lemma_)
                found_words[i][0] = word
                print("Wort: " + str(found_words[i]))
        print(str(token.lemma_) + " - " + str(token.pos_) + " - " + str(token.tag_) + " - " + spacy.explain(token.tag_))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Successfully executed!")
