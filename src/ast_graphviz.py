import os, html
from antlr4.tree.Tree import TerminalNode
from graphviz import Digraph

def _node_id(obj) -> str:
    return f"n{id(obj)}"

def render_tree_png(tree, parser, out_path_png: str) -> str:
    """
    Renderiza a parse tree em PNG. Retorna o caminho final do PNG.
    Requer: pacote Python 'graphviz' e o Graphviz instalado no sistema.
    """
    # Configuração visual
    dot = Digraph(
        "ParseTree",
        node_attr={
            "shape": "box",
            "fontname": "Consolas",
            "fontsize": "10",
            "style": "rounded,filled",
        },
        edge_attr={"arrowsize": "0.6"},
        graph_attr={
            "ranksep": "0.3",
            "nodesep": "0.25",
            "labelloc": "t",
        },
    )

    def add(node):
        nid = _node_id(node)
        if isinstance(node, TerminalNode):
            text = node.getText()
            label = f"'{html.escape(text)}'"
            dot.node(nid, label, fillcolor="#eaf5ff")  # tokens = azul clarinho
        else:
            rule = parser.ruleNames[node.getRuleIndex()]
            dot.node(nid, rule, fillcolor="#f6f6f6")    # regras = cinza claro

        for i in range(node.getChildCount()):
            ch = node.getChild(i)
            dot.edge(nid, _node_id(ch))
            add(ch)

    add(tree)

    # Gera PNG
    base, _ = os.path.splitext(out_path_png)
    dot.format = "png"
    out = dot.render(filename=base, cleanup=True)  # apaga .gv temporário
    return out  # caminho final do .png

def render_tree_svg(tree, parser, out_path_svg: str) -> str:
    base, _ = os.path.splitext(out_path_svg)
    # Reusa a lógica do PNG trocando formato:
    import os, html
    from antlr4.tree.Tree import TerminalNode
    from graphviz import Digraph

    dot = Digraph(
        "ParseTree",
        node_attr={"shape":"box","fontname":"Consolas","fontsize":"10","style":"rounded,filled"},
        edge_attr={"arrowsize":"0.6"},
        graph_attr={"ranksep":"0.3","nodesep":"0.25","labelloc":"t"},
    )

    def add(node):
        nid = f"n{id(node)}"
        if isinstance(node, TerminalNode):
            label = f"'{html.escape(node.getText())}'"
            dot.node(nid, label, fillcolor="#eaf5ff")
        else:
            rule = parser.ruleNames[node.getRuleIndex()]
            dot.node(nid, rule, fillcolor="#f6f6f6")
        for i in range(node.getChildCount()):
            ch = node.getChild(i)
            dot.edge(nid, f"n{id(ch)}")
            add(ch)

    add(tree)
    dot.format = "svg"
    out = dot.render(filename=base, cleanup=True)
    return out
