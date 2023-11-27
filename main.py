def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    char_list = sorted(get_character_count(text).items(), key = lambda tuple: tuple[1], reverse = True)
    for character in char_list:
        if character[0].isalpha():
            print(f"The '{character[0]}' character was found {character[1]} times")
    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    word_list = text.split()
    return len(word_list)

def get_character_count(text):
    characters = {}
    for character in text.lower():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

main()