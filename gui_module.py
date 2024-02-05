import tkinter as tk
from lexer_module import analyze

root = tk.Tk()
root.title("Analizador Léxico")

# Crear un área de texto para la entrada
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

output = tk.Text(root, height=10, width=50)
output.pack()

# Función para analizar el texto ingresado
def analizar():
    data = text_input.get("1.0", tk.END)
    results = analyze(data)
    output.delete("1.0", tk.END)
    for result in results:
        output.insert(tk.END, result + '\n')

analyze_button = tk.Button(root, text="Analizar", command=analizar)
analyze_button.pack()

root.mainloop()
