import ply.lex as lex
from ply.lex import LexError

tokens = [
    'CICLO', 'FUNCION', 'BOOLEANO',
    'VARIABLE', 'ASIGNACION', 'CADENA', 'NUMERO', 'PREGUNTA', 'PARENTESIS',
    'PARENTESIS_CIERRE', 'LLAVE', 'LLAVE_CIERRE', 'OPERADORES', 'ASIGNACION_FOR',
    'PUNTO_COMA', 'OPERADOR_FOR', 'AUMENTO'
]

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

t_ignore = ' \t\n'

lexer = lex.lex()

def t_error(t):
    print(f"Error de sintaxis: Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

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
