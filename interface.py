import tkinter as tk

# letra da música (trecho)
lyrics = [
    "I wanna be your vacuum cleaner",
    "Breathing in your dust",
    "I wanna be your Ford Cortina",
    "I will never rust",
    "I just wanna be yours",
    "",
    "I wanna be your raincoat",
    "For those frequent rainy days",
    "I wanna be your dreamboat",
    "When you want to sail away",
    "Let me be yours",
    "",
    "I just wanna be yours"
]

# configurações de velocidade
char_delay = 50   # delay em ms entre caracteres
line_delay = 500  # delay em ms entre linhas

current_line = 0
current_char = 0

def type_text():
    global current_line, current_char

    if current_line < len(lyrics):
        line = lyrics[current_line]

        if current_char < len(line):
            text_box.insert(tk.END, line[current_char])
            current_char += 1
            root.after(char_delay, type_text)  # chama de novo para próxima letra
        else:
            text_box.insert(tk.END, "\n")  # fim da linha
            current_line += 1
            current_char = 0
            root.after(line_delay, type_text)  # espera antes de próxima linha

# janela principal
root = tk.Tk()
root.title("I Wanna Be Yours - Arctic Monkeys")
root.configure(bg="black")

# caixa de texto ocupando toda a janela
text_box = tk.Text(root, font=("Arial", 14), bg="black", fg="white", wrap="word", bd=0, highlightthickness=0)
text_box.pack(expand=True, fill="both")

# inicia a digitação automática
type_text()

root.mainloop()
