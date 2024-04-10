import tkinter as tk
from lexer_module import analyze
from parser_module import parse, parse_errors
from semantic_analyzer import run_code

import subprocess
import sys

root = tk.Tk()
root.title("Analizador Léxico y Sintáctico")

# Crear un área de texto para la entrada
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

output = tk.Text(root, height=10, width=50)
output.pack()

terminal = tk.Text(root, height=10, width=50)
terminal.pack()

def analizar():
    terminal.delete("1.0", tk.END)
    data = text_input.get("1.0", tk.END)
    lexer_results, errors_found, _ = analyze(data)  # Almacenar resultados y verificar errores
        
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Resultados del Análisis Léxico:\n")
    for result in lexer_results:
        output.insert(tk.END, result + '\n')
        
    if len(errors_found) > 0:
        for error in errors_found:
            output.insert(tk.END, error + '\n')
    
    if errors_found:
        output.insert(tk.END, "\nSe encontraron errores léxicos. Análisis sintáctico detenido.\n")
    else:
        output.insert(tk.END, "\nProcediendo al Análisis Sintáctico...\n")
        parser_result = parse(data)  # Realiza el análisis sintáctico solo si no hay errores léxicos
        if parse_errors:  # Si hay errores de sintaxis
            for error in parse_errors:
                output.insert(tk.END, error + '\n')
            return
        else:
            output.insert(tk.END, "No se encontraron errores sintacticos")
            if run_code(lexer_results):
                try:
                    ruta_archivo = 'mi_script.py'

                    # Abre una nueva terminal y ejecuta el archivo Python
                    if sys.platform.startswith('win'):  # Para Windows
                        proceso = subprocess.Popen(['python', ruta_archivo], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                    else:  # Para Linux y otros sistemas Unix
                        subprocess.Popen(['gnome-terminal', '-x', 'python', ruta_archivo])
                        proceso = subprocess.Popen(['python', ruta_archivo], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    for line in iter(proceso.stdout.readline, b''):
                        terminal.insert(tk.END, line.decode(sys.stdout.encoding))
                except:
                    pass
            else:
                output.insert(tk.END, 'Error al ejecutar el archivo')


analyze_button = tk.Button(root, text="Analizar", command=analizar)
analyze_button.pack()

root.mainloop()