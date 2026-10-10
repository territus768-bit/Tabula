import json
from pprint import pp

path = "thesaurus.txt"

with open(path, "r", encoding="utf-8") as f:
    raw = json.load(f)

entry = {"word": raw["word"],
        "pos": raw["pos"],
         "etymology_text": raw["etymology_text"],
         "expansion": raw["head_templates"][0]["expansion"],
         "meanings": []
         }
for sense in raw["senses"]:
    entry["meanings"].append(sense["glosses"])

pp(entry, indent=4)
