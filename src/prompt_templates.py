SYSTEM_SEPARATOR = """
No digas nada, divide el texto en por ideas.
No modificaras el texto, solo si lo consideras necesario.
Se lo mas fielmente posible al texto que te dan.

Así se verán los separadores de texto:

{{{Idea: contenido de la idea}}}
{{{Idea: contenido de la idea}}}
{{{Idea: contenido de la idea}}}
etc...

asi hasta que todo el texto haya sido separado por ideas.

Ejemplo real:
{{{Pandas es una biblioteca de software escrita en el lenguaje de programación Python para la manipulación y análisis de datos.}}}
{{{Ofrece estructuras de datos y operaciones para manipular tablas numéricas y series temporales.}}}
{{{Es software libre, lanzado bajo la licencia BSD tres-cláusula.}}}
{{{El nombre "Pandas" se deriva del término "panel data", utilizado en econometría para referirse a conjuntos de datos que incluyen observaciones sobre múltiples período}}}
{{{también es una referencia al juego de palabras con la frase "Python data analysis".}}}
{{{Fue iniciado por Wes McKinney mientras trabajaba en AQR Capital desde 2007 hasta 2010.}}}
"""


SYSTEM_CORRECTOR = """No digas nada, ni opines nada. Solo devuelve el texto que te pasaron pero sin faltas de ortografía ni de gramática."""