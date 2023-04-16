def is_palindrome(word):
    # Convert the word to lowercase and remove any non-alphabetic characters
    word = ''.join(filter(str.isalpha, word)).lower()
    # Check if the word is the same forwards and backwards
    return word == word[::-1]

# Ask the user to input a word
word = input("Enter a word: ")

# Check if the word is a palindrome
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")
