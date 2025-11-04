from typing import Dict, List
from .grammar import GRAMMAR, NONTERMINALS, TERMINALS
from .first_follow import compute_first, compute_follow, first_of_sequence, EPS

def build_ll1_table():
    FIRST = compute_first()
    FOLLOW = compute_follow(FIRST)

    table: Dict[str, Dict[str, List[str]]] = {A: {} for A in NONTERMINALS}

    for A, prods in GRAMMAR.items():
        for prod in prods:
            first_set = first_of_sequence(prod, FIRST)
            for a in (first_set - {EPS}):
                if a in table[A]:
                    raise ValueError(f"Gramática no LL(1): conflicto en M[{A},{a}]")
                table[A][a] = prod
            if EPS in first_set:
                for b in FOLLOW[A]:
                    if b in table[A]:
                        raise ValueError(f"Gramática no LL(1): conflicto en M[{A},{b}] por ε")
                    table[A][b] = [EPS]
    return table, FIRST, FOLLOW
