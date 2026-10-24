from pathlib import Path
import json

def parse(source, output):
    """Parses a JSON object source and appends a cleaned JSON object string to file output."""
    raw = json.loads(source)
    entry = {}

    entry["word"] = raw.get("word") or ""
    entry["pos"] = raw.get("pos") or ""
    
    entry["expansions"] = []
    if "head_templates" in raw:
        for head in raw["head_templates"]:
            entry["expansions"].append(head.get("expansion") or "")
            
    entry["etymology_text"] = raw.get("etymology_text") or ""

    #I type cast to int because I am uncertain whether etymology_number is an int or a str in certain entries, /
    #though I think it is probably a str in most if not all of the wikitionary data.
    entry["etymology_number"] = int(raw.get("etymology_number") or 0)

    entry["is_link"] = False
    
    
    entry["meanings"] = []
    entry["alt_of"] = []
    entry["form_of"] = []
    if "senses" in raw:
        i = 0
        entry["meanings"].append([])
        for sense in raw["senses"]: 
        
            if "head_nr" in sense:
                if (sense["head_nr"] - 1 > i):
                    entry["meanings"].append([])
                    i = i + 1
            entry["meanings"][i].append(sense.get("glosses") or [])
            if "alt_of" in sense:
                entry["is_link"] = True
                entry["alt_of"].append(sense["alt_of"])            
            if "form_of" in sense:
                entry["is_link"] = True
                entry["form_of"].append(sense["form_of"])
                
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



    
