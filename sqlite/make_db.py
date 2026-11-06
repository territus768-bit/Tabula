import sqlite3
from pathlib import Path
import json

con = sqlite3.connect("wiktionary-latin.db")
cur = con.cursor()

#word is the word itself and is going to be used as the searching key.
#details stroes the json object.
cur.execute("""CREATE TABLE IF NOT EXISTS dictionary
            (word TEXT NOT NULL,
            details TEXT NOT NULL CHECK (json_valid(details)))""")

source_path = Path.cwd().parent / "text files" / "output.jsonl"
if source_path.exists():
    with open(source_path, "r", encoding="utf-8") as source:
        for line in source:            
            entry = json.loads(line.strip())
            cur.execute("INSERT INTO dictionary VALUES(?, ?)", (entry["word"], line,))
    con.commit() 
    print("done")
else:
    print("output.jsonl doesn't exist")




            
