text = "hello world"
vowels = "aeiou"
count = sum(1 for ch in text if ch in vowels)
print("Vowel count:", count)
