import sys
from pathlib import Path

import pytest

from parser_formal import driver


def test_driver_cli_reads_file(tmp_path, capsys, monkeypatch):
    content = "a = b + c;\nresultado = valor;\n"
    file_path = tmp_path / "cases.txt"
    file_path.write_text(content)

    monkeypatch.setattr(sys, "argv", ["parser_formal.driver", "--file", str(file_path)])

    driver.main()
    captured = capsys.readouterr().out.splitlines()

    assert captured == [
        "ACEPTADA: a = b + c;",
        "ACEPTADA: resultado = valor;",
    ]


def test_driver_cli_reports_rejections(tmp_path, capsys, monkeypatch):
    file_path = tmp_path / "bad_cases.txt"
    file_path.write_text("a = b + ;\n")

    monkeypatch.setattr(sys, "argv", ["parser_formal.driver", "--file", str(file_path)])

    driver.main()
    out = capsys.readouterr().out

    assert "RECHAZADA: a = b + ;" in out
    assert "Error de sintaxis" in out
