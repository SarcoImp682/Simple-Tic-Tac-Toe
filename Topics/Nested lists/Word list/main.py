text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

value = int(input())
value_list = [word for sentence in text for word in sentence if len(word) <= value]
print(value_list)
