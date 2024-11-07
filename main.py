def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    character_count = get_character_count(text)
    num_words = count(text)
    character_report = report(character_count)

    print(f"--- Begin report of {book_path}---")
    print(f"{num_words} words found in the document")
    for c in character_report:
        print(f"The {c['letter']} character was found {c['count']} times")
    print("---End Report---")

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

def report(character_count):
    def sort_on(character_count):
        return character_count["count"]
    word_count_sentence = []
    alpha_array = []
    for c, count in character_count.items():
        if c.isalpha():
            alpha_array.append({'letter':c,'count':count})
    
    alpha_array.sort(reverse=True, key=sort_on)
    return alpha_array


main()