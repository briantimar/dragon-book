import unittest

class TestLexer(unittest.TestCase):

    def test_isdigit(self):
        from lexer import isdigit
        for i in range(0, 10):
            self.assertTrue(isdigit(str(i)))
        self.assertFalse(isdigit('a'))
        self.assertFalse(isdigit('+'))

    def test_iswhitespace(self):
        from lexer import iswhitespace
        self.assertTrue(iswhitespace(' '))
        self.assertTrue(iswhitespace('\t'))
        self.assertTrue(iswhitespace('\n'))

    def test_get_lexeme(self):
        from lexer import TokenStream
        source = "23+4"
        ts = TokenStream(source)
        self.assertEqual(ts.get_all_lexemes(), ["23","+", "4"])

        source = "4 - 32   +5"
        ts = TokenStream(source)
        self.assertEqual(ts.get_all_lexemes(), ["4", "-", "32", "+", "5"])

        source = "4 + a"
        ts = TokenStream(source)
        with self.assertRaises(SyntaxError):
            ts.get_all_lexemes()
        
    def test_get_token(self):
        from lexer import TokenStream
        source = "23+4-2"
        lexes = ["23", "+", "4", "-", "2"]
        vals = [23, None, 4, None, 2]
        ts = TokenStream(source)
        toks = ts.get_all_tokens()
        for i in range(len(toks)):
            self.assertEqual(toks[i].lex, lexes[i])
            if vals[i] is not None:
                self.assertEqual(toks[i].val, vals[i])


if __name__ == "__main__":
    unittest.main()