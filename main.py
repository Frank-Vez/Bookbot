import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"this text has {num_words}")
    letter_dict = count_letters(text)
   # print(f"The count of letters is: {letter_dict}")
    alpha_list = clean_dict(letter_dict)
    alpha_list.sort(key=get_key, reverse=True)
    final_print(book_path,num_words,alpha_list)


def final_print(path, num, list):
      print("----here's the report of the book you asked-----")
      print(f"-----this should be your book: {path}----")
      print(f"---There is {num} in this book-----")
      print(f"---------and here<s a run down of the letters too:--------")
      for i in range(0,len(list)):
          for letter, count in list[i].items():
            print(f"there is {count} appearances of {letter} ")
      print("------- good read!----------")

def get_key(dict):
    for letter in dict:
        return dict[letter]
    
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