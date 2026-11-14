README

INSTALLATION & USAGE

First, download the files parse_to_db.py and lookup.py. Make sure that they are in the same folder. Next, go to https://kaikki.org/dictionary/Latin/ and scroll down to the "Download" section. Click the hyperlink to download the postprocessed JSONL data for the entire Latin dictionary. Make sure that the JSONL file is in the same folder as parse_to_db.py and lookup.py and rename it to kaikki.jsonl Next, open the terminal. Run parse_to_db.py by using

python3 /path/to/parse_to_db.py

or by navigating to the folder containing parse_to_db.py, then using

python3 parse_to_db.py

This take about a minute or two to execute. Once finished, you will have a SQLite db file that stores the dictionary.

Next, download the lookup file (Note: this is not the same as lookup.py). Move this file to /usr/local/bin. Then, change the path in line 3 of the file to the correct path of lookup.py. This will depend on where you chose to tore lookup.py. Once this is done, In the terminal, run

chmod +x lookup

You should now be able to query the dictionary through the terminal using

lookup WORD

where WORD is the word you wish to look up.

PARSING

Wiktionary stores an enormous amount of data for each entry. This makes simply copying Wiktionary impractical for reading entries in the terminal. I therefore chose to keep only the most useful portion of that information.

The JSON schema for one entry is as follows:

{
	"word": "" #str	
	"pos": ""  #str
	"expansions": [] #array of str. 
	"etymology_text": ""  #str	
	"etymology_number": 0  #int
	"is_link": false #boolean
	"alt_of": []  #array
	"form_of": [] #array	
	"meanings": [  #array of arrays of arrays
		       [
		           []
		       ]
		   ]
}

"word": This is simply the word being described by the entry. It is the key used by lookup.py to query the database. However, it is not a uniquekey . Multiple entries, i.e. entries for different meanings of the same word, may have the same value in "word". "word" is not limited to storing only the headword of a word, e.g. the nominative form of a noun or the first principal part of a verb, but also inflections. In that case, the entry directs the user to the headword. The default value is an empty string.

"pos": the part of speech of the word. The default value is an empty string.

"expansions": This is an array of strings. Each string is essentially a subheading for the entry. Despite being an array, most entries only have a single element in "expansions". On occasion, an entry will have multiple elements. An example is one of the entries for "ut," which has the following:

"expansions": ["ut (followed by the subjunctive)", "ut (followed by the indicative)"]

The default value is an empty array.

"etymology_text": a string containing etymological information on the word. This field can sometimes get quite large. The default value is an empty string.

"etymology_number": This is used when a word is spelled the same but has different meanings based its etymology. This happens when two originally distinct words evolve to have the same spelling over time. Each etymology will receive its own entry, and will be assigned a number. Most entries, however, will have the default value, meaning that the word does not have different etymological origins. The default value is zero.

"is_link": A boolean value used to indicate whether the word is an alternative form of another word (e.g. "expecto" vs "exspecto"), or is an inflection of another word (e.g. "domu" is an inflection of "domus"; "dixit" is an inflection of "dico"). The default value is false.

"alt_of": If the word is an alternative form of any other words, those words will go here. For example, "expecto" and "exspecto" are alternative spellings. THe default value is an empty array.

"form_of": If the word is an inflection of any other words, those words will go here. For example, "laudaris" is an inflection of "laudo." THe default value is an empty array.

"meanings":  
















