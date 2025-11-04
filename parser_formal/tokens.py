from dataclasses import dataclass
from typing import Literal

TokenType = Literal[
    "ID", "NUM",
    "PLUS", "MINUS", "MUL", "DIV",
    "LPAREN", "RPAREN",
    "ASSIGN", "SEMI",
    "EOF"
]

@dataclass
class Token:
    type: TokenType
    lexeme: str
    pos: int  # índice en la cadena de entrada, para errores
