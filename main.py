import json
import difflib

dictionary = json.load(open("dictionary.json"))


class Dictionary:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Dictionary, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.data: dict = dictionary

    def lookup(self, word: str):
        results: str | bool = self.data.get(word.lower(), False)
        if results:
            print(length := len(results), f"result{'s' if length > 1 else ''} found")
            for result in results:
                print(word, ":", result)
        else:
            suggestions = difflib.get_close_matches(word, self.data.keys(), 3)
            print(f"No results found. You may be looking for ({' - ' .join(suggestions)})", )


if __name__ == "__main__":
    translator = Dictionary()
    while (word := input("Please enter a word: ")) != r"\exit":
        translator.lookup(word)
