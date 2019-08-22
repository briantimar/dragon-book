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
        if self.is_empty():
            return chars
        while True:
            try:
                char = self.getchar()
                if iswhitespace(char):
                    continue
                elif isop(char):
                    return char
                elif isdigit(char):
                    chars += char
                    while isdigit(self.peek_char()):
                        chars += self.getchar()
                    return chars
                else:
                    raise SyntaxError(f"Unexpected character: {char}")

            except EOFError:
                return ''

    def get_all_lexemes(self):
        ls = []
        while not self.is_empty():
            ls.append(self.get_lexeme())
        return ls