import unittest
from project.services.weird_words import WeirdText


class TestWeirdEncoder(unittest.TestCase):

    def test_native_encoding(self):
        w = WeirdText()
        sentence = "Lorem ipsum (dolor) sit ameeeeeet, consectetur adipiscing elit."
        encoded = w.encode_sentence(sentence)
        decoded = w.decode_sentence(encoded)
        self.assertEqual(sentence, decoded)
        self.assertNotEqual(sentence, encoded)

    def test_list_based_decoding(self):
        w = WeirdText()
        sentence = "Lorem ipsum (dolor)"
        encoded = w.encode_sentence(sentence)
        print(encoded)
        decoded = w.decode_based_on_list(encoded, ['Lorem', 'ipsum', 'dolor'])
        self.assertEqual(sentence, decoded)