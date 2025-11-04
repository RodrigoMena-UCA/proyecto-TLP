import pytest
from parser_formal.lexer import lex
from parser_formal.parser import LL1Parser

ACCEPT = [
    "a = b + c * (d - e);",
    "x = (y + 2) * (z - 5);",
    "id123 = 42;",
    "result = (a);",
]
REJECT = [
    "= a + b;",
    "a = (b + c;",
    "a = b + ;",
    "hola como estas ;",
]

@pytest.mark.parametrize("src", ACCEPT)
def test_accept(src):
    tokens = lex(src)
    assert LL1Parser().parse(tokens) is True

@pytest.mark.parametrize("src", REJECT)
def test_reject(src):
    tokens = lex(src)
    with pytest.raises(Exception):
        LL1Parser().parse(tokens)
