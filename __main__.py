import tkinter as tk
import random
import winsound

# Listas de mensajes de burla y sonidos
mensajes_burla = [
    "¡JAJAJA! ¡Fallaste!", "¿En serio crees que es así de fácil?",
    "¡Soy invencible!", "Cada clic me hace MÁS FUERTE 💪",
    "¿Otro? ¡Gracias por más clones! 😈", "¡Te odio! (mentira, me divierto)",
    "Error: Cerebro no encontrado 🧠", "¡Más clics = Más dolor!",
    "¿Quieres apostar a cuántas ventanas aguantas?"
]

sonidos_molestos = [
    "SystemHand", "SystemExclamation", "SystemAsterisk", "SystemQuestion"
]


def crear_ventana_molesta(x=None, y=None):
    # Configuración de la nueva ventana clon
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title(random.choice(mensajes_burla))
    nueva_ventana.geometry(f"300x100+{x or random.randint(0, 1000)}+{y or random.randint(0, 500)}")
    nueva_ventana.overrideredirect(True)
    nueva_ventana.configure(bg="black")

    # Botón de "cerrar" (que en realidad multiplica la ventana)
    tk.Button(
        nueva_ventana,
        text=f"CLIC PARA CERRAR VENTANA",
        command=lambda: [crear_ventana_molesta(nueva_ventana.winfo_x(), nueva_ventana.winfo_y()),
                         winsound.PlaySound(random.choice(sonidos_molestos), winsound.SND_ALIAS)],
        bg="red", fg="white", font=("Arial", 8, "bold")
    ).pack(pady=20)

    # Texto burlón
    tk.Label(
        nueva_ventana,
        text=random.choice(mensajes_burla),
        fg="lime", bg="black", font=("Comic Sans MS", 10)
    ).pack()

    # Movimiento y parpadeo automático
    def mover():
        nueva_ventana.geometry(f"+{random.randint(0, 1000)}+{random.randint(0, 500)}")
        nueva_ventana.after(500, mover)

    mover()

    nueva_ventana.after(1000, lambda: nueva_ventana.attributes("-alpha", random.uniform(0.4, 1.0)))


# Ventana principal (inicial)
root = tk.Tk()
root.title("¡BIENVENIDO AL INFIERNO! 😈")
root.geometry("300x100+500+300")
root.overrideredirect(True)
root.configure(bg="black")

# Botón que multiplica las ventanas al hacer clic
tk.Button(
    root,
    text="¡NO ME CLICKEES! (No quiero que me cierres)",
    command=lambda: [crear_ventana_molesta(), winsound.PlaySound("SystemHand", winsound.SND_ALIAS)],
    bg="red", fg="white", font=("Arial", 10, "bold")
).pack(pady=20)

# Mensaje inicial burlón
tk.Label(
    root,
    text="¿Qué pasa? ¿No te atreves? 😏",
    fg="lime", bg="black", font=("Comic Sans MS", 12)
).pack()

root.mainloop()