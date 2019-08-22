""" Lexical analyzer. Provides a token stream to the syntactic analyzer
    Types of token: 
        num, operator, identifier
    """
import re
OPS = ['+', '-']

def isop(char):
    """ Checks whether character determines a valid operation"""
    return char in OPS

def isdigit(char):
    """ Check whether character represents a digit """
    if re.match(r"[0-9]", char):
        return True
    return False

def iswhitespace(char):
    """ Matches whitespace chars"""
    if re.match(r"\s", char):
        return True
    return False

class Token:
    pass

class Op(Token):
    def __init__(self, lex):
        self.lex = lex

class Num(Token):
    def __init__(self, lex):
        self.lex = lex
        self.val = int(lex)

def isNum(token):
    return isinstance(token, Num)
def isOp(token):
    return isinstance(token, Op)

class TokenStream:
    """Given source input string, provides tokens on demand."""

    def __init__(self, source):
        """ Source: string holding the source code"""
        self.source = source
        self.indx = 0

    def getchar(self):
        """Returns next char from the source, or EOFError when the source is exhausted
        """
        if self.indx < len(self.source):
            c = self.source[self.indx]
            self.indx += 1
            return c
        else:
            raise EOFError
    
    def peek_char(self):
        if self.indx < len(self.source):
            return self.source[self.indx]
        return ''
    
    def is_empty(self):
        return self.indx >= len(self.source)

    def get_lexeme(self):
        """Returns string representation of next token.
            Returns empty string when source is exhausted.
        """
        chars = ''
        typ = None

        if self.is_empty():
            return chars, typ
        while True:
            try:
                char = self.getchar()
                if iswhitespace(char):
                    continue
                elif isop(char):
                    typ = 'op'
                    return char, typ
                elif isdigit(char):
                    typ = 'num'
                    chars += char
                    while isdigit(self.peek_char()):
                        chars += self.getchar()
                    return chars, typ
                else:
                    raise SyntaxError(f"Unexpected character: {char}")

            except EOFError:
                return '', typ

    def get_token(self):
        """Returns next token, or None if source is exhausted."""
        lex, typ = self.get_lexeme()
        if typ == 'op':
            return Op(lex)
        elif typ == 'num':
            return Num(lex)
        elif typ is None:
            return None
        else:
            raise ValueError(f"Invalid token type {typ}")

    def get_all_lexemes(self):
        ls = []
        while not self.is_empty():
            ls.append(self.get_lexeme()[0])
        return ls

    def get_all_tokens(self):
        toks = []
        while not self.is_empty():
            toks.append(self.get_token())
        return toks