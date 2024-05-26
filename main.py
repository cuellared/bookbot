def main():
    book_to_use = "books/frankenstein.txt"
    #book_to_use = "books/testing.txt"
    
    text = open_book(book_to_use)
    #print(type(text))
    #print(text)
    
    num_words = count_words(text)
    #print(num_words)
    #print(f"{num_words} words found in the document")
    
    lista_numero_letters = count_letters(text)
    #print(lista_numero_letters)
    
    #chars_dict = get_chars_dict(text)
   # print(chars_dict)

    chars_list = convert_to_list(lista_numero_letters)


    chars_list.sort(key=sort_on,reverse=True)

    #print("ordenado")
    #print(chars_list)

    print_a_report(book_to_use,num_words,chars_list)
    
    #numero_letters = count_letters(text)
    #for i in numero_letters:
    #    print(f"{i} numero_letters {numero_letters[i]}")

def open_book(book_name):
    with open(book_name) as f:
        file_contents = f.read()
        return file_contents

def count_words(content):
    words = content.split()
    #print(words)
    return len(words)

def count_letters(content):
    
    num_letters = {}
    for word in content:
        lowered_word = word.lower()
        #print(lowered_word)
        for letter in lowered_word:
            #print(letter)
            if letter not in num_letters:
                num_letters[letter] = 1
            else:
                num_letters[letter] = num_letters[letter] + 1
           #print(num_letters)
    return num_letters

#def get_chars_dict(text):
#    chars = {}
#    for c in text:
#        lowered = c.lower()
#        if lowered in chars:
#            chars[lowered] += 1
#        else:
#            chars[lowered] = 1
#    return chars 


def sort_on(dict):
    parejas = dict.items()
    #print(type(parejas))
    #print(parejas)
    for letra in dict:
        #print(letra)
        #print(letra)
        num = dict[letra]
        #print(num)

    return num

def convert_to_list(dict):
    lista = []
    for letter in dict:
        dic_temp ={}
        dic_temp[letter] = dict[letter]
        #print(dic_temp)
        #print(lista)
        lista.append(dic_temp)
    return lista

def print_a_report(book,words_found,lista_letras):
    print(f"--- Begin report of {book} ---")
    print(f"{words_found} words found in the document")
    print("")
    for par in lista_letras:
        for letra in par:
            if not letra.isalpha():
                continue
            print(f"The '{letra}' character was found {par[letra]} times.")
    print("--- End report ---")

main()