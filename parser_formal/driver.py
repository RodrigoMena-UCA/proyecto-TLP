import argparse
from .lexer import lex
from .parser import LL1Parser

def run_line(line: str):
    tokens = lex(line)
    parser = LL1Parser()
    ok = parser.parse(tokens)
    print(("ACEPTADA: " if ok else "RECHAZADA: ") + line.strip())

def main():
    ap = argparse.ArgumentParser(description="Parser LL(1) demo")
    ap.add_argument("input", nargs="?", help="Expresión o sentencia a evaluar")
    ap.add_argument("--file", help="Ruta de archivo con entradas (una por línea)")
    args = ap.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        run_line(line)
                    except Exception as e:
                        print(f"RECHAZADA: {line.strip()} ({e})")
    elif args.input:
        try:
            run_line(args.input)
        except Exception as e:
            print(f"RECHAZADA: {args.input.strip()} ({e})")
    else:
        ap.print_help()

if __name__ == "__main__":
    main()
