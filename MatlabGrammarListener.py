# Generated from MatlabGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MatlabGrammarParser import MatlabGrammarParser
else:
    from MatlabGrammarParser import MatlabGrammarParser

# This class defines a complete listener for a parse tree produced by MatlabGrammarParser.
class MatlabGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MatlabGrammarParser#file_.
    def enterFile_(self, ctx:MatlabGrammarParser.File_Context):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#file_.
    def exitFile_(self, ctx:MatlabGrammarParser.File_Context):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#primary_expression.
    def enterPrimary_expression(self, ctx:MatlabGrammarParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#primary_expression.
    def exitPrimary_expression(self, ctx:MatlabGrammarParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#postfix_expression.
    def enterPostfix_expression(self, ctx:MatlabGrammarParser.Postfix_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#postfix_expression.
    def exitPostfix_expression(self, ctx:MatlabGrammarParser.Postfix_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#index_expression.
    def enterIndex_expression(self, ctx:MatlabGrammarParser.Index_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#index_expression.
    def exitIndex_expression(self, ctx:MatlabGrammarParser.Index_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#index_expression_list.
    def enterIndex_expression_list(self, ctx:MatlabGrammarParser.Index_expression_listContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#index_expression_list.
    def exitIndex_expression_list(self, ctx:MatlabGrammarParser.Index_expression_listContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#array_expression.
    def enterArray_expression(self, ctx:MatlabGrammarParser.Array_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#array_expression.
    def exitArray_expression(self, ctx:MatlabGrammarParser.Array_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#unary_expression.
    def enterUnary_expression(self, ctx:MatlabGrammarParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#unary_expression.
    def exitUnary_expression(self, ctx:MatlabGrammarParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#unary_operator.
    def enterUnary_operator(self, ctx:MatlabGrammarParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#unary_operator.
    def exitUnary_operator(self, ctx:MatlabGrammarParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:MatlabGrammarParser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:MatlabGrammarParser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#additive_expression.
    def enterAdditive_expression(self, ctx:MatlabGrammarParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#additive_expression.
    def exitAdditive_expression(self, ctx:MatlabGrammarParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#relational_expression.
    def enterRelational_expression(self, ctx:MatlabGrammarParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#relational_expression.
    def exitRelational_expression(self, ctx:MatlabGrammarParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#equality_expression.
    def enterEquality_expression(self, ctx:MatlabGrammarParser.Equality_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#equality_expression.
    def exitEquality_expression(self, ctx:MatlabGrammarParser.Equality_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#and_expression.
    def enterAnd_expression(self, ctx:MatlabGrammarParser.And_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#and_expression.
    def exitAnd_expression(self, ctx:MatlabGrammarParser.And_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#or_expression.
    def enterOr_expression(self, ctx:MatlabGrammarParser.Or_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#or_expression.
    def exitOr_expression(self, ctx:MatlabGrammarParser.Or_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#expression.
    def enterExpression(self, ctx:MatlabGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#expression.
    def exitExpression(self, ctx:MatlabGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#assignment_expression.
    def enterAssignment_expression(self, ctx:MatlabGrammarParser.Assignment_expressionContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#assignment_expression.
    def exitAssignment_expression(self, ctx:MatlabGrammarParser.Assignment_expressionContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#eostmt.
    def enterEostmt(self, ctx:MatlabGrammarParser.EostmtContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#eostmt.
    def exitEostmt(self, ctx:MatlabGrammarParser.EostmtContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#statement.
    def enterStatement(self, ctx:MatlabGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#statement.
    def exitStatement(self, ctx:MatlabGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#statement_list.
    def enterStatement_list(self, ctx:MatlabGrammarParser.Statement_listContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#statement_list.
    def exitStatement_list(self, ctx:MatlabGrammarParser.Statement_listContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#identifier_list.
    def enterIdentifier_list(self, ctx:MatlabGrammarParser.Identifier_listContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#identifier_list.
    def exitIdentifier_list(self, ctx:MatlabGrammarParser.Identifier_listContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#global_statement.
    def enterGlobal_statement(self, ctx:MatlabGrammarParser.Global_statementContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#global_statement.
    def exitGlobal_statement(self, ctx:MatlabGrammarParser.Global_statementContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#clear_statement.
    def enterClear_statement(self, ctx:MatlabGrammarParser.Clear_statementContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#clear_statement.
    def exitClear_statement(self, ctx:MatlabGrammarParser.Clear_statementContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#expression_statement.
    def enterExpression_statement(self, ctx:MatlabGrammarParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#expression_statement.
    def exitExpression_statement(self, ctx:MatlabGrammarParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#assignment_statement.
    def enterAssignment_statement(self, ctx:MatlabGrammarParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#assignment_statement.
    def exitAssignment_statement(self, ctx:MatlabGrammarParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#array_element.
    def enterArray_element(self, ctx:MatlabGrammarParser.Array_elementContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#array_element.
    def exitArray_element(self, ctx:MatlabGrammarParser.Array_elementContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#array_list.
    def enterArray_list(self, ctx:MatlabGrammarParser.Array_listContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#array_list.
    def exitArray_list(self, ctx:MatlabGrammarParser.Array_listContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#selection_statement.
    def enterSelection_statement(self, ctx:MatlabGrammarParser.Selection_statementContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#selection_statement.
    def exitSelection_statement(self, ctx:MatlabGrammarParser.Selection_statementContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#elseif_clause.
    def enterElseif_clause(self, ctx:MatlabGrammarParser.Elseif_clauseContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#elseif_clause.
    def exitElseif_clause(self, ctx:MatlabGrammarParser.Elseif_clauseContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#iteration_statement.
    def enterIteration_statement(self, ctx:MatlabGrammarParser.Iteration_statementContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#iteration_statement.
    def exitIteration_statement(self, ctx:MatlabGrammarParser.Iteration_statementContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#jump_statement.
    def enterJump_statement(self, ctx:MatlabGrammarParser.Jump_statementContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#jump_statement.
    def exitJump_statement(self, ctx:MatlabGrammarParser.Jump_statementContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#translation_unit.
    def enterTranslation_unit(self, ctx:MatlabGrammarParser.Translation_unitContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#translation_unit.
    def exitTranslation_unit(self, ctx:MatlabGrammarParser.Translation_unitContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#func_ident_list.
    def enterFunc_ident_list(self, ctx:MatlabGrammarParser.Func_ident_listContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#func_ident_list.
    def exitFunc_ident_list(self, ctx:MatlabGrammarParser.Func_ident_listContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#func_return_list.
    def enterFunc_return_list(self, ctx:MatlabGrammarParser.Func_return_listContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#func_return_list.
    def exitFunc_return_list(self, ctx:MatlabGrammarParser.Func_return_listContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#function_declare_lhs.
    def enterFunction_declare_lhs(self, ctx:MatlabGrammarParser.Function_declare_lhsContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#function_declare_lhs.
    def exitFunction_declare_lhs(self, ctx:MatlabGrammarParser.Function_declare_lhsContext):
        pass


    # Enter a parse tree produced by MatlabGrammarParser#function_declare.
    def enterFunction_declare(self, ctx:MatlabGrammarParser.Function_declareContext):
        pass

    # Exit a parse tree produced by MatlabGrammarParser#function_declare.
    def exitFunction_declare(self, ctx:MatlabGrammarParser.Function_declareContext):
        pass



del MatlabGrammarParser