# ARBOL-DERIVACION

**INTRODUCCION**

En este trabajo se desarrolla un programa que analiza expresiones aritméticas y construye su árbol sintáctico. Para esto, se utiliza la librería Lark en Python, que permite definir la gramática y procesar operaciones como suma, resta, multiplicación y división.

Además, con ayuda de Graphviz, los árboles generados se convierten en imágenes, lo que facilita visualizar cómo se organiza cada expresión. De esta forma, se puede entender mejor la estructura interna de las operaciones matemáticas de manera clara y gráfica.

**COMO EJECUTARLO**

se realizo el programa en el sistema operativo de linux ubuntu

**Requisitos**

PASO 1

Instalación del motor de dibujo UBUNTU
 ```bash
  sudo apt update && sudo apt install -y graphviz
  ```
Instalación del motor de dibujo WINDOWS

```bash
  pip install lark pydot
```

Instalacion del motor de dibujo MacOS

```bash
  brew install graphviz
```
PASO 2

Instalacion de librerias en Python UBUNTU

```bash
  pip install lark pydot --break-system-packages
```

Instalacion de librerias en Python MacOS
```bash
pip3 install lark pydot
```

**DESCRIPCION DEL CODIGO**

El programa opera mediante la integración de la librería Lark y el motor Graphviz. En la primera etapa, el sistema utiliza un analizador de tipo LALR para procesar las expresiones basadas en una gramática formal. Esta estructura jerárquica permite que el software identifique correctamente la prioridad de los operadores y maneje la recursividad de las reglas, asegurando que cada elemento de la operación se agrupe según las normas matemáticas de asociación y precedencia.

Una vez validada la sintaxis, el script recorre el árbol generado y lo traduce manualmente a lenguaje DOT, asignando identificadores únicos a cada nodo para evitar redundancias visuales. Finalmente, el programa automatiza la lectura por lotes desde un archivo externo, procesando cada línea de texto y ejecutando un comando de sistema que renderiza la estructura lógica en una imagen de alta resolución. Este flujo garantiza que cualquier expresión compleja se convierta en una representación gráfica clara y precisa en formato PNG.



**RESULTADOS Y PRUEBAS

**Ejecucion en consola**

Como se observa en la captura de ejecución, el programa lee secuencialmente cada línea del archivo operaciones.txt. Durante el proceso, el sistema notifica en tiempo real qué cadena está analizando y confirma la creación exitosa de cada imagen. Esta fase es crucial para asegurar que no existan errores de sintaxis en las expresiones de entrada y que el motor de renderizado esté respondiendo correctamente.

![Ejecución en Consola](Captura%20desde%202026-03-31%2019-17-07.png)
