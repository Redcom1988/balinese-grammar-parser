import tkinter as tk
from tkinter import ttk, messagebox
import re
from kamusbali import words

class BalineseParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Balinese Sentence Parser")
        self.root.geometry("800x600")
        
        # Grammar rules dictionary
        self.grammar = {
            'K': ['S P', 'S P O', 'S P Pel', 'S P Ket', 'S P O Pel', 'S P O Ket', 'S P O Pel Ket'],
            'S': ['NP', 'Name'],
            'P': ['VP'],
            'O': ['NP', 'Name'],
            'Pel': ['NP', 'PP', 'AdjP', 'NumP', 'VP', 'Name'],
            'Ket': ['PP'],
            'NP': ['Noun', 'NP Det', 'Pronoun', 'NP Pronoun', 'NP Adj', 'Num NP', 'NP Prep', 'Adj NP', 'NumP NP'],
            'VP': ['Verb', 'Adv Verb', 'Verb Adv', 'Verb O', 'Verb Prep O', 'Verb NP', 'Verb AdjP', 'Verb PP'],
            'PP': ['Prep Noun', 'Prep Pronoun', 'Prep Det Noun', 'Prep Adj Noun', 'Prep Num Noun', 'Prep NP', 'Prep PP', 'Prep Name'],
            'AdjP': ['Adj', 'AdjP Noun', 'AdjP Adv', 'AdjP Prep'],
            'NumP': ['Num', 'NumP Noun', 'NumP Det Noun', 'NumP Adj Noun', 'NumP PP', 'NumP Pronoun']
        }

        self.words = words
        self.setup_gui()

    def setup_gui(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input section
        ttk.Label(main_frame, text="Enter Balinese Sentence (use \"\" for names):").grid(row=0, column=0, sticky=tk.W)
        self.input_text = ttk.Entry(main_frame, width=60)
        self.input_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

        # Parse button
        ttk.Button(main_frame, text="Parse Sentence", command=self.parse_sentence).grid(row=2, column=0, pady=10)

        # Result section
        ttk.Label(main_frame, text="Parsing Result:").grid(row=3, column=0, sticky=tk.W)
        self.result_text = tk.Text(main_frame, height=20, width=80, wrap=tk.WORD)
        self.result_text.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))

    def extract_words_and_names(self, sentence):
        """
        Extract words and names from the sentence, treating quoted text as names.
        Returns a list of tuples (word, is_name).
        """
        pattern = r'"([^"]+)"|(\S+)'
        matches = re.finditer(pattern, sentence)
        
        words_and_names = []
        for match in matches:
            if match.group(1) is not None:
                # This is a quoted name
                words_and_names.append((match.group(1), True))
            else:
                # This is a regular word
                words_and_names.append((match.group(2), False))
        
        return words_and_names

    def categorize_word(self, word):
        """Categorize a regular word (non-name)"""
        for category, word_list in self.words.items():
            if word.lower() in word_list:
                return category
        return None

    def matches_category(self, remaining_categories, component):
        """Check if categories match a grammar component through expansions"""
        if not remaining_categories:
            return False, 0
                
        if remaining_categories[0] == component:
            return True, 1
                
        if component not in self.grammar:
            return False, 0

        for expansion in self.grammar[component]:
            parts = expansion.split()
            if len(remaining_categories) >= len(parts):
                all_match = True
                for i, part in enumerate(parts):
                    if remaining_categories[i] != part:
                        all_match = False
                        break
                if all_match:
                    return True, len(parts)

        return False, 0

    def parse_sentence(self):
        sentence = self.input_text.get().strip()
        if not sentence:
            messagebox.showerror("Error", "Please enter a sentence")
            return

        # Extract words and names from the sentence
        words_and_names = self.extract_words_and_names(sentence)
        
        categories = []
        invalid_words = []
        original_words = []

        # Categorize each word
        for word, is_name in words_and_names:
            original_words.append(word)
            if is_name:
                categories.append('Name')
            else:
                category = self.categorize_word(word)
                if category:
                    categories.append(category)
                else:
                    invalid_words.append(word)

        # Clear previous results
        self.result_text.delete(1.0, tk.END)

        if invalid_words:
            self.result_text.insert(tk.END, f"Unknown words found: {', '.join(invalid_words)}\n\n")
            return

        # Try to match with grammar patterns
        pattern = ' '.join(categories)
        valid_structure = False
        matching_pattern = None

        for structure in self.grammar['K']:
            components = structure.split()
            current_pattern = []
            
            valid = True
            remaining_categories = categories.copy()
            
            for component in components:
                if not remaining_categories:
                    valid = False
                    break
                    
                matched, words_to_consume = self.matches_category(remaining_categories, component)
                if matched:
                    current_pattern.append(component)
                    for _ in range(words_to_consume):
                        if remaining_categories:
                            remaining_categories.pop(0)
                else:
                    valid = False
                    break

            if valid and not remaining_categories:
                valid_structure = True
                matching_pattern = structure
                break

        # Display results
        self.result_text.insert(tk.END, f"Original sentence: {sentence}\n\n")
        self.result_text.insert(tk.END, f"Words: {' '.join(original_words)}\n")
        self.result_text.insert(tk.END, f"Categories: {' '.join(categories)}\n\n")
        
        if valid_structure:
            self.result_text.insert(tk.END, f"Valid sentence structure found!\n")
            self.result_text.insert(tk.END, f"Matching pattern: {matching_pattern}\n")

            if 'VP' in matching_pattern.split():
                self.result_text.insert(tk.END, "\nThis is a Simple Balinese Sentence with Verbal Predicate (VP).\n")
        else:
            self.result_text.insert(tk.END, "No valid sentence structure found.\n")
            self.result_text.insert(tk.END, "Please check the grammar rules and word order.\n")


def main():
    root = tk.Tk()
    app = BalineseParserGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
