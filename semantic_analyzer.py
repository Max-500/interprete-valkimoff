import re

variables = []
functions = []

def run_code(data):
    variables.clear()
    functions.clear()
    with open('mi_script.py', 'w') as _:
        pass
    
    for i in range(len(data)):
        length = len(data[i])
        elements = data[i][9:length-1]
        new_elements = elements.split(',')
        if new_elements[0] == 'VARIABLE':
            length_asignacion = len(data[i+1])
            is_variable = data[i+1][9:length_asignacion-1]
            is_asignacion = is_variable.split(',')
            if is_asignacion[0] == 'ASIGNACION':
                length_variable = len(data[i+2])
                valor = data[i+2][9:length_variable-1]
                variable = valor.split(',')
                variables.append(new_elements[1][1:len(new_elements[1])-1])
                pam = ''
                if variable[1][1:len(variable[1])-1] == 'true':
                    pam = True
                elif detect_quotes(variable[1]):
                    pam = variable[1][1:len(variable[1])-1]
                else:
                    pam = variable[1]
                codigo = '\n{0} = {1}\n'.format(new_elements[1][1:len(new_elements[1])-1], pam)
                with open('mi_script.py', 'a') as archivo:
                    archivo.write(codigo)
        elif new_elements[0] == 'PREGUNTA':
            length_variable_if = len(data[i+1])
            variable = data[i+1][9:length_variable_if]
            first_part = variable.split(',')
            first_part = first_part[1][1:len(first_part[1])-1]
            if not is_declared(first_part):
                with open('mi_script.py', 'w') as _:
                    pass
                return False
            
            ope_length = len(data[i+2])
            ope = data[i+2][9:ope_length]
            ope = ope.split(',')
            ope = ope[1][1:len(ope[1])-1]

            second_part_length = len(data[i+3])
            second_part = data[i+3][9:second_part_length]
            second_part = second_part.split(',')
            second_part = second_part[1][1:len(second_part[1])-1]
            if not is_declared(second_part):
                with open('mi_script.py', 'w') as _:
                    pass
                return False
                        
            impresion = data[i+7]
            impresion = data[i+7][9:len(data[i+7])]
            impresion = impresion.split(',')
            
            pam_impresion = ''
            if impresion[0] == 'VARIABLE':
                pam_impresion = impresion[1][1:len(impresion[1])-1]
                if not is_declared(pam_impresion) or is_function(pam_impresion):
                    with open('mi_script.py', 'w') as _:
                        pass
                    return False
            else:
                pam_impresion = impresion[1][1:len(impresion[1])-1]
            
            codigo = '\nif {0} {1} {2}:\n\t print({3})\n'.format(first_part, ope, second_part, pam_impresion)
            with open('mi_script.py', 'a') as archivo:
                archivo.write(codigo)
        
        elif new_elements[0] == 'CICLO':
            first_part_for = data[i+2]
            first_part_for = data[i+2][9:len(first_part_for)]
            first_part_for = first_part_for.split(',')
            first_part_for = first_part_for[1][1:len(first_part_for[1])-1]
            
            check = data[i+6]
            check = data[i+6][9:len(check)]
            check = check.split(',')
            check = check[1][1:len(check[1])-1]
            
            check_cond = data[i+10]
            check_cond = data[i+6][9:len(check_cond)]
            check_cond = check_cond.split(',')
            check_cond = check_cond[1][1:len(check_cond[1])-1]
            
            if first_part_for != check and first_part_for != check_cond:
                return False
            
            value_first_part_for = data[i+4]
            value_first_part_for = data[i+4][9:len(value_first_part_for)]
            value_first_part_for = value_first_part_for.split(',')
            value_first_part_for = value_first_part_for[1]
            
            ope_for = data[i+7]
            ope_for = data[i+7][9:len(ope_for)]
            ope_for = ope_for.split(',')
            ope_for = ope_for[1]
            ope_for = ope_for[1:len(ope_for)-1]
            
            second_part_for = data[i+8]
            second_part_for = data[i+8][9:len(second_part_for)]
            second_part_for = second_part_for.split(',')
            second_part_for = second_part_for[1][1:len(second_part_for[1])-1]
            
            aumento = data[i+11]
            aumento = data[i+11][9:len(aumento)]
            aumento = aumento.split(',')
            aumento = aumento[1][1:len(aumento[1])-1]
            
            impresion = data[i+16]
            impresion = data[i+16][9:len(data[i+7])]
            impresion = impresion.split(',')
            pam_impresion = ''
            if impresion[0] == 'VARIABLE':
                pam_impresion = impresion[1][1:len(impresion[1])-1]
                if not is_declared(pam_impresion) and pam_impresion != first_part_for:
                    with open('mi_script.py', 'w') as _:
                        pass
                    return False
            else:
                pam_impresion = impresion[1][1:len(impresion[1])-1]
                
            if aumento == '++':
                aumento = '+'
            else:
                aumento = '-'

            if not is_declared(second_part_for):
                return False
            
            codigo = '\n{0} = {1} \nwhile {0} {2} {3}: \n\tprint({4}) \n\t{0} {5}= 1'.format(first_part_for, value_first_part_for, ope_for, second_part_for, pam_impresion, aumento)
            with open('mi_script.py', 'a') as archivo:
                archivo.write(codigo)
        
        elif new_elements[0] == 'FUNCION':
            name_function = data[i+1]
            name_function = data[i+1][9:len(name_function)]
            name_function = name_function.split(',')
            name_function = name_function[1][1:len(name_function[1])-1]
            if is_declared(name_function):
                with open('mi_script.py', 'w') as _:
                    pass
                return False
            functions.append(name_function)
            impresion = data[i+7]
            impresion = data[i+7][9:len(data[i+7])]
            impresion = impresion.split(',')
            pam_impresion = ''
            if impresion[0] == 'VARIABLE':
                pam_impresion = impresion[1][1:len(impresion[1])-1]
                if not is_declared(pam_impresion) and pam_impresion != first_part_for:
                    with open('mi_script.py', 'w') as _:
                        pass
                    return False
            else:
                pam_impresion = impresion[1][1:len(impresion[1])-1]
            codigo = '\ndef {0}(): \n\tprint({1}) \n{0}()'.format(name_function, pam_impresion)
            with open('mi_script.py', 'a') as archivo:
                archivo.write(codigo)
    return True

def detect_quotes(s):
    if re.search(r'\".*\"', s):
        return True
    else:
        return False

def is_declared(var):
    for element in variables:
        if element == var:
            return True
    return False

def is_function(var_fn):
    for element in functions:
        if element == var_fn:
            return True
    return False