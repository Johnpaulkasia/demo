import unittest

def encode(text, alphabet):
    return list(
        map(
            lambda char: alphabet.find(char),
            text
        )
    )

def decode(encoded_text, alphabet):
    return ''.join(
        map(
            lambda n: alphabet[n],
            encoded_text
        )
    )

def vigenere_encrypt(text, key, alphabet):
    table = [alphabet[i:] + alphabet[:i] for i in range(len(alphabet))]
    encoded_text = encode(text, alphabet)
    encoded_key = encode(key, alphabet)
    encrypted_text = []
    for i in range(len(encoded_text)):
        encrypted_letter = (encoded_text[i] + encoded_key[i % len(key)]) % len(alphabet)
        encrypted_text.append(encrypted_letter)
    return decode(encrypted_text, alphabet)

def vigenere_decrypt(cipher, key, alphabet):
    table = [alphabet[i:] + alphabet[:i] for i in range(len(alphabet))]
    encoded_cipher = encode(cipher, alphabet)
    encoded_key = encode(key, alphabet)
    decrypted_text = []
    for i in range(len(encoded_cipher)):
        decrypted_letter = (encoded_cipher[i] - encoded_key[i % len(key)]) % len(alphabet)
        decrypted_text.append(decrypted_letter)
    return decode(decrypted_text, alphabet)

class Vigenere_test(unittest.TestCase):
    def __init__(self, *args, **kw_args):
        super(Vigenere_test, self).__init__(*args, **kw_args)

        self.alphabet = 'abcdefghijklmnopqrstuvwxyz, '
        self.text = 'egy aprocska kalapocska, benne csacska macska mocska'
        self.key = 'lusta dick'
        self.key2 = 'grabowsky'
        self.cipher = 'p,osaouweavurbakdxqmbcsr ahvpokwitcrnibwlwiba,pweavu'
    
    def test_encrypt(self):
        self.assertEqual(vigenere_encrypt(self.text, self.key, self.alphabet), self.cipher)
        self.assertNotEqual(vigenere_encrypt(self.text, self.key2, self.alphabet), self.cipher)

    def test_decrypt(self):
        self.assertEqual(vigenere_decrypt(self.cipher, self.key, self.alphabet), self.text)
        self.assertNotEqual(vigenere_decrypt(self.cipher, self.key2, self.alphabet), self.text)

    def test_end2end(self):
        self.assertEqual(vigenere_decrypt(vigenere_encrypt(self.text, self.key, self.alphabet), self.key, self.alphabet), self.text)

if __name__ == '__main__':
    unittest.main()
