from antlr4.error.ErrorListener import ErrorListener

class LexicalError(Exception):
    pass

class SyntacticError(Exception):
    pass

class RaisingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Se o recognizer é o *Lexer*, tratamos como erro léxico.
        # Em Python, o nome da classe gerada termina com "Lexer"/"Parser".
        name = recognizer.__class__.__name__
        if name.endswith("Lexer"):
            # offendingSymbol costuma vir None em erros léxicos; a mensagem (msg) já descreve o problema.
            raise LexicalError(f"ERRO LÉXICO [linha {line}, col {column}]: {msg}")
        else:
            tok = offendingSymbol.text if offendingSymbol else "?"
            raise SyntacticError(f"ERRO SINTÁTICO [linha {line}, col {column}] token='{tok}': {msg}")
