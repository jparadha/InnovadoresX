import tkinter as tk
from tkinter import messagebox

def registrar():
    # Validación básica
    if not entry_nombre.get().strip():
        messagebox.showwarning("Atención", "El nombre es obligatorio.")
        return

    #materias optativas
    seleccionadas = [m for m, v in vars_materias.items() if v.get() == 1]
    
    # Manejo de información: Mostrar en terminal de VS Code
    print("\n" + "═"*50)
    print("REGISTRO DE ESTUDIANTE")
    print("═"*50)
    print(f"NOMBRE:          {entry_nombre.get()}")
    print(f"APELLIDO:        {entry_apellido.get()}")
    print(f"EDAD:            {entry_edad.get()} años")
    print(f"CLASE:           {entry_clase.get()}")
    print(f"SECCIÓN:         {entry_seccion.get()}")
    print(f"ESTADO:          {var_inscripcion.get()}")
    print(f"OPTATIVAS:       {', '.join(seleccionadas) if seleccionadas else 'Ninguna'}")
    print(f"COMENTARIOS:     {text_comentarios.get('1.0', tk.END).strip()}")
    print(f"NIVEL ESCOLAR:   {var_nivel.get()}")
    print("═"*50 + "\n")
    
    messagebox.showinfo("Registro", "Información enviada a la terminal.")

def limpiar():
    # Reiniciar todos los campos del formulario
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_clase.delete(0, tk.END)
    entry_seccion.delete(0, tk.END)
    var_inscripcion.set("No Inscrito")
    for v in vars_materias.values():
        v.set(0)
    text_comentarios.delete("1.0", tk.END)
    var_nivel.set("Seleccionar")

# --- Ventana Principal ---
root = tk.Tk()
root.title("Sistema de Registro Escolar")
root.geometry("700x780")
root.configure(bg="#f8fafc")

# 1. FRAME: DATOS PERSONALES
f_personal = tk.LabelFrame(root, text=" Datos personales ", padx=15, pady=10, bg="white", font=("Arial", 10, "bold"))
f_personal.pack(padx=25, pady=10, fill="x")

tk.Label(f_personal, text="Nombre:", bg="white").grid(row=0, column=0, sticky="w", pady=2)
entry_nombre = tk.Entry(f_personal, width=30); entry_nombre.grid(row=0, column=1, padx=10)

tk.Label(f_personal, text="Apellido:", bg="white").grid(row=1, column=0, sticky="w", pady=2)
entry_apellido = tk.Entry(f_personal, width=30); entry_apellido.grid(row=1, column=1, padx=10)

tk.Label(f_personal, text="Edad:", bg="white").grid(row=2, column=0, sticky="w", pady=2)
entry_edad = tk.Entry(f_personal, width=10); entry_edad.grid(row=2, column=1, sticky="w", padx=10)

# 2. FRAME: DETALLES ACADÉMICOS
f_detalles = tk.LabelFrame(root, text=" Detalles Académicos ", padx=15, pady=10, bg="white", font=("Arial", 10, "bold"))
f_detalles.pack(padx=25, pady=10, fill="x")

tk.Label(f_detalles, text="Clase:", bg="white").grid(row=0, column=0, sticky="w", pady=2)
entry_clase = tk.Entry(f_detalles, width=25); entry_clase.grid(row=0, column=1, padx=10)

tk.Label(f_detalles, text="Sección:", bg="white").grid(row=1, column=0, sticky="w", pady=2)
entry_seccion = tk.Entry(f_detalles, width=10); entry_seccion.grid(row=1, column=1, sticky="w", padx=10)

# 3. FRAME: ESTADO DE INSCRIPCIÓN (Radiobuttons)
f_estado = tk.LabelFrame(root, text=" Estado de inscripción ", bg="white", font=("Arial", 10, "bold"), pady=10)
f_estado.pack(padx=25, pady=10, fill="x")

var_inscripcion = tk.StringVar(value="No Inscrito")
tk.Radiobutton(f_estado, text="Inscrito", variable=var_inscripcion, value="Inscrito", bg="white").pack(side="left", padx=40)
tk.Radiobutton(f_estado, text="No Inscrito", variable=var_inscripcion, value="No Inscrito", bg="white").pack(side="left")

# 4. FRAME: MATERIAS OPTATIVAS (Checkbuttons)
f_optativas = tk.LabelFrame(root, text=" Materias optativas ", bg="white", font=("Arial", 10, "bold"), padx=10, pady=10)
f_optativas.pack(padx=25, pady=10, fill="x")

opciones = ["Física", "Biología", "Química", "Filosofía"]
vars_materias = {opt: tk.IntVar() for opt in opciones}
for opt in opciones:
    tk.Checkbutton(f_optativas, text=opt, variable=vars_materias[opt], bg="white").pack(side="left", expand=True)

# 5. FRAME: COMENTARIOS ADICIONALES (Label + Text)
f_comentarios = tk.LabelFrame(root, text=" Comentarios adicionales ", bg="white", font=("Arial", 10, "bold"), padx=10, pady=10)
f_comentarios.pack(padx=25, pady=10, fill="x")

tk.Label(f_comentarios, text="Comentarios:", bg="white").pack(anchor="w")
text_comentarios = tk.Text(f_comentarios, height=4, font=("Arial", 10))
text_comentarios.pack(fill="x")

# 6. MENÚ DESPLEGABLE PARA NIVEL ESCOLAR
f_nivel = tk.LabelFrame(root, text=" Nivel escolar ", bg="white", font=("Arial", 10, "bold"), padx=15, pady=10)
f_nivel.pack(padx=25, pady=10, fill="x")

var_nivel = tk.StringVar(value="Seleccionar")
menu_nivel = tk.OptionMenu(f_nivel, var_nivel, "Primaria", "Secundaria")
menu_nivel.config(bg="white", width=20)
menu_nivel.pack(anchor="w")

# 7. BOTONES DE ACCIÓN
f_botones = tk.Frame(root, bg="#f8fafc")
f_botones.pack(pady=20)

btn_registrar = tk.Button(f_botones, text="Registrar Estudiante", command=registrar, bg="#0f172a", fg="white", font=("Arial", 9, "bold"), padx=20, pady=5)
btn_registrar.pack(side="left", padx=10)

btn_limpiar = tk.Button(f_botones, text="Limpiar", command=limpiar, bg="#be123c", fg="white", font=("Arial", 9, "bold"), padx=20, pady=5)
btn_limpiar.pack(side="left", padx=10)

root.mainloop()