from pathlib import Path
import json
import sqlite3

def parse_to_db(source):
    """Parses a JSON object source and returns a tuple with the word as a str and the json object as a JSON formatted string."""
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
                
    return (entry["word"], json.dumps(entry, ensure_ascii=False),)

source_path = Path.cwd() / "text files" / "kaikki.jsonl"
#output_path = Path.cwd().parent / "text files" / "output.jsonl"

source = source_path.open("r", encoding="utf-8")
#output = output_path.open("a", encoding="utf-8")

con = sqlite3.connect("wiktionary-latin.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS dictionary
            (word TEXT NOT NULL,
            details TEXT NOT NULL CHECK (json_valid(details)))""")

for line in source:
    entry = parse_to_db(line.strip())
    cur.execute("INSERT INTO dictionary VALUES(?, ?)", entry)

source.close()
con.commit()
print("done")
#output.close()
