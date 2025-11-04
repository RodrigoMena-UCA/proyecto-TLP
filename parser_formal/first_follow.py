from typing import Dict, Set, List
from .grammar import GRAMMAR, NONTERMINALS, TERMINALS

EPS = "ε"

def compute_first() -> Dict[str, Set[str]]:
    FIRST = {X: set() for X in NONTERMINALS + TERMINALS + [EPS]}
    for t in TERMINALS:
        FIRST[t].add(t)
    FIRST[EPS].add(EPS)

    changed = True
    while changed:
        changed = False
        for A, prods in GRAMMAR.items():
            for prod in prods:
                # FIRST(A) += FIRST(prod)
                can_epsilon = True
                for symbol in prod:
                    FIRST_before = len(FIRST[A])
                    FIRST[A] |= (FIRST[symbol] - {EPS})
                    if EPS not in FIRST[symbol]:
                        can_epsilon = False
                        break
                    if len(FIRST[A]) > FIRST_before:
                        pass
                if can_epsilon:
                    if EPS not in FIRST[A]:
                        FIRST[A].add(EPS)
                        changed = True
                else:
                    if len(FIRST[A]) > FIRST_before:
                        changed = True
    return FIRST

def first_of_sequence(seq: List[str], FIRST: Dict[str, Set[str]]) -> Set[str]:
    result = set()
    for s in seq:
        result |= (FIRST[s] - {EPS})
        if EPS not in FIRST[s]:
            return result
    result.add(EPS)
    return result

def compute_follow(FIRST: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    FOLLOW = {A: set() for A in NONTERMINALS}
    FOLLOW["Program"].add("EOF")  # start symbol

    changed = True
    while changed:
        changed = False
        for A, prods in GRAMMAR.items():
            for prod in prods:
                for i, B in enumerate(prod):
                    if B in NONTERMINALS:
                        beta = prod[i+1:]
                        first_beta = first_of_sequence(beta, FIRST)
                        before = len(FOLLOW[B])
                        FOLLOW[B] |= (first_beta - {EPS})
                        if EPS in first_beta or len(beta) == 0:
                            FOLLOW[B] |= FOLLOW[A]
                        if len(FOLLOW[B]) > before:
                            changed = True
    return FOLLOW
