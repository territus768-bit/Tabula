import sqlite3
import pathlib
from pprint import pprint

dict_path = "wiktionary-latin.db"
dictionary = pathlib.Path(dict_path)

def lookup(word: str):
    if not dictionary.exists():
        print("wiktionary-latin.db needs to be created in the same directory as lookup.py")
    else:
        con = sqlite3.connect(dict_path)
        cur = con.cursor()
        result = cur.execute("""SELECT *
                            FROM dictionary
                            WHERE word = ?""", (word,))
        pprint(result.fetchall() or "word not found : (")
               
word = "ut"
lookup(word)
