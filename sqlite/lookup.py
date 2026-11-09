import sqlite3
import pathlib
from pprint import pprint
import json

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
        for item in result.fetchall():
            entry = json.loads(item[1])
            word_name = entry['word']
            part_of_speech = entry['pos']
            etymology_text = entry['etymology_text']
            expansions = entry['expansions']
            meanings = entry['meanings']
            print(f"{word}, {part_of_speech}\n{etymology_text}")
            print("etymology-numb: " + str(entry['etymology_number']))
            j = 0
            for expansion in expansions:
                print(expansion)
                meaning = meanings[j]
                j = j + 1                
                i = 1
                for submeaning in meaning:
                    print(f"{i}.", end = " ")
                    i = i + 1
                    for subsubmeaning in submeaning:
                        print(f"-{subsubmeaning}")
            


            
            #print(f"""word: {entry['word']}, {entry['pos']}
            #        {entry['expansions']}
             #       Etymology: {entry['etymology_text']}
            #        Meanings: {entry['meanings']}""")
            
        #print(result.fetchall() or "word not found : (")
               
word = "ut"
lookup(word)
