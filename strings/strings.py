import re
import unicodedata

def str_len(str):
    clean_str = str.replace(' ', '')
    len_str = len(clean_str)

    return f'{len_str} caractère{'s' if len_str > 1 else ""}'

def name_greetings(name):
    capitalized_name = name.capitalize()

    if len(capitalized_name.split('-')) > 1 :
        splitted_name = capitalized_name.split('-')      
        capitalized_splitted_name = [name.capitalize() for name in splitted_name]
        capitalized_name = "-".join(capitalized_splitted_name)

    return f'Bonjour {capitalized_name}'

def ends_with_exclamation(str):
    last_car = str[-1:]
    if last_car == "!":
        return True
    else :
        return False
    
def reverse_words(str):
    splitted_str = str.split(" ")
    reverse_str = splitted_str[::-1]
    reverse_words = " ".join(reverse_str)

    return reverse_words

def letter_occurences(str, letter):
    str = str.lower()
    letter = letter.lower()
    occurence = str.count(letter)

    return occurence

def str_to_camel_case(str):
    str = str.split("_")
    camel_case = ''

    for index, word in enumerate(str):
        if index == 0:
            camel_case = camel_case + word
        else:
            camel_case = camel_case + word.capitalize()

    return camel_case

def get_vowels_from_str(str):
    vowels_count = 0
    for char in str:
        if(re.match('[aàâeëéèioôuùïAEIOU]', char)):
            vowels_count = vowels_count + 1

    return vowels_count

def alternate_upper_lower(str):
    upper_lower_str = ""

    for index, char in enumerate(str):
        if index % 2 == 0:
            upper_lower_str = upper_lower_str + char.capitalize()
        else:
            upper_lower_str = upper_lower_str + char

    return upper_lower_str

def remove_duplicates(str):
    remove_duplicates_str = ""
    i = 0
    while i < len(str) :
        if(str[i] != str[i-1]):
            remove_duplicates_str = remove_duplicates_str + str[i]
        i+=1
        
    return remove_duplicates_str

def get_initials(name):
    name = name.split(" ")
    name_initials = ""

    for n in name:
        name_initials = name_initials + n[0].capitalize()

    return name_initials

def mask_string(str, number):
    str = str[-number:]
    return str

def is_palindrome(str):
    str = str.lower()
    clean_str = ''

    for char in str:
        if char.isalpha():
            match char :
                case 'ç':
                    clean_str = clean_str + 'c'
                case 'â'| 'à':
                    clean_str = clean_str + 'a'
                case 'é' |'è'| 'ê'| 'ë':
                    clean_str = clean_str + 'c'
                case 'ô':
                    clean_str = clean_str + 'o'
                case 'ï':
                    clean_str = clean_str + 'i'
                case _:
                    clean_str = clean_str + char             
                    
    return clean_str == clean_str[::-1]

def longest_sequence(str):
    sequences = []
    i = 0
    n = 0

    while i < len(str) -1  :
        if(str[i] == str[i+1]):
            n += 1
        else:
            n+=1
            sequences.append((str[i], n))            
            n = 0

        i+=1
    
    sequences.append((str[-1:], n + 1))

    longest_sequence = sorted(sequences, key=lambda x: x[1])[-1:]

    return longest_sequence[0][0] * longest_sequence[0][1]

def truncate(str, number):
    return str[:number - 3] + "..."

def capitalize_words(str):
    str = str.split(" ")
    capitalized_words = ''

    for index, word in enumerate(str):
        if index + 1 != len(str):
            capitalized_words = capitalized_words + word.capitalize() + ' '
        else:
            capitalized_words = capitalized_words + word.capitalize()

    return capitalized_words
