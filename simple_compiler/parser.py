from lexer import isOp, isNum

class PredictiveParser:
    """ Predictive parser for simple algebraic grammar. 
        Translates infix to postfix.
        Two nonterminals:
            expr
        """
    def __init__(self):
        self.output_buffer = ""
        self.current_token = None

    def advance_token(self):
        self.current_token = self.tokenstream.get_token()

    def match_production(self):
        """ Find production whose first output matches the current token, and whose LHS matches
        the current nonterminal"""
        if isOp(self.current_token):
            return 'apply_op'
        elif isNum(self.current_token):
            return 'eval_num'
        else:
            return 'empty'

    def emit(self, str):
        """ Emits a string into the translation"""
        self.output_buffer += str

    def num(self):
        """ Emit portion of translation corresponding to a num token"""
        if not isNum(self.current_token):
            raise ValueError(f"Unexpected token {self.current_token.lex}")
        self.emit('(' + str(self.current_token.val) + ')')
        self.advance_token()

    def expr(self):
        """ Emit translation for expression into output buffer."""
        self.num()
        self.rest()
    
    def rest(self):
        if self.current_token is None:
            # translation has finished
            return
        elif isOp(self.current_token):
            opstr = self.current_token.lex
            self.advance_token()
            self.num()
            self.emit(opstr)
            self.rest()
        else:
            raise SyntaxError(f"Unexpected token {self.current_token.lex}")

    def translate(self, tokenstream):
        """ Stores postfix translation of the token stream in output buffer."""
        self.output_buffer = ""
        self.tokenstream = tokenstream
        self.advance_token()
        self.expr()