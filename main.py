import spacy
from sentenceAlgorithm import sentence_detection

sampleText = "Den Körper trainieren viele Menschen. Aber wer trainiert auch sein Gehirn? „Das Gehirn muss genauso " \
             "trainiert werden wie der Körper“, sagt Professor Siegfried Lehrl von der Universität Erlangen-Nürnberg. " \
             "Denn wissenschaftliche Untersuchungen haben gezeigt, dass wir die Leistungsfähigkeit unseres Gehirns um " \
             "10 bis 15% steigern können, wenn wir einige Wochen lang täglich zehn Minuten unser Gehirn trainieren. " \
             "Besonders wichtig ist dieses Gehirn-Jogging für Menschen, die sich im Alltag geistig nur wenig " \
             "anstrengen. Ein Beispiel sind Krankenhauspatienten: Bereits nach wenigen Tagen beginnt ihr " \
             "Intelligenzquotient zu sinken. Nach drei Wochen Krankenhausaufenthalt kann er bereits 20% niedriger als " \
             "gewöhnlich sein. Auch im Alter lässt die Intelligenz oft nach. Dies geschieht nicht nur aus " \
             "körperlichen Gründen, wie z.B. durch zunehmende Verkalkung [1], sondern auch deshalb, weil das Gehirn zu " \
             "wenig beansprucht oder geübt wird. Deshalb hat Professor Lehrl zusammen mit Bernd Fischer, dem Leiter " \
             "einer Rehabilitationsklinik, ein Programm für Gehirn-Jogging entwickelt. Seit einigen Jahren nun bieten " \
             "Krankenhäuser und Altenheime auf der Basis dieses Programms Übungen zum Training des Gehirns an – mit " \
             "großem Erfolg: So erreichte eine siebzigjährige Testperson mit Gehirn-Training das höchste geistige " \
             "Niveau ihres gesamten Lebens. Inzwischen hat sich auch gezeigt, dass dieses Programm für alle Menschen " \
             "nützlich ist. Professor Lehrl selbst absolviert [2] Übungen aus diesem Programm, wenn er sich geistig " \
             "müde fühlt oder wenn er einen schwierigen Text schreiben muss. Denn das Lösen der Aufgaben bringt das " \
             "Gehirn in Bewegung; es wird dadurch zugleich besser durchblutet und mit Sauerstoff versorgt. Die " \
             "Aufgaben des Programms zielen vor allem darauf ab, die Geschwindigkeit der Informationsverarbeitung und " \
             "die sogenannte Gegenwartsdauer zu erhöhen. Mit „Gegenwartsdauer“ bezeichnet man den Zeitraum, " \
             "in dem neue Informationen im sogenannten Kurzzeitgedächtnis präsent [3] sind. Er umfasst normalerweise " \
             "bis zu fünf Sekunden. Wenn nun durch Gehirn-Jogging dieser Zeitraum erreicht oder sogar noch " \
             "ausgeweitet wird, können wir mehr Informationen länger behalten und schneller verarbeiten. "

nlp = spacy.load("de_core_news_sm")

sentence_detection(nlp("Wie lange gibt es die HWR?"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Successfully executed!")

