import ply.lex as lex
import tkinter as tk
from ply.lex import LexError

# Lista de nombres de tokens
tokens = [
    'CICLO', 'FUNCION', 'BOOLEANO',
    'VARIABLE', 'ASIGNACION', 'CADENA', 'NUMERO', 'PREGUNTA', 'PARENTESIS', 
    'PARENTESIS_CIERRE', 'LLAVE', 'LLAVE_CIERRE', 'OPERADORES', 'ASIGNACION_FOR',
    'PUNTO_COMA', 'OPERADOR_FOR', 'AUMENTO'
]

# Reglas para expresiones regulares simples
t_ASIGNACION = r'='
t_PREGUNTA = r'\?'
t_PARENTESIS = r'\('
t_PARENTESIS_CIERRE = r'\)'
t_LLAVE = r'\{'
t_LLAVE_CIERRE = r'\}'
t_OPERADORES = r'==|<|>'
t_ASIGNACION_FOR = r':='
t_PUNTO_COMA = r';'
t_OPERADOR_FOR = r'>|<'
t_AUMENTO = r'\+\+|--'

# Reglas para expresiones regulares más complejas
def t_CICLO(t):
    r'for'
    return t

def t_FUNCION(t):
    r'fn'
    return t

def t_VARIABLE(t):
    r'[a-z]+'
    if t.value == 'for':
        t.type = 'CICLO'
    elif t.value == 'fn':
        t.type = 'FUNCION'
    elif t.value == 'true' or t.value == 'false':
        t.type = "BOOLEANO"
    return t

def t_BOOLEANO(t):
    r'true|false'
    return t

def t_CADENA(t):
    r'\"[a-z0-9 ]*\"'
    return t

def t_NUMERO(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Construir el lexer
lexer = lex.lex()

# Función para manejar errores en el lexer
def t_error(t):
    error_message = f"Error de sintaxis: Carácter ilegal '{t.value[0]}' en la línea {t.lineno}"
    output.insert(tk.END, error_message + '\n')
    t.lexer.skip(1)

# Función para analizar el texto ingresado
def analizar():
    data = text_input.get("1.0", tk.END)
    print(data)
    lexer.input(data)
    output.delete("1.0", tk.END)

    try:
        while True:
            tok = lexer.token()
            if not tok:
                break
            output.insert(tk.END, str(tok) + '\n')
    except LexError as e:
        output.insert(tk.END, f"Error de lexing: {e}\n")


# Crear la ventana principal
root = tk.Tk()
root.title("Analizador Léxico")

# Crear un área de texto para la entrada
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# Crear un botón para iniciar el análisis
analyze_button = tk.Button(root, text="Analizar", command=analizar)
analyze_button.pack()

# Crear un área de texto para mostrar la salida y los errores
output = tk.Text(root, height=10, width=50)
output.pack()

# Ejecutar la aplicación
root.mainloop()