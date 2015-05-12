#Lu Lu and Dichen Li

def is_valid_word(word):
    """Check if the string word is not longer than 13 characters and is all
    lower letters"""
    #Check if the word is 0 length? such as ""
    if len(word) > 13:
        return False
    for e in word:
        if ord(e) < ord("a") or ord(e) > ord("z"):
            return False
    return True
    
def append_some_letters(s, num):
    """Assume s is a string and num is an int. Append num numbers of letters
    from the end of alphabet to s. return the new string"""
    #What if num > 26?
    num = num - 1
    while num >= 0:
        s += chr(ord("z") - num)
        num -= 1
    return s

def append_alphabet(s):
    """Append 26 letters of the alphabet to a string s. Return the new string"""
    for i in range(26):
        s += chr(ord('a') + i)
    return s

def remove_duplicate(s):
    """Remove the duplicate letters from string s and return the new string"""
    i = 0
    while i < len(s):
        char = s[i]
        while s.find(char, i + 1) != -1:
            s = s[:i + 1] + s[i + 1:].replace(char, '')
        i += 1
    return s

def generate_cipher_dic(s):
    """Return a cipher dictionary by mapping each letter in the alphabet to
    each letter in string s"""
    cipher_dic = {}
    for i in range(26):
        cipher_dic[chr(ord('a') + i)] = s[i]
    return cipher_dic

def generate_decipher_dic(dic):
    """Return a reversed dictionary from a dictionary dic"""
    decipher_dic = {}
    for e in dic:
        decipher_dic[dic[e]] = e
    return decipher_dic

def secret_word_to_dic(secret_word):
    """return the cipher dictionary from a secret_word"""
    s = append_some_letters(secret_word, len(secret_word))
    s = append_alphabet(s)
    s = remove_duplicate(s)
    return generate_cipher_dic(s)

def to_lower(char):
    """Assume char is a capital letter, return its lower case"""
    return chr(ord(char) + ord("a") - ord("A"))

def to_uper(char):
    """Assume char is a lower letter, return its uper case"""
    #change name to to_upper?
    return chr(ord(char) - ord("a") + ord("A"))

def is_capital(char):
    """check if a char is a capital letter or not"""
    return ord(char) >= ord("A") and ord(char) <= ord("Z")


def encipher(secret_word, plaintext_message):
    """Return the enciphered text from plaintext_message according to the
    secret_word"""
    cipher_dic = secret_word_to_dic(secret_word)
    ciphered_text = ""
    for char in plaintext_message:
        x = char
        if is_capital(char):
            char = to_lower(char)
        new_char = cipher_dic.get(char, char)
        if is_capital(x):
            new_char = to_uper(new_char)
        ciphered_text += new_char
    return ciphered_text

def decipher(secret_word, enciphered_message):
    """Return the deciphered text from enciphered_message according to the
    secret_word"""
    cipher_dic = secret_word_to_dic(secret_word)
    decipher_dic = generate_decipher_dic(cipher_dic)
    deciphered_text = ""
    for char in enciphered_message:
        x = char
        if is_capital(char):
            char = to_lower(char)
        new_char = decipher_dic.get(char, char)
        if is_capital(x):
            new_char = to_uper(new_char)
        deciphered_text += new_char
    return deciphered_text
        
def main():
    prompt = "Please choose to encipher or decipher: "
    encipher_or_decipher = raw_input(prompt)
    while encipher_or_decipher not in ("encipher", "decipher"):
        encipher_or_decipher = raw_input(prompt)

    prompt = "Please select a secret word: "
    secret_word = raw_input(prompt)
    while not is_valid_word(secret_word):
        secret_word = raw_input(prompt)

    message = raw_input("Please type in your message: ")
    if encipher_or_decipher == "encipher":
        print "After encipherring, your message:", "\n", message, "\n", \
              "becomes: ", "\n", encipher(secret_word, message)
    else:
        print "After decipherring, your message:", "\n", message, "\n", \
              "becomes: ", "\n", decipher(secret_word, message)
    return
    
if __name__ == "__main__":
    main()
    
    
