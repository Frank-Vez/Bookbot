import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"this text has {num_words}")
    letter_dict = count_letters(text)
   # print(f"The count of letters is: {letter_dict}")
    alpha_dict = clean_dict(letter_dict)
    print(alpha_dict)


def clean_dict(dict):
    clean_dict = []
    for key in dict:
        if(str.isalpha(key)):
            clean_dict.append({key:dict[key]})
    return clean_dict       

def count_letters(text):
    letter_count_dict = {}
    for letter in text.lower():
        if(letter in letter_count_dict):
            letter_count_dict[letter] +=1
        else:
          letter_count_dict[letter] =1
    return letter_count_dict
        

def get_book_text(path):
    with open(path) as f:
        return f.read()
  
def get_num_words(text):
  return len(text.split())
   
main()