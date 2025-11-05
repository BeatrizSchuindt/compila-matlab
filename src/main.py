import os, sys
from antlr4 import FileStream, CommonTokenStream

from src.error import RaisingErrorListener, LexicalError, SyntacticError

# parser/lexer gerados (saída em src/gen/grammar)
from src.gen.grammar.matlabLexer import matlabLexer
from src.gen.grammar.matlabParser import matlabParser

# novo: render direto em imagem (sem .dot feio)
from src.ast_graphviz import render_tree_png, render_tree_svg

def parse_file(path):
    input_stream = FileStream(path, encoding="utf-8")
    lexer = matlabLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = matlabParser(tokens)

    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    listener = RaisingErrorListener()
    lexer.addErrorListener(listener)
    parser.addErrorListener(listener)

    # regra inicial
    tree = parser.programa()
    return tree, parser

def main():
    if len(sys.argv) < 2:
        print("Uso:\n  python -m src.main caminho\\arquivo.m")
        sys.exit(64)

    src_path = sys.argv[1]
    try:
        tree, parser = parse_file(src_path)
    except LexicalError as e:
        print(e); sys.exit(65)
    except SyntacticError as e:
        print(e); sys.exit(66)

    base, _ = os.path.splitext(src_path)
    png_path = base + ".tree.png"
    svg_path = base + ".tree.svg"

    # Gera PNG e SVG (o PNG dá pra colar fácil no relatório)
    png_out = render_tree_png(tree, parser, png_path)
    print(f"OK: gerei {png_out}")
    try:
        svg_out = render_tree_svg(tree, parser, svg_path)
        print(f"OK: gerei {svg_out}")
    except Exception:
        pass

if __name__ == "__main__":
    main()
