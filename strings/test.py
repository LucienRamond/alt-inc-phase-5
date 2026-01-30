from strings import str_len, name_greetings, ends_with_exclamation, reverse_words, letter_occurences, str_to_camel_case, get_vowels_from_str, alternate_upper_lower, remove_duplicates, get_initials, mask_string, is_palindrome, longest_sequence, truncate, capitalize_words

def test_str_len():
    assert str_len("Bonjour le monde !") == "15 caractères"
    assert str_len("B ") == "1 caractère"

def test_name_greeting():
    assert name_greetings("jean-pierre") == "Bonjour Jean-Pierre"
    assert name_greetings("jean-pierre-castaldi") == "Bonjour Jean-Pierre-Castaldi"

def test_ends_with_exclamation():
    assert ends_with_exclamation("Je suis très satisfait !") == True
    assert ends_with_exclamation("Je ne suis pas satisfait :(") == False

def test_reverse_words():
    assert reverse_words('Je mange une pomme') == "pomme une mange Je"

def test_letter_occurences():
    sentence = "Je mange une pomme"
    assert letter_occurences(sentence, "e") == 4
    assert letter_occurences(sentence, "E") == 4

def test_str_to_camel_case():
    assert str_to_camel_case("user_first_name") == "userFirstName"

def test_get_vowels_from_str():
    assert get_vowels_from_str("Maël et anaïs élèvent la côte !") == 12

def test_alternater_upper_lower():
    assert alternate_upper_lower("motdepassedelamortquitue") == "MoTdEpAsSeDeLaMoRtQuItUe"

def test_remove_duplicates():
    assert remove_duplicates("Bonjouuuur !!! J'ai besoiiiin d'aide....") == "Bonjour ! J'ai besoin d'aide."

def test_get_initials():
    assert get_initials("michelle rodriguez") == "MR"
    assert get_initials("patrick poivre d harvor") == "PPDH"

def test_mask_string():
    assert mask_string('1234567890123456', 4 ) == "3456"
    assert mask_string('1234567890123456', 8 ) == "90123456"

def test_is_palindrome():
    assert is_palindrome("Eh ! ça va la vache ?") == True

def test_longest_sequence():
    assert longest_sequence("aaabbbbbcccc") == "bbbbb"

def test_truncate():
    assert truncate("Ceci est une très longue description d'un produit", 20) == "Ceci est une très..."

def test_capitalize_words():
    assert capitalize_words("bienvenue sur notre site web") == "Bienvenue Sur Notre Site Web"

test_str_len()
test_name_greeting()
test_ends_with_exclamation()
test_reverse_words()
test_letter_occurences()
test_str_to_camel_case()
test_get_vowels_from_str()
test_alternater_upper_lower()
test_remove_duplicates()
test_get_initials()
test_mask_string()
test_is_palindrome()
test_longest_sequence()
test_truncate()
test_capitalize_words()