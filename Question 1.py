# Cindy Hightower Homework 1 Question 1


words = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
def count_vowels(word):
    vowels = ['a', 'e', 'i' 'o', 'u']
    vowel_count = 0

    for letter in word:
        if letter.lower() in vowels:
            vowel_count += 1

    return vowel_count

total_vowel_count = 0
for word in words:
    total_vowel_count += count_vowels(word)
    word_vowels = count_vowels(word)
    print(f"The number of vowels in {word} is {word_vowels}")

print(" The number of vowels in", words, "is", total_vowel_count)