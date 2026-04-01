import os
import subprocess
from lark import Lark, Tree
import sys

# Gramática para expresiones aritméticas
gramatica = r"""
    ?e: e opsuma t | t
    ?t: t opmul f | f
    ?f: ID -> id | num -> num | "(" e ")" -> parentesis

    opsuma: "+" | "-"
    opmul : "*" | "/"
    num   : NUMBER
    ID    : /[a-zA-Z_]\w*/

    %import common.NUMBER
    %import common.WS
    %ignore WS
"""

def tree_to_dot(tree):
    """Convierte el objeto Tree de Lark a formato DOT para Graphviz"""
    nodes = []
    edges = []
    
    def walk(node):
        node_id = str(id(node))
        # Si es un Tree, el label es el nombre de la regla (e, t, f...)
        # Si es un Token, el label es el valor (2, +, *, x...)
        label = node.data if isinstance(node, Tree) else str(node)
        nodes.append(f'  "{node_id}" [label="{label}"];')
        
        if isinstance(node, Tree):
            for child in node.children:
                child_id = walk(child)
                edges.append(f'  "{node_id}" -> "{child_id}";')
        return node_id

    walk(tree)
    return "digraph G {\n" + "\n".join(nodes + edges) + "\n}"

def generar_arbol(cadena, nombre_base):
    cadena = cadena.strip() # Limpiar espacios y saltos de línea
    if not cadena: return

    print(f"Generando arbol para: {cadena}")
    try:
        # Usamos el parser LALR de Lark (similar a Bison)
        parser = Lark(gramatica, start='e', parser='lalr')
        parse_tree = parser.parse(cadena)
        
        dot_path = f"{nombre_base}.dot"
        png_path = f"{nombre_base}.png"
        
        # Generar código DOT
        with open(dot_path, "w") as f:
            f.write(tree_to_dot(parse_tree))
        
        # Ejecutar comando dot de Graphviz para crear el PNG
        subprocess.run(["dot", "-Tpng", dot_path, "-o", png_path])
        
        if os.path.exists(png_path):
            print(f"  Imagen guardada: {png_path}")
            os.remove(dot_path) # Limpiar archivo temporal .dot

    except Exception as e:
        print(f"  No se pudo procesar '{cadena}': {e}")

if __name__ == "__main__":
    archivo_input = "operaciones.txt"

    # Verificar si el archivo existe
    if not os.path.exists(archivo_input):
        print(f"Error: No se encuentra el archivo '{archivo_input}'")
        print("Crea un archivo llamado operaciones.txt con una operacion por linea.")
        sys.exit(1)

    with open(archivo_input, "r") as f:
        lineas = f.readlines()

    if not lineas:
        print("El archivo no contiene operaciones")
        sys.exit(1)

    print(f"CREANDO {len(lineas)} ARBOLES")
    
    for i, linea in enumerate(lineas):
        # Nombre de salida: arbol_1.png, arbol_2.png, etc.
        nombre_archivo = f"arbol_{i+1}"
        generar_arbol(linea, nombre_archivo)
