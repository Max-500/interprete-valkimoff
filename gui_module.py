import tkinter as tk
from lexer_module import analyze
from parser_module import parse, parse_errors

root = tk.Tk()
root.title("Analizador Léxico y Sintáctico")

# Crear un área de texto para la entrada
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

output = tk.Text(root, height=10, width=50)
output.pack()

def analizar():
    data = text_input.get("1.0", tk.END)
    lexer_results, errors_found = analyze(data)  # Almacenar resultados y verificar errores
    
    print(errors_found)
    
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
        else:
            output.insert(tk.END, str(parser_result) + '\n')


analyze_button = tk.Button(root, text="Analizar", command=analizar)
analyze_button.pack()

root.mainloop()