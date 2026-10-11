from pathlib import Path
import json

def parse(source, output):
    raw = json.loads(source)
    entry = {}

    entry["word"] = raw.get("word") or ""
    entry["pos"] = raw.get("pos") or ""
    
    entry["expansions"] = []
    if "head_templates" in raw:
        for head in raw["head_templates"]:
            entry["expansions"].append(head.get("expansion") or "")
            
    entry["etymology_text"] = raw.get("etymology_text") or ""
    
    if ("etymology_number" in raw) and (isinstance(raw["etymology_number"], str)):
        entry["etymology_number"] = int(raw["etymology_number"])
    elif ("etymology_number" in raw) and (isinstance(raw["etymology_number"], int)):
        entry["etymology_number"] = raw["etymology_number"]
    else:
        entry["etymology_number"] = 0
        
    entry["is_link"] = False

    entry["alt_of"] = []
    entry["form_of"] = []
    if "senses" in raw:
        for sense in raw["senses"]: 
            if "alt_of" in sense:
                entry["is_link"] = True
                entry["alt_of"].append(sense["alt_of"])
            
            if "form_of" in sense:
                entry["is_link"] = True
                entry["form_of"].append(sense["form_of"])
              
    entry["meanings"] = []
    if "senses" in raw:
        i = 0
        entry["meanings"].append([])
        for sense in raw["senses"]:            
            entry["meanings"][i].append(sense.get("glosses") or [])
            if "head_nr" in sense:
                if (sense["head_nr"] - 1 > i):
                    entry["meanings"].append([])
                    i = i + 1

    output.write(json.dumps(entry, ensure_ascii=False) + "\n")

source_path = Path.cwd().parent / "text files" / "kaikki.jsonl"
output_path = Path.cwd().parent / "text files" / "output.jsonl"

source = source_path.open("r", encoding="utf-8")
output = output_path.open("a", encoding="utf-8")

for line in source:
    parse(line.strip(), output)    

print("done")

source.close()
output.close()



    
