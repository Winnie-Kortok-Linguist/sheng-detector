# Sheng Detector - by Winnie Kortok
# Analyses code-switching between Sheng, Swahili and English
# Data from students in Ruiru, Kenya

sheng_words = ["mambo", "madhaoo", "poa", "sasa", "maze", "mbogi", "kiroma"]
swahili_words = ["leo", "tutaenda", "anadai", "ako", "na", "lakini", "si", "uniangushie", "iko"]
english_words = ["my", "friend", "town", "teacher"]

text = input("Type a sentence from your students: ")

words = text.lower().replace(",", "").replace("?", "").replace("!", "").replace("'", "").replace('"', "").split()

sheng_count = 0
swahili_count = 0
english_count = 0

for word in words:
    if word in sheng_words:
        sheng_count += 1
        print(word, "-> SHENG")
    elif word in swahili_words:
        swahili_count += 1
        print(word, "-> SWAHILI")
    elif word in english_words:
        english_count += 1
        print(word, "-> ENGLISH")
    else:
        print(word, "-> UNKNOWN - add me!")

total = len(words)
print("\n--- RESULT ---")
print(f"Sheng: {sheng_count} / {total} = {sheng_count/total*100:.0f}%")
print(f"Swahili: {swahili_count} / {total} = {swahili_count/total*100:.0f}%")
print(f"English: {english_count} / {total} = {english_count/total*100:.0f}%")
