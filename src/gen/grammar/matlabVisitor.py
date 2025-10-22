# Generated from ./grammar/matlab.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .matlabParser import matlabParser
else:
    from matlabParser import matlabParser

# This class defines a complete generic visitor for a parse tree produced by matlabParser.

class matlabVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by matlabParser#file_.
    def visitFile_(self, ctx:matlabParser.File_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#primary_expression.
    def visitPrimary_expression(self, ctx:matlabParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#postfix_expression.
    def visitPostfix_expression(self, ctx:matlabParser.Postfix_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#index_expression.
    def visitIndex_expression(self, ctx:matlabParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#index_expression_list.
    def visitIndex_expression_list(self, ctx:matlabParser.Index_expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#array_expression.
    def visitArray_expression(self, ctx:matlabParser.Array_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#unary_expression.
    def visitUnary_expression(self, ctx:matlabParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#unary_operator.
    def visitUnary_operator(self, ctx:matlabParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:matlabParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#additive_expression.
    def visitAdditive_expression(self, ctx:matlabParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#relational_expression.
    def visitRelational_expression(self, ctx:matlabParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#equality_expression.
    def visitEquality_expression(self, ctx:matlabParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#and_expression.
    def visitAnd_expression(self, ctx:matlabParser.And_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#or_expression.
    def visitOr_expression(self, ctx:matlabParser.Or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expression.
    def visitExpression(self, ctx:matlabParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#assignment_expression.
    def visitAssignment_expression(self, ctx:matlabParser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#eostmt.
    def visitEostmt(self, ctx:matlabParser.EostmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#statement.
    def visitStatement(self, ctx:matlabParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#statement_list.
    def visitStatement_list(self, ctx:matlabParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#identifier_list.
    def visitIdentifier_list(self, ctx:matlabParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#global_statement.
    def visitGlobal_statement(self, ctx:matlabParser.Global_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#clear_statement.
    def visitClear_statement(self, ctx:matlabParser.Clear_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expression_statement.
    def visitExpression_statement(self, ctx:matlabParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#assignment_statement.
    def visitAssignment_statement(self, ctx:matlabParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#array_element.
    def visitArray_element(self, ctx:matlabParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#array_list.
    def visitArray_list(self, ctx:matlabParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#selection_statement.
    def visitSelection_statement(self, ctx:matlabParser.Selection_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#elseif_clause.
    def visitElseif_clause(self, ctx:matlabParser.Elseif_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#iteration_statement.
    def visitIteration_statement(self, ctx:matlabParser.Iteration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#jump_statement.
    def visitJump_statement(self, ctx:matlabParser.Jump_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#translation_unit.
    def visitTranslation_unit(self, ctx:matlabParser.Translation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#func_ident_list.
    def visitFunc_ident_list(self, ctx:matlabParser.Func_ident_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#func_return_list.
    def visitFunc_return_list(self, ctx:matlabParser.Func_return_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#function_declare_lhs.
    def visitFunction_declare_lhs(self, ctx:matlabParser.Function_declare_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#function_declare.
    def visitFunction_declare(self, ctx:matlabParser.Function_declareContext):
        return self.visitChildren(ctx)



del matlabParser