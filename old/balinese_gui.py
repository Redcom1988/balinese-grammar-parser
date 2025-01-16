import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import Dict, Set, Tuple
import re
from balinese_parser_cyk import BalineseParserRevised

class BalineseParserGUI:
    def __init__(self):
        # Initialize the main window
        self.root = tk.Tk()
        self.root.title("Balinese Sentence Parser")
        self.root.geometry("800x600")
        
        # Initialize the parser
        self.parser = BalineseParserRevised()
        
        # Create the main container
        self.create_main_layout()
        
        # Create the components
        self.create_input_section()
        self.create_results_section()
        self.create_details_section()
        
    def create_main_layout(self):
        """Create the main layout containers"""
        # Create main frames
        self.input_frame = ttk.LabelFrame(self.root, text="Input", padding="10")
        self.input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.results_frame = ttk.LabelFrame(self.root, text="Parsing Results", padding="10")
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.details_frame = ttk.LabelFrame(self.root, text="Parsing Details", padding="10")
        self.details_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
    def create_input_section(self):
        """Create the input section with text area and parse button"""
        # Add input instructions
        instruction_text = "Enter a Balinese sentence with components marked as: S (subject) P (predicate) O (object) Pel (complement) Ket (explanation)"
        instruction_label = ttk.Label(self.input_frame, text=instruction_text, wraplength=700)
        instruction_label.pack(fill=tk.X, pady=(0, 5))
        
        # Add example text
        example_text = "Example: S (Titiang) P (sampun meblanja) O (barang) Ket (ring pasar)"
        example_label = ttk.Label(self.input_frame, text=example_text, font=("TkDefaultFont", 9, "italic"))
        example_label.pack(fill=tk.X, pady=(0, 5))
        
        # Create text input area
        self.input_text = scrolledtext.ScrolledText(self.input_frame, height=4)
        self.input_text.pack(fill=tk.BOTH, expand=True)
        
        # Create parse button
        self.parse_button = ttk.Button(self.input_frame, text="Parse Sentence", command=self.parse_input)
        self.parse_button.pack(pady=10)
        
    def create_results_section(self):
        """Create the results section showing validity of components"""
        # Create a frame for results grid
        results_grid = ttk.Frame(self.results_frame)
        results_grid.pack(fill=tk.BOTH, expand=True)
        
        # Create labels for each component
        self.result_labels = {}
        components = ['S', 'P', 'O', 'Pel', 'Ket']
        
        for i, component in enumerate(components):
            # Component name label
            ttk.Label(results_grid, text=f"{component}:").grid(row=0, column=i*2, padx=5, pady=5, sticky='e')
            
            # Result label
            result_label = ttk.Label(results_grid, text="Not checked", width=10)
            result_label.grid(row=0, column=i*2+1, padx=5, pady=5, sticky='w')
            self.result_labels[component] = result_label
            
            # Configure column weights
            results_grid.columnconfigure(i*2, weight=1)
            results_grid.columnconfigure(i*2+1, weight=1)
            
    def create_details_section(self):
        """Create the details section showing parsing information"""
        # Create text area for details
        self.details_text = scrolledtext.ScrolledText(self.details_frame, height=8)
        self.details_text.pack(fill=tk.BOTH, expand=True)
        
    def parse_input(self):
        """Handle the parsing of input text and update the display"""
        # Get input text
        input_text = self.input_text.get("1.0", tk.END).strip()
        
        if not input_text:
            self.show_error("Please enter a sentence to parse")
            return
        
        try:
            # Parse the sentence
            results, details = self.parser.parse_sentence(input_text)
            
            # Update result labels
            for component in self.result_labels:
                if component in results:
                    is_valid = results[component]
                    self.result_labels[component].config(
                        text="Valid" if is_valid else "Invalid",
                        foreground="green" if is_valid else "red"
                    )
                else:
                    self.result_labels[component].config(
                        text="Not found",
                        foreground="gray"
                    )
            
            # Update details text
            self.update_details_text(details)
            
        except Exception as e:
            self.show_error(f"Error parsing sentence: {str(e)}")
    
    def update_details_text(self, details: Dict[str, Set[str]]):
        """Update the details text area with parsing information"""
        self.details_text.delete("1.0", tk.END)
        
        details_text = "Parsing Details:\n\n"
        for component, categories in details.items():
            details_text += f"{component} component contains: {', '.join(sorted(categories))}\n\n"
        
        self.details_text.insert("1.0", details_text)
    
    def show_error(self, message: str):
        """Display an error message"""
        # Clear previous results
        for label in self.result_labels.values():
            label.config(text="Error", foreground="red")
        
        # Show error in details
        self.details_text.delete("1.0", tk.END)
        self.details_text.insert("1.0", f"Error: {message}")
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

# Example usage
if __name__ == "__main__":
    app = BalineseParserGUI()
    app.run()