from test2.ImpParser import ImpParser
from test2.ImpVisitor import ImpVisitor
from antlr4 import *


# This class defines a complete generic visitor for a parse tree produced by ImpParser.


class ExtendedImpVisitor(ImpVisitor):
    # IMP_D translated code to AM commands
    translated_code = []

    # List of operators
    operators = {
        '+': 'ADD',
        '-': 'SUB',
        '*': 'MULT',
        '/': 'DIV',
        '<>': ['EQ', 'NEG'],
        '=<': 'LE',
        '>=': ['LE', 'NEG', 'EQ', 'OR'],
        '=': 'EQ',
        '<': ['EQ', 'NEG', 'LE', 'AND'],
        '>': ['LE', 'NEG'],
        'and': 'AND',
        'or': 'OR',
        'not': 'NEG'
    }

    # bool constants
    bools = ['TRUE', 'FALSE']

    def pushFetch(self, elem):
        elem = str(elem)

        if elem in self.bools:
            return elem

        return 'PUSH({})'.format(elem) if elem.isnumeric() \
            else 'FETCH({})'.format(elem)

    # translating expressions into AM commands
    def expression(self, elem_0, elem_1, relation):
        if relation in ['>=', '<']:
            return ' : '.join([
                elem_1,
                elem_0,
                self.operators[relation][0],
                self.operators[relation][1],
                elem_1,
                elem_0,
                self.operators[relation][2],
                self.operators[relation][3]
            ])

        if relation in ['<>', '>']:
            return ' : '.join([
                elem_1, elem_0,
                self.operators[relation][0], self.operators[relation][1]
            ])

        return ' : '.join([
            elem_1, elem_0, self.operators[relation]
        ])

    # Visit a parse tree produced by ImpParser#progr.
    def visitProgr(self, ctx: ImpParser.ProgrContext):
        # at the end of walking the parsed tree we will have a ready array of AM commands
        self.visitChildren(ctx)
        print(self.translated_code)

    # Visit a parse tree produced by ImpParser#series.
    def visitSeries(self, ctx: ImpParser.SeriesContext):
        return_value = self.visit(ctx.getChild(0))

        for i in range(2, ctx.getChildCount(), 2):
            return_value + ' : ' + self.visit(ctx.getChild(i))

        self.translated_code = return_value
        return return_value

    # Visit a parse tree produced by ImpParser#stmt.
    def visitStmt(self, ctx: ImpParser.StmtContext):
        # for SKIP_STMT
        if isinstance(ctx.getChild(0), TerminalNode):
            return 'NOOP'

        return self.visitChildren(ctx)

    # Visit a parse tree produced by ImpParser#assign_stmt.
    def visitAssign_stmt(self, ctx: ImpParser.Assign_stmtContext):
        return '{} : STORE({})'.format(
            self.visit(ctx.getChild(2)),
            str(ctx.getChild(0))
        )

    # Visit a parse tree produced by ImpParser#cond_stmt.
    def visitCond_stmt(self, ctx: ImpParser.Cond_stmtContext):
        return '{} : BRANCH({}, {})'.format(
            self.visit(ctx.getChild(1)),
            self.visit(ctx.getChild(3)),
            self.visit(ctx.getChild(5))
        )

    # Visit a parse tree produced by ImpParser#loop.
    def visitLoop(self, ctx: ImpParser.LoopContext):
        el1 = self.visit(ctx.getChild(1))
        el3 = self.visit(ctx.getChild(3))

        return 'LOOP({}, {})'.format(
            el1,
            el3
        )

    # Visit a parse tree produced by ImpParser#logical_expr.
    def visitLogical_expr(self, ctx: ImpParser.Logical_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        return '{} : {} : {}'.format(
            self.visit(ctx.getChild(2)),
            self.visit(ctx.getChild(0)),
            self.operators[str(ctx.getChild(1))]
        )

    # Visit a parse tree produced by ImpParser#logical_term.
    def visitLogical_term(self, ctx: ImpParser.Logical_termContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        return '{} : {} : {}'.format(
            self.visit(ctx.getChild(2)),
            self.visit(ctx.getChild(0)),
            self.operators[str(ctx.getChild(1))]
        )

    # Visit a parse tree produced by ImpParser#logical_neg_elem.
    def visitLogical_neg_elem(self, ctx: ImpParser.Logical_neg_elemContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        return '{} : {}'.format(
            self.visit(ctx.getChild(1)),
            self.operators[str(ctx.getChild(0))]
        )

    # Visit a parse tree produced by ImpParser#logical_elem.
    def visitLogical_elem(self, ctx: ImpParser.Logical_elemContext):
        # another logical expression in parentheses
        if ctx.getChildCount() != 1:
            return '{}'.format(self.visit(ctx.getChild(1)))

        if ctx.compar():
            return self.visitChildren(ctx)

        return self.pushFetch(ctx.getChild(0))

    # Visit a parse tree produced by ImpParser#compar.
    def visitCompar(self, ctx: ImpParser.ComparContext):
        elem_0 = self.visit(ctx.getChild(0))
        elem_1 = self.visit(ctx.getChild(2))
        relation = str(ctx.RELATION())

        return self.expression(elem_0, elem_1, relation)

    # Visit a parse tree produced by ImpParser#expr.
    def visitExpr(self, ctx: ImpParser.ExprContext):
        translation = self.visit(ctx.getChild(0))

        for i in range(1, ctx.getChildCount(), 2):
            translation += ' : {} : {}'.format(
                self.visit(ctx.getChild(i + 1)),
                self.operators[str(ctx.getChild(i))]
            )

        return translation

    # Visit a parse tree produced by ImpParser#term.
    def visitTerm(self, ctx: ImpParser.TermContext):
        translation = self.visit(ctx.getChild(0))

        for i in range(1, ctx.getChildCount(), 2):
            translation += ' : {} : {}'.format(
                self.visit(ctx.getChild(i)),
                self.operators[str(ctx.getChild(i + 1))]
            )

        return translation

    # Visit a parse tree produced by ImpParser#elem.
    def visitElem(self, ctx: ImpParser.ElemContext):
        if ctx.getChildCount() != 1:
            return '({})'.format(self.visit(ctx.getChild(1)))

        return self.pushFetch(ctx.getChild(0))
