# Parser LL(1) – Fase 1 (Proyecto TLP02-2025)

Este proyecto implementa un **parser LL(1)** mínimo para un subconjunto de expresiones y asignaciones tipo C, y demuestra sus **limitaciones frente al lenguaje natural** comparándolo con **spaCy**.  
Alcance alineado a Fase 1: implementar parser formal + demo comparativa con NLP:contentReference[oaicite:2]{index=2}.

## Requisitos
- Python 3.11+ (ideal 3.12 en Windows 11)
- `pip install -r requirements.txt`
- `python -m spacy download es_core_news_sm`

## Estructura
- `parser_formal/` → Lexer, gramática, FIRST/FOLLOW, tabla LL(1), parser y driver CLI.
- `examples/` → Casos válidos/erróneos para probar.
- `demo/compare_with_spacy.py` → Comparación con NLP (spaCy) sobre oraciones en español.

## Ejecutar
```bash
# activar venv (Windows Powershell)
.venv\Scripts\activate

# correr parser sobre ejemplos:
python -m parser_formal.driver "a = b + c * (d - e);"
python -m parser_formal.driver --file examples/expressions_ok.txt
python -m parser_formal.driver --file examples/expressions_bad.txt

# correr pruebas
pytest

# demo NLP VS parser formal
python demo/compare_with_spacy.py
