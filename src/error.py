from antlr4.error.ErrorListener import ErrorListener

class LexicalError(Exception):
    pass

class SyntacticError(Exception):
    pass

class RaisingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        name = recognizer.__class__.__name__
        if name.endswith("Lexer"):
            raise LexicalError(f"ERRO LÉXICO [linha {line}, col {column}]: {msg}")
        else:
            tok = offendingSymbol.text if offendingSymbol else "?"
            raise SyntacticError(f"ERRO SINTÁTICO [linha {line}, col {column}] token='{tok}': {msg}")
