import ply.lex as lex
from ply.lex import LexError

tokens = [
    'PRINT', 'CICLO', 'FUNCION', 'BOOLEANO', 'VARIABLE', 'ASIGNACION',
    'CADENA', 'NUMERO', 'PREGUNTA', 'PARENTESIS', 'PARENTESIS_CIERRE',
    'LLAVE', 'LLAVE_CIERRE', 'OPERADORES', 'ASIGNACION_FOR', 'PUNTO_COMA',
    'OPERADOR_FOR', 'AUMENTO'
]

# Reglas de expresiones regulares simples para tokens
t_PRINT = r'Print'
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
t_FUNCION = r'fn'

def t_CICLO(t):
    r'for'
    return t

def t_VARIABLE(t):
    r'[a-z]+'
    if t.value == 'for':
        t.type = 'CICLO'
    elif t.value == 'fn':
        t.type = 'FUNCION'
    elif t.value == 'true' or t.value == 'false':
        t.type = "BOOLEANO"
    elif t.value == 'Print':
        t.type ="PRINT"
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

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def analyze(data):
    lexer.input(data)
    results = []
    try:
        while True:
            tok = lexer.token()
            if not tok:
                break
            results.append(str(tok))
    except LexError as e:
        results.append(f"Error de lexing: {e}")
    return results