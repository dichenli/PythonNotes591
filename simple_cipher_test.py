## Lu Lu and Dichen Li
import unittest
from simple_cipher import *



class TestSimpleCipher(unittest.TestCase):


    def test_is_valid_word(self):
        print"\ntest_is_valid_word"
        self.assertEqual(is_valid_word("abc"), True)
        self.assertEqual(is_valid_word("aBc"), False)
        self.assertEqual(is_valid_word("abcdefghijklm"), True)
        self.assertEqual(is_valid_word("abcdefghijklmn"), False)
        self.assertEqual(is_valid_word("a1c"), False)


    def test_append_some_letters(self):
        print"\ntest_append_some_letters"
        self.assertEqual(append_some_letters("RGH", 4), "RGHwxyz")
        self.assertEqual(append_some_letters("zzz", 0), "zzz")
        self.assertEqual(append_some_letters("", 1), "z")

    def test_append_alphabet(self):
        print"\ntest_append_alphabet"
        self.assertEqual(append_alphabet("1"), "1abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(append_alphabet(""), "abcdefghijklmnopqrstuvwxyz")


    def test_remove_duplicate(self):
        print"\ntest_remove_duplicate"
        self.assertEqual(remove_duplicate("aa"), "a")
        self.assertEqual(remove_duplicate("1122"), "12")
        self.assertEqual(remove_duplicate("abc"), "abc")
        self.assertEqual(remove_duplicate(""), "")

    def test_generate_cipher_dic(self):
        print"\ntest_generate_cipher_dic"
        self.assertEqual(generate_cipher_dic("qwertyuiopasdfghjklzxcvbnm"), {"a":"q", "b":"w", "c":"e", "d":"r", "e":"t", "f":"y", "g":"u", "h":"i", "i":"o", "j":"p", "k":"a", "l":"s", "m":"d", "n":"f", "o":"g", "p":"h", "q":"j", "r":"k", "s":"l", "t":"z", "u":"x", "v":"c", "w":"v", "x":"b", "y":"n", "z":"m"})


    def test_generate_decipher_dic(self):
        print"\ntest_generate_decipher_dic"
        self.assertEqual(generate_decipher_dic({"a":"q", "b":"w", "c":"e", "d":"r", "e":"t", "f":"y", "g":"u", "h":"i", "i":"o", "j":"p", "k":"a", "l":"s", "m":"d", "n":"f", "o":"g", "p":"h", "q":"j", "r":"k", "s":"l", "t":"z", "u":"x", "v":"c", "w":"v", "x":"b", "y":"n", "z":"m"}), {"q":"a", "w":"b", "e":"c", "r":"d", "t":"e", "y":"f", "u":"g", "i":"h", "o":"i", "p":"j", "a":"k", "s":"l", "d":"m", "f":"n", "g":"o", "h":"p", "j":"q", "k":"r", "l":"s", "z":"t", "x":"u", "c":"v", "v":"w", "b":"x", "n":"y", "m":"z"})



    def test_secret_word_to_dic(self):
        print"\ntest_secret_word_to_dic"
        self.assertEqual(secret_word_to_dic("a"), {'a': 'a', 'c': 'b', 'b': 'z', 'e': 'd', 'd': 'c', 'g': 'f', 'f': 'e', 'i': 'h', 'h': 'g', 'k': 'j', 'j': 'i', 'm': 'l', 'l': 'k', 'o': 'n', 'n': 'm', 'q': 'p', 'p': 'o', 's': 'r', 'r': 'q', 'u': 't', 't': 's', 'w': 'v', 'v': 'u', 'y': 'x', 'x': 'w', 'z': 'y'})
        self.assertEqual(secret_word_to_dic(""), {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z'})

    def test_to_lower(self):
        print"\ntest_to_lower"
        self.assertEqual(to_lower('A'), 'a')
        self.assertEqual(to_lower('Z'), 'z')



    def test_to_uper(self):
        print"\ntest_to_uper"
        self.assertEqual(to_uper('a'), 'A')
        self.assertEqual(to_uper('z'), 'Z')



    def test_is_capital(self):
        print"\ntest_is_capital"
        self.assertEqual(is_capital('A'), True)
        self.assertEqual(is_capital('a'), False)
        self.assertEqual(is_capital('\n'), False)
        self.assertEqual(is_capital('1'), False)

    def test_encipher(self):
        print"\ntest_encipher"
        self.assertEqual(encipher("a", "Good"), "Fnnc")
        self.assertEqual(encipher("", "Bad"), "Bad")



    def test_decipher(self):
        print"\ntest_decipher(self)"
        self.assertEqual(decipher("a", "Fnnc"), "Good")
        self.assertEqual(encipher("", "Good"), "Good")


unittest.main()
