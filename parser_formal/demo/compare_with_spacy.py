import spacy
from parser_formal.lexer import lex
from parser_formal.parser import LL1Parser

def try_formal_parser(text: str):
    try:
        tokens = lex(text)
        ok = LL1Parser().parse(tokens)
        print(f"Formal parser: {'ACEPTA' if ok else 'RECHAZA'} — {text}")
    except Exception as e:
        print(f"Formal parser: RECHAZA — {text}  (motivo: {e})")

def spacy_demo(text: str, nlp):
    doc = nlp(text)
    print(f"\nspaCy análisis: {text}")
    for tok in doc:
        print(f"{tok.text:12}  POS={tok.pos_:6}  DEP={tok.dep_:10}  HEAD={tok.head.text}")
    print("-"*60)

if __name__ == "__main__":
    nlp = spacy.load("es_core_news_sm")

    # Frases naturales
    sentences = [
        "Juan come manzanas.",
        "El perro azul corre rápido.",
        "María y José escriben cartas largas."
    ]

    print("== Intento con parser formal (debe fallar) ==")
    for s in sentences:
        try_formal_parser(s)

    print("\n== Análisis con spaCy (debe producir POS/DEP) ==")
    for s in sentences:
        spacy_demo(s, nlp)
