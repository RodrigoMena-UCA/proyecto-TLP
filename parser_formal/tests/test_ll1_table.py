from parser_formal.ll1_table import build_ll1_table


def test_first_and_follow_core_entries():
    _, first, follow = build_ll1_table()
    assert first["Expr"] == {"ID", "LPAREN", "NUM"}
    assert {"EOF", "ID"} <= follow["Stmt"]


def test_ll1_table_core_rows():
    table, _, _ = build_ll1_table()
    assert table["Program"]["ID"] == ["StmtList", "EOF"]
    assert table["Stmt"]["ID"] == ["ID", "ASSIGN", "Expr", "SEMI"]
