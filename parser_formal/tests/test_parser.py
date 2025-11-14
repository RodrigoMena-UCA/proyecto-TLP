import pytest
from parser_formal.lexer import lex
from parser_formal.parser import LL1Parser

ACCEPT = [
    "a = b + c * (d - e);",
    "x = (y + 2) * (z - 5);",
    "id123 = 42;",
    "result = (a);",
    "a = 1; b = 2;",
    "total = (valor1 + valor2) / 3 - 5;",
]
REJECT = [
    "= a + b;",
    "a = (b + c;",
    "a = b + ;",
    "hola como estas ;",
    "a = 3.14;",
    "resultado = valor",
    "Juan come manzanas.",
]

@pytest.mark.parametrize("src", ACCEPT)
def test_accept(src):
    tokens = lex(src)
    assert LL1Parser().parse(tokens) is True

@pytest.mark.parametrize("src", REJECT)
def test_reject(src):
    with pytest.raises(Exception):
        tokens = lex(src)
        LL1Parser().parse(tokens)
