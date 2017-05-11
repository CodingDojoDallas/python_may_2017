phrase = ["My","alter","ego","is","ninja","panda"]
char = "a"
new_phrase = []

for item in phrase:
    if item.find(char) != -1:
        new_phrase.append(item)
        print new_phrase
