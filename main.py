import spacy
import sentence_algorithm

nlp = spacy.load("de_core_news_sm")
detected_sentence = "Was kannst du mir über den Studiengang Informatik erzählen?"
doc = nlp(detected_sentence)
sentence_algorithm.sentence_detection(doc)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Successfully executed!")

