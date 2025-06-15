def is_palindrome(word):
    return word == word[::-1]

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)

def sum_digits(n):
    return sum(int(d) for d in str(n))
