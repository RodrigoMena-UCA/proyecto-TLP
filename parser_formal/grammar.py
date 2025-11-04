"""
Gramática (no ambigua y factorizada) para LL(1):

Program   -> StmtList EOF
StmtList  -> Stmt StmtList | ε
Stmt      -> ID ASSIGN Expr SEMI
Expr      -> Term ExprP
ExprP     -> PLUS Term ExprP | MINUS Term ExprP | ε
Term      -> Factor TermP
TermP     -> MUL Factor TermP | DIV Factor TermP | ε
Factor    -> LPAREN Expr RPAREN | ID | NUM
"""

NONTERMINALS = ["Program", "StmtList", "Stmt", "Expr", "ExprP", "Term", "TermP", "Factor"]
TERMINALS = ["ID","ASSIGN","NUM","PLUS","MINUS","MUL","DIV","LPAREN","RPAREN","SEMI","EOF"]
START = "Program"

# Reglas como dict: {A: [[...], [...]]}
GRAMMAR = {
    "Program": [["StmtList", "EOF"]],
    "StmtList": [["Stmt", "StmtList"], ["ε"]],
    "Stmt": [["ID", "ASSIGN", "Expr", "SEMI"]],
    "Expr": [["Term", "ExprP"]],
    "ExprP": [["PLUS", "Term", "ExprP"], ["MINUS", "Term", "ExprP"], ["ε"]],
    "Term": [["Factor", "TermP"]],
    "TermP": [["MUL", "Factor", "TermP"], ["DIV", "Factor", "TermP"], ["ε"]],
    "Factor": [["LPAREN", "Expr", "RPAREN"], ["ID"], ["NUM"]],
}
