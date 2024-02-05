import ply.yacc as yacc
from lexer_module import tokens  # Asegúrate de que este importe es correcto

# Definición de la estructura del programa
def p_program(p):
    '''program : statement
               | statement program'''
    if len(p) == 2:
        p[0] = (p[1],)
    else:
        p[0] = (p[1],) + p[2]

# Definición de los posibles statements
def p_statement(p):
    '''statement : DV
                 | DEC
                 | DFN
                 | DF'''
    p[0] = p[1]

# Declaración de variables
def p_declaracion_variable(p):
    '''DV : VARIABLE ASIGNACION VALS'''
    p[0] = ('declaracion_variable', p[1], p[3])

# Estructura de control (ejemplo con condicional)
def p_estructura_control(p):
    '''DEC : PREGUNTA COND LLAVE CT LLAVE_CIERRE'''
    p[0] = ('estructura_control', p[2], p[4])

# Definición de funciones
def p_definicion_funcion(p):
    '''DFN : FUNCION VARIABLE PARENTESIS PARENTESIS_CIERRE LLAVE CT LLAVE_CIERRE'''
    p[0] = ('definicion_funcion', p[2], p[6])

# Ciclo for
def p_ciclo_for(p):
    '''DF : CICLO PARENTESIS VARIABLE ASIGNACION_FOR NUMERO PUNTO_COMA VARIABLE OPERADORES VARIABLE PUNTO_COMA VARIABLE AUMENTO PARENTESIS_CIERRE LLAVE CT LLAVE_CIERRE'''
    p[0] = ('ciclo_for', {
        'inicializacion': (p[3], p[5]),
        'condicion': (p[7], p[8], p[9]),
        'actualizacion': (p[11], p[12]),
        'cuerpo': p[14]
    })

# Condición
def p_condicion(p):
    '''COND : VARIABLE OPERADORES VARIABLE'''
    p[0] = ('condicion', p[1], p[2], p[3])

# Contenido del control de flujo
def p_ct(p):
    '''CT : PRINT PARENTESIS VARIABLE PARENTESIS_CIERRE
          | PRINT PARENTESIS CADENA PARENTESIS_CIERRE'''
    p[0] = ('print', p[3])

# Valores (booleanos, cadenas, números)
def p_valores(p):
    '''VALS : BOOLEANO
            | valor_cadena
            | N'''
    p[0] = p[1]

# Valor cadena
def p_valor_cadena(p):
    '''valor_cadena : CADENA'''
    p[0] = p[1]

# Números
def p_numero(p):
    '''N : NUMERO'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis en EOF")

parser = yacc.yacc()

def parse(data):
    result = parser.parse(data)
    return result

if __name__ == '__main__':
    test_strings = [
        "a = false",
        "b = \"hello world 123 oh me vengo\"",
        "c = 123",
        "d = 123.456",
        """
            ?a < b {
                Print (c)
            }
            a = true
        """,
        '''
        c = true
        fn mifuncion() {
            Print(c)
        }
        ''',
        "variable = 10 for (x := 0; x < variable; x++) { Print(x) }",
    ]
    
    for s in test_strings:
        print(f"Testing: {s}")
        result = parse(s)
        print(f"Result: {result}\n")
