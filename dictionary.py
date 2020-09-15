import json
from difflib import get_close_matches

data = json.load(open("data.json"))


# print(data)

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), n=5)) > 0:
        yn = input("Do you mean %s instead? If Yes press Y else press N: " % get_close_matches(w, data.keys(), n=5)[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys(), n=5)[0]]
        elif yn == "N":
            return "Word doesn't exist.Please enter different word."
        else:
            return "Didn't understand this word.Enter correct word."
    else:
        return "Word doesn't exist. Please enter different word."


while True:
    word = input("Enter Word:")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
