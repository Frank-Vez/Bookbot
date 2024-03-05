import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"this text has {num_words}")
    letter_dict = count_letters(text)
   # print(f"The count of letters is: {letter_dict}")
    alpha_dict = clean_dict(letter_dict)
    print("----here's the report of the book you asked-----")
    print(f"-----this should be your book: {book_path}----")
    print(f"---There is {num_words} in this book-----")
    print(f"---------and here<s a run down of the letters too:--------")
    for i in range(0,len(alpha_dict)):
        print(alpha_dict[i])
        for letter, count in alpha_dict[i].items():
            
            print(f"there is {count} appearances of {letter} ")


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