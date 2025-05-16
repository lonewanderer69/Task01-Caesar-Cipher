import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, encrypt=True):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if encrypt else -shift
            shifted = (ord(char) - base + offset) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)
    return ''.join(result)

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher GUI")
        self.root.geometry("500x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Input Frame
        input_frame = ttk.Frame(self.root, padding=10)
        input_frame.pack(fill='x')
        
        # Text Input
        ttk.Label(input_frame, text="Message:").grid(row=0, column=0, sticky='w')
        self.text_input = tk.Text(input_frame, height=4, width=40)
        self.text_input.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Shift Value
        ttk.Label(input_frame, text="Shift Value:").grid(row=2, column=0, sticky='w', pady=5)
        self.shift_entry = ttk.Entry(input_frame, width=5)
        self.shift_entry.grid(row=2, column=1, sticky='w')
        self.shift_entry.insert(0, "3")
        
        # Action Buttons
        action_frame = ttk.Frame(self.root, padding=10)
        action_frame.pack(fill='x')
        
        self.mode_var = tk.StringVar(value="encrypt")
        ttk.Radiobutton(action_frame, text="Encrypt", variable=self.mode_var, 
                       value="encrypt").pack(side='left', padx=5)
        ttk.Radiobutton(action_frame, text="Decrypt", variable=self.mode_var,
                       value="decrypt").pack(side='left', padx=5)
        
        ttk.Button(action_frame, text="Process", command=self.process_text).pack(side='left', padx=10)
        ttk.Button(action_frame, text="Clear", command=self.clear_fields).pack(side='left')
        
        # Output
        output_frame = ttk.Frame(self.root, padding=10)
        output_frame.pack(fill='x')
        
        ttk.Label(output_frame, text="Result:").pack(anchor='w')
        self.output_text = tk.Text(output_frame, height=4, width=40, state='disabled')
        self.output_text.pack()
    
    def process_text(self):
        try:
            text = self.text_input.get("1.0", "end-1c")
            shift = int(self.shift_entry.get())
            mode = self.mode_var.get()
            
            result = caesar_cipher(text, shift, encrypt=(mode == "encrypt"))
            
            self.output_text.config(state='normal')
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)
            self.output_text.config(state='disabled')
        except ValueError:
            self.output_text.config(state='normal')
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "Error: Shift must be an integer!")
            self.output_text.config(state='disabled')
    
    def clear_fields(self):
        self.text_input.delete("1.0", "end")
        self.shift_entry.delete(0, 'end')
        self.shift_entry.insert(0, "3")
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", "end")
        self.output_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()