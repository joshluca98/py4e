def count(word, letter):
    count = 0
    for character in word:
        if character == letter:
            count = count + 1
    print(count)

word = input("Please enter a word: ")
letter = input("Please enter a letter to search for: ")
count(word, letter)