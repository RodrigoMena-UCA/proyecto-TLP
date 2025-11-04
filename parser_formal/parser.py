from typing import List
from .tokens import Token
from .grammar import START, NONTERMINALS
from .ll1_table import build_ll1_table

class LL1Parser:
    def __init__(self):
        self.table, self.FIRST, self.FOLLOW = build_ll1_table()

    def parse(self, tokens: List[Token]) -> bool:
        # Convertimos tokens a secuencia de tipos (terminales)
        input_stream = [t.type for t in tokens]
        stack: List[str] = ["EOF", START]
        i = 0

        while stack:
            top = stack.pop()
            current = input_stream[i]

            if top == "EOF" and current == "EOF":
                return True

            if top not in NONTERMINALS:
                # Terminal esperado
                if top == current:
                    i += 1
                    continue
                else:
                    raise SyntaxError(f"Token inesperado '{current}' (esperaba '{top}')")

            # No terminal: consultamos tabla
            row = self.table.get(top, {})
            prod = row.get(current, None)

            if prod is None:
                # Si no hay entrada para el token actual, intentamos con ε por FOLLOW
                prod = row.get("EOF", None) if current == "EOF" else None
                if prod is None:
                    raise SyntaxError(
                        f"Error de sintaxis con '{current}' al expandir {top}. "
                        f"No hay producción válida en la tabla LL(1)."
                    )

            if prod != ["ε"]:
                for symbol in reversed(prod):
                    stack.append(symbol)
        # Si la pila se vacía incorrectamente
        return False
