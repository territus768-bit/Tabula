import json

extract = {"word":"",
           "meanings": []
        }


with open("../text files/deus.json", "r") as f:
    object = json.load(f)

extract["word"] = object["word"]



for sense in object["senses"]:
    for gloss in sense["glosses"]:
        extract["meanings"].append(gloss)



print(extract)
