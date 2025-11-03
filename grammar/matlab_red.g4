grammar matlab_min;

// ======== PROGRAMA PRINCIPAL ========
file_
    : statement_list? EOF
    ;

// ======== LISTA DE COMANDOS ========
statement_list
    : statement
    | statement_list statement
    ;

// ======== COMANDOS ========
statement
    : assignment_statement
    | io_statement
    | selection_statement
    | iteration_statement
    ;

// ======== ATRIBUIÇÃO ========
assignment_statement
    : IDENTIFIER '=' expression eostmt
    ;

// ======== ENTRADA / SAÍDA ========
io_statement
    : INPUT '(' IDENTIFIER ')' eostmt
    | DISP '(' expression ')' eostmt
    ;

// ======== CONDICIONAL ========
selection_statement
    : IF expression statement_list (ELSE statement_list)? END eostmt
    ;

// ======== REPETIÇÃO ========
iteration_statement
    : WHILE expression statement_list END eostmt
    ;

// ======== EXPRESSÕES ========
expression
    : logical_or_expression
    ;

logical_or_expression
    : logical_and_expression
    | logical_or_expression '||' logical_and_expression
    ;

logical_and_expression
    : equality_expression
    | logical_and_expression '&&' equality_expression
    ;

equality_expression
    : relational_expression
    | equality_expression '==' relational_expression
    | equality_expression '!=' relational_expression
    ;

relational_expression
    : additive_expression
    | relational_expression '<' additive_expression
    | relational_expression '>' additive_expression
    | relational_expression '<=' additive_expression
    | relational_expression '>=' additive_expression
    ;

additive_expression
    : multiplicative_expression
    | additive_expression '+' multiplicative_expression
    | additive_expression '-' multiplicative_expression
    ;

multiplicative_expression
    : unary_expression
    | multiplicative_expression '*' unary_expression
    | multiplicative_expression '/' unary_expression
    ;

unary_expression
    : primary_expression
    | '!' primary_expression
    | '+' primary_expression
    | '-' primary_expression
    ;

primary_expression
    : IDENTIFIER
    | CONSTANT
    | STRING_LITERAL
    | '(' expression ')'
    ;

// ======== FIM DE INSTRUÇÃO ========
eostmt
    : ';'
    | CR
    ;

// ======== TOKENS ========
INPUT       : 'input';
DISP        : 'disp';
IF          : 'if';
ELSE        : 'else';
WHILE       : 'while';
END         : 'end';

IDENTIFIER  : [a-zA-Z] [a-zA-Z0-9_]*;
CONSTANT    : NUMBER;
STRING_LITERAL : '"' (~["\r\n])* '"';

fragment NUMBER : [0-9]+ ('.' [0-9]+)?;
CR          : [\r\n]+;
WS          : [ \t]+ -> skip;
COMMENT     : '%' ~[\r\n]* -> skip;
