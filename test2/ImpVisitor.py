# Generated from C:/Users/pauli/Documents/uni/6_sem/pvsus/md03/md03_1/IMP_D_TO_AM\Imp.g4 by ANTLR 4.9.2
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ImpParser.

class ImpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ImpParser#progr.
    def visitProgr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#series.
    def visitSeries(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#stmt.
    def visitStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#assign_stmt.
    def visitAssign_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#cond_stmt.
    def visitCond_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#loop.
    def visitLoop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#logical_expr.
    def visitLogical_expr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#logical_term.
    def visitLogical_term(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#logical_neg_elem.
    def visitLogical_neg_elem(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#logical_elem.
    def visitLogical_elem(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#compar.
    def visitCompar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#term.
    def visitTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ImpParser#elem.
    def visitElem(self, ctx):
        return self.visitChildren(ctx)


