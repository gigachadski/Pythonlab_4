def count_vowel(s):
    count=0
    vowels={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for letter in s:
        if letter in vowels:
            count += 1

    return count
test_strs=[
    "Hello World",
    "Python",
    "Rhythm",
    "AEIOU aeiou"
]
for text in test_strs:
    print(f"Vowels in your text:{count_vowel(text)}")


def analyze_char_frequency(text):
    frequency = {}
    text = text.lower()

    for char in text:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency
test_texts = [
    "Hello, Python Developer!",
    "Data structure",
    "A a B b C c"
]

print("--- Частотний аналіз текстів ---")
for sample in test_texts:
    result = analyze_char_frequency(sample)
    print(f"\nОригінальний текст: '{sample}'")
    for char, count in result.items():
        print(f"Літера '{char}': {count} раз(и)")