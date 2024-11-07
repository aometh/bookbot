def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    character_count = get_character_count(text)
    num_words = count(text)
    return print(f"{character_count}")


    #print(f"{num_words} words found in the document")

def count(text):
    words = text.split() 
    return len(words)

def get_book_text(path):
   with open(path) as f:
      return f.read()

def get_character_count(text):
    text = text.lower()
    small_text = text.split()
    character_lib = {}
    for word in small_text:
        for c in word:
            if c in character_lib:
                character_lib[c] += 1
            else:
                character_lib.update({c:1})
    return character_lib


main()