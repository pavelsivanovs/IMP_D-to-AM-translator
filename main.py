from antlr4 import *
from test2.ImpLexer import ImpLexer
from test2.ImpParser import ImpParser
from ExtendedImpVisitor import ExtendedImpVisitor
from antlr4.tree.Trees import Trees
import nltk


def main(filename):
    input_stream = FileStream(filename)
    lexer = ImpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ImpParser(stream)
    tree = parser.progr()

    visitor = ExtendedImpVisitor()
    visitor.visit(tree)

    tree_string = Trees.toStringTree(tree, None, parser)
    tree = nltk.Tree.fromstring(tree_string)
    tree.draw()


if __name__ == '__main__':
    main('samples/LDK.txt')
