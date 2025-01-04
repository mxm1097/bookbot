def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_word_count(text)
  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words found in the document.")
  print("\n")
  letter_count = get_character_count(text)
  for i in letter_count:
    print(f"The {i} character was found {letter_count[i]} times")
  print("--- End report---")
  

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  words = text.split()
  return len(words)

def get_character_count(text):
    chars = {}
    for c in text:
      lowered = c.lower()
      if lowered in chars:
        chars[lowered] += 1
      else:
        chars[lowered] = 1
    return chars
    
    

main()