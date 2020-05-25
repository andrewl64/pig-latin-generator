original = input("Enter Text: ").lower()

words = original.split()

x = []

for word in words:
    if word[0] in "aeiou":
        x.append(word + "yay")
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        cons = word[:vowel_pos]
        rest = word[vowel_pos:]

        x.append(rest + cons + "ay")

print(" ".join(x))
