import json

f = open("answers.txt",)
answers_data = json.load(f)
f.close()

f = open("generic_terms.txt",)
generics_terms_data = json.load(f)
f.close()

f = open("synonyms.txt",)
synonyms_data = json.load(f)
f.close()


if __name__ == '__main__':
    print("Successfully executed!")
