import tkinter as tk
from tkinter import ttk
import time
from tkinter import scrolledtext
from typing import Dict, List, Set, Tuple
from balinese_cyk import CYKParser, CNFConverter
from cfg_rules import cfg_rules

class ParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Balinese Language Parser")
        self.root.geometry("800x650")  # Increased size to accommodate more content
        
        # Initialize parser components
        self.cfg_rules = cfg_rules
        self.converter = CNFConverter()
        self.cnf_rules = self.converter.convert_to_cnf(self.cfg_rules)
        self.parser = CYKParser(self.cnf_rules)
        
        # Configure styles
        style = ttk.Style()
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        
        # Create main frame with padding
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Balinese Language Parser", style='Title.TLabel')
        title_label.grid(row=0, column=0, pady=(0, 20), sticky=tk.W)
        
        # Input section
        input_label = ttk.Label(main_frame, text="Input Sentence:", font=('Arial', 10, 'bold'))
        input_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        self.input_text = scrolledtext.ScrolledText(main_frame, height=4, width=70, wrap=tk.WORD)
        self.input_text.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Parse button
        self.parse_button = ttk.Button(main_frame, text="Parse Sentence", command=self.handle_parse)
        self.parse_button.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Output section
        output_label = ttk.Label(main_frame, text="Parse Result:", font=('Arial', 10, 'bold'))
        output_label.grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        
        self.output_text = scrolledtext.ScrolledText(main_frame, height=25, width=70, wrap=tk.WORD)
        self.output_text.grid(row=5, column=0, sticky=(tk.W, tk.E))
        self.output_text.configure(state='disabled')
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Initialize state
        self.is_loading = False

    def update_output(self, text):
        """Helper method to update the output text widget"""
        self.output_text.configure(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', text)
        self.output_text.configure(state='disabled')

    def handle_parse(self):
        if not self.input_text.get('1.0', tk.END).strip() or self.is_loading:
            return
            
        self.is_loading = True
        self.parse_button.configure(state='disabled')
        self.parse_button['text'] = "Parsing..."
        
        # Get the input sentence
        input_sentence = self.input_text.get('1.0', tk.END).strip()
        
        # Create a string buffer to capture the output
        import io
        import sys
        output_buffer = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output_buffer
        
        # Perform parsing
        print(f"Parsing sentence: {input_sentence}")
        is_valid = self.parser.parse(input_sentence)
        print(f"Valid: {is_valid}")
        
        # Restore stdout and get the captured output
        sys.stdout = original_stdout
        parse_result = output_buffer.getvalue()
        output_buffer.close()
        
        # Update the GUI with the results
        self.update_output(parse_result)
        
        # Reset button state
        self.is_loading = False
        self.parse_button.configure(state='normal')
        self.parse_button['text'] = "Parse Sentence"

def main():
    root = tk.Tk()
    app = ParserGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()