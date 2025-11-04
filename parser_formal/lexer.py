from .tokens import Token, TokenType

_WHITESPACE = set(" \t\r\n")
_LETTERS = set("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ_")
_DIGITS = set("0123456789")

def _is_letter(ch: str) -> bool:
    return ch in _LETTERS

def _is_digit(ch: str) -> bool:
    return ch in _DIGITS

def lex(src: str):
    i = 0
    n = len(src)
    tokens = []

    while i < n:
        ch = src[i]

        if ch in _WHITESPACE:
            i += 1
            continue

        if _is_letter(ch):
            start = i
            i += 1
            while i < n and ( _is_letter(src[i]) or _is_digit(src[i]) ):
                i += 1
            lexeme = src[start:i]
            tokens.append(Token("ID", lexeme, start))
            continue

        if _is_digit(ch):
            start = i
            i += 1
            while i < n and _is_digit(src[i]):
                i += 1
            lexeme = src[start:i]
            tokens.append(Token("NUM", lexeme, start))
            continue

        if ch == '+':
            tokens.append(Token("PLUS", ch, i)); i+=1; continue
        if ch == '-':
            tokens.append(Token("MINUS", ch, i)); i+=1; continue
        if ch == '*':
            tokens.append(Token("MUL", ch, i)); i+=1; continue
        if ch == '/':
            tokens.append(Token("DIV", ch, i)); i+=1; continue
        if ch == '(':
            tokens.append(Token("LPAREN", ch, i)); i+=1; continue
        if ch == ')':
            tokens.append(Token("RPAREN", ch, i)); i+=1; continue
        if ch == '=':
            tokens.append(Token("ASSIGN", ch, i)); i+=1; continue
        if ch == ';':
            tokens.append(Token("SEMI", ch, i)); i+=1; continue

        raise SyntaxError(f"Caracter inesperado '{ch}' en posición {i}")

    tokens.append(Token("EOF", "", n))
    return tokens
