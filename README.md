# ARBOL-DERIVACION

**INTRODUCCION**

En este trabajo se desarrolla un programa que analiza expresiones aritméticas y construye su árbol sintáctico. Para esto, se utiliza la librería Lark en Python, que permite definir la gramática y procesar operaciones como suma, resta, multiplicación y división.

Además, con ayuda de Graphviz, los árboles generados se convierten en imágenes, lo que facilita visualizar cómo se organiza cada expresión. De esta forma, se puede entender mejor la estructura interna de las operaciones matemáticas de manera clara y gráfica.

**COMO EJECUTARLO**

se realizo el programa en el sistema operativo de linux ubuntu

**Requisitos**

 PASO 1 -Instalación del motor de dibujo
 ```bash
  sudo apt update && sudo apt install -y graphviz
  ```

PASO 2 - Instalacion de librerias en Python

```bash
  pip install lark pydot --break-system-packages
```
