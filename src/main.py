import os, sys
from antlr4 import FileStream, CommonTokenStream

from src.error import RaisingErrorListener, LexicalError, SyntacticError
from src.gen.grammar.matlabLexer import matlabLexer
from src.gen.grammar.matlabParser import matlabParser
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

    tree = parser.translation_unit()
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

    in_dir = os.path.dirname(os.path.abspath(src_path))
    out_dir = os.path.join(in_dir, "arvores")
    os.makedirs(out_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(src_path))[0]
    png_path = os.path.join(out_dir, f"{base_name}.tree.png")
    svg_path = os.path.join(out_dir, f"{base_name}.tree.svg")

    png_out = render_tree_png(tree, parser, png_path)
    print(f"OK: gerei {png_out}")
    try:
        svg_out = render_tree_svg(tree, parser, svg_path)
        print(f"OK: gerei {svg_out}")
    except Exception:
        pass

if __name__ == "__main__":
    main()
