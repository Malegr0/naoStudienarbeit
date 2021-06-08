import spacy
import word

nlp = spacy.load("de_core_news_sm")


# Funktion erhält deen erkannten Satz und verarbeitet diesen pro Wort in einer Schleife.
# Das erste Wort wird in Lowercase umgewandelt, um Erkennungsfehler zu vermeiden.
# Danach wird das Wort genauestens untersucht. Am Ende wird der Originalsatz mit dem nun gekürzten Satz verglichen.
def sentence_detection(sentence):
    global token
    global found_words
    new_sentence = ""

    found_words = []

    for token in sentence:
        token.lemma_ = token.lemma_.lower()
        check_word()
    print("Drin geblieben:"
          "\nPos - Tag - Lemma \n")
    for checked_word in found_words:
        print(word.Word.get_word(checked_word))
    print("-----------------------"
          "\nOriginalsatz:"
          "\n" + str(sentence) +
          "\n-----------------------")
    print("Neuer Satz:")
    for checked_word in found_words:
        new_sentence = new_sentence + " " + word.Word.get_lemma(checked_word)
    print(new_sentence + "\n -----------------------")


# Als erstes wird der POS untersucht. Wenn einer der Fälle eintritt, wird das Wort nicht weiter beachtet,
# sondern in der Konsole mit einigen Daten ausgegeben. Kommt das Wort in keinen der Fälle,
# wird es in einer weiteren Funktion auf den TAG überprüft.
def check_word():
    if token.pos_ == "AUX":
        print("Rausgeflogen wegen POS:"
              " \nText: " + token.text +
              " \nLemma: " + token.lemma_ +
              " \nPos: " + token.pos_ +
              " \nTag: " + token.tag_ +
              " \n-----------------------")
    elif token.pos_ == "PUNCT":
        print("Rausgeflogen wegen POS:"
              " \nText: " + token.text +
              " \nLemma: " + token.lemma_ +
              " \nPos: " + token.pos_ +
              " \nTag: " + token.tag_ +
              " \n-----------------------")
    else:
        check_specific()


# Nach dem POS wird der TAG untersucht. Wenn einer der Fälle eintritt, wird das Wort nicht gespeichert,
# sondern in der Konsole mit einigen Daten ausgegeben. Kommt das Wort in keinen der Fälle wird es zusammen mit
# dem POS als Liste in die Liste "found_words" eingefügt.
def check_specific():
    if token.tag_ == "PPER":
        print("Rausgeflogen wegen TAG:"
              " \nText: " + token.text +
              " \nLemma: " + token.lemma_ +
              " \nPos: " + token.pos_ +
              " \nTag: " + token.tag_ +
              " \n-----------------------")
    elif token.tag_ == "ART":
        print("Rausgeflogen wegen TAG:"
              " \nText: " + token.text +
              " \nLemma: " + token.lemma_ +
              " \nPos: " + token.pos_ +
              " \nTag: " + token.tag_ +
              " \n-----------------------")
    elif token.tag_ == "ADJD":
        print("Rausgeflogen wegen TAG:"
              " \nText: " + token.text +
              " \nLemma: " + token.lemma_ +
              " \nPos: " + token.pos_ +
              " \nTag: " + token.tag_ +
              " \n-----------------------")
    elif token.tag_ == "PROAV":
        print("Rausgeflogen wegen TAG:"
              " \nText: " + token.text +
              " \nLemma: " + token.lemma_ +
              " \nPos: " + token.pos_ +
              " \nTag: " + token.tag_ +
              " \n-----------------------")
    else:
        new_word = word.Word(token.pos_, token.tag_, token.lemma_)
        found_words.append(new_word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Successfully executed!")
