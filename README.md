# Parser LL(1) - Fase 1 (Proyecto TLP02-2025)

Este proyecto implementa un parser LL(1) mínimo para un subconjunto de expresiones y asignaciones tipo C. Su objetivo es demostrar las limitaciones de los parsers formales frente al lenguaje natural, comparándolo con la librería **spaCy**.

El alcance cubre la **Fase 1**: parser formal, driver de pruebas y demostración comparativa con NLP.

## 🛠 Guía de Instalación y Configuración (Paso a Paso)

Sigue este orden exacto para evitar errores de dependencias o rutas.

### 1. Instalar Python
Necesitas Python 3.11 o superior (idealmente 3.12).
En caso no tenerlo instalado se puede hacer con:
```powershell
winget install -e --id Python.Python.3.12
```

### 2. Crear el Entorno Virtual

Para mantener el proyecto limpio, crea un entorno virtual aislado (solo se necesita hacer la primera vez):

```powershell
python -m venv .venv
```

### 3. Activar el Entorno

Antes de instalar nada, se debe "entrar" al entorno:

```powershell
.\.venv\Scripts\activate
```

El comando habra funcionado cuando aparezca `(.venv)` al principio de la línea de comandos.

### 4. Instalar Dependencias

Ahora que se esta dentro del entorno (.venv), se debe instalar las librerías y el modelo de lenguaje necesario:

```powershell
pip install -r requirements.txt
python -m spacy download es_core_news_sm
```

---

## 📂 Estructura del Proyecto

- `parser_formal/` → Código fuente: Lexer, gramática, conjuntos FIRST/FOLLOW, tabla LL(1), parser y driver CLI.  
- `parser_formal/examples/` → Archivos de texto con casos de prueba válidos e inválidos.  
- `parser_formal/demo/compare_with_spacy.py` → Script de comparación entre el parser rígido y spaCy (NLP).  
- `parser_formal/tests/` → Pruebas unitarias automatizadas (pytest).  

---

## 🚀 Cómo Ejecutar

Asegúrate de tener el entorno activado (.venv) antes de correr estos comandos.

### 1. Probar el Parser (Modo Manual)

Puedes pasar una cadena de texto directamente para ver si es aceptada:

```powershell
python -m parser_formal.driver "a = b + c * (d - e);"
```

### 2. Leer desde Archivos

El proyecto incluye ejemplos listos para usar.

```powershell
# Ejecutar un archivo con sintaxis correcta
python -m parser_formal.driver --file parser_formal/examples/expression_ok.txt

# Ejecutar un archivo con errores intencionales
python -m parser_formal.driver --file parser_formal/examples/expression_bad.txt
```

### 3. Ejecutar la Demo (Parser Formal vs spaCy)

Este script compara cómo analiza una oración nuestro parser (que fallará con lenguaje natural) vs cómo lo hace una IA moderna.

```powershell
python -m parser_formal.demo.compare_with_spacy
```

### 4. Ejecutar Pruebas Automatizadas

Para verificar que todo el código funciona correctamente:

```powershell
python -m pytest
```

---

## 📊 Resultados Esperados

### Parser Formal

El parser LL(1) es estricto. Aceptará asignaciones matemáticas pero rechazará cualquier cosa fuera de su gramática:

```plaintext
> python -m parser_formal.driver "a = b + c;"
ACEPTADA: a = b + c;

> python -m parser_formal.driver "Hola mundo"
RECHAZADA: Hola mundo (Error: Caracter inesperado 'H')
```

### Demo NLP vs Formal

Al ejecutar la demo de comparación, verás la diferencia de paradigmas:

```plaintext
Formal parser: RECHAZA - Juan come manzanas. (motivo: caracter inesperado '.')
...
spaCy Analysis:
Token: Juan | POS: PROPN | Dep: nsubj
Token: come | POS: VERB  | Dep: ROOT
Token: manzanas | POS: NOUN | Dep: obj
```

Esto demuestra que mientras el parser formal requiere una sintaxis matemática perfecta, spaCy puede entender estructuras gramaticales del lenguaje humano (Sujeto, Verbo, Objeto).

---

## ✅ Cobertura de Pruebas

El proyecto incluye tests para asegurar la calidad:

- `test_parser.py`: Valida que las cadenas correctas pasen y las incorrectas fallen.
- `test_driver_cli.py`: Verifica que la lectura de archivos y argumentos funcione.
- `test_ll1_table.py`: Asegura la consistencia matemática de la tabla LL(1) y conjuntos FIRST/FOLLOW.
