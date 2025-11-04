# Parser LL(1) - Fase 1 (Proyecto TLP02-2025)

Este proyecto implementa un parser LL(1) minimo para un subconjunto de expresiones y asignaciones tipo C y demuestra sus limitaciones frente al lenguaje natural comparandolo con spaCy. El alcance cubre la Fase 1: parser formal y demostracion comparativa con NLP.

## Requisitos
- Python 3.11+ (ideal 3.12 en Windows 11)
- `winget install -e --id Python.Python.3.12`
- `pip install -r requirements.txt`
- `python -m spacy download es_core_news_sm`

## Estructura
- `parser_formal/` -> Lexer, gramatica, conjuntos FIRST/FOLLOW, tabla LL(1), parser y driver CLI.
- `parser_formal/examples/` -> Casos validos e invalidos para ejecutar desde archivos.
- `parser_formal/demo/compare_with_spacy.py` -> Comparacion con spaCy sobre oraciones en espanol.
- `parser_formal/tests/` -> Pruebas unitarias del parser y del driver.

## Como ejecutar
```powershell
# activar entorno virtual (Windows PowerShell)
.venv\Scripts\activate

# correr parser sobre una cadena puntual
python -m parser_formal.driver "a = b + c * (d - e);"

# correr parser leyendo archivos de ejemplo incluidos en el repo
python -m parser_formal.driver --file parser_formal/examples/expression_ok.txt
python -m parser_formal.driver --file parser_formal/examples/expression_bad.txt

# ejecutar pruebas automatizadas
python -m pytest

# demo NLP vs parser formal (usar -m para resolver el paquete)
python -m parser_formal.demo.compare_with_spacy
```

## Ejemplos de ejecucion
Resultados obtenidos al correr los comandos anteriores en PowerShell:

```powershell
> python -m parser_formal.driver "a = b + c * (d - e);"
ACEPTADA: a = b + c * (d - e);

> python -m parser_formal.driver --file parser_formal/examples/expression_ok.txt
ACEPTADA: a = b + c * (d - e);
ACEPTADA: total = num1 - num2 / 3;
ACEPTADA: x = (y + 2) * (z - 5);
ACEPTADA: id123 = 42;
ACEPTADA: result = (a);

> python -m parser_formal.driver --file parser_formal/examples/expression_bad.txt
RECHAZADA: = a + b;                # falta ID al inicio (Caracter inesperado '#' en posicion 24)
RECHAZADA: a = b + ;               # falta termino (Caracter inesperado '#' en posicion 24)
RECHAZADA: a = (b + c;             # parentesis sin cerrar (Caracter inesperado '#' en posicion 24)
RECHAZADA: a = b + c) ;            # parentesis extra (Caracter inesperado '#' en posicion 24)
RECHAZADA: hola como estas ;       # tokens no validos para la gramatica formal (Caracter inesperado '#' en posicion 24)

> python -m pytest
.................                                                        [100%]
17 passed in 0.07s
```

Las lineas con `#` en `expression_bad.txt` son comentarios explicativos dentro del archivo y provocan deliberadamente el mensaje de error del lexer para mostrar como se rechazan simbolos fuera de la gramatica.

## Resultados de la demo formal vs spaCy
El parser LL(1) acepta asignaciones y expresiones de la gramatica definida, pero falla en cuanto la entrada se desvia del subconjunto controlado. La demo produce evidencia concreta:

```
Formal parser: RECHAZA - Juan come manzanas.  (motivo: caracter inesperado '.')
Formal parser: RECHAZA - El perro azul corre rapido.  (motivo: caracter inesperado '\u00e1')
Formal parser: RECHAZA - Maria y Jose escriben cartas largas.  (motivo: caracter inesperado '\u00ed')
```

En contraste, `python -m parser_formal.demo.compare_with_spacy` imprime el analisis de spaCy, donde cada token recibe etiquetas POS y dependencias, demostrando la diferencia de cobertura entre un parser LL(1) rigido y una libreria NLP estadistica.

## Cobertura de pruebas
- `parser_formal/tests/test_parser.py`: valida aceptaciones y rechazos esperados del parser LL(1).
- `parser_formal/tests/test_driver_cli.py`: cubre el CLI del driver y la lectura desde archivos.
- `parser_formal/tests/test_ll1_table.py`: asegura consistencia de los conjuntos FIRST/FOLLOW y de la tabla LL(1).

Ejecuta `python -m pytest` para comprobar que todas las pruebas continuan en verde tras cualquier modificacion.
