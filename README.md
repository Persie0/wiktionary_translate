# wiktionary_translate
Get English translations of foreign word with Wiktionary

GitHub: https://github.com/Persie0/wiktionary_translate


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/marvinperzi#)

<a href="https://paypal.me/marvinperzi?country.x=AT&locale.x=de_DE"><img src="https://github.com/andreostrovsky/donate-with-paypal/raw/master/blue.svg" height="36"></a>

# Usage 
You can only get the English definitions of foreign words
```python
from wiktionary_translate.wiktionary_translate import WiktionaryResult

if __name__ == "__main__":

    wr = WiktionaryResult()
    if wr.query(word="essen", lang="de"):
        print(wr.definitions) # ['to eat']
        print(wr.partOfSpeech) # Verb
        print(wr.definitionList[0].parsedExamples) # {'Er isst gern Schokolade.': 'He likes eating chocolate.', '...}
        print(wr.definitionList[0].examples) # ['Er isst gern Schokolade.', 'Ich esse einen Apfel.']
        print(wr.definitionList[0].definition) # to eat
        print(wr.rawResult) # {'other': [{'partOfSpeech': 'Verb', 'language': 'Alemannic German', ...
```
&nbsp;
