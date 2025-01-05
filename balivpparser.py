import tkinter as tk
from tkinter import ttk, messagebox
import re
from kamusbali import words

class BalineseVPParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Balinese VP Sentence Parser")
        self.root.geometry("800x600")
        
        # Grammar rules focused on VP patterns
        self.grammar = {
            'K': ['S P', 'S P O', 'S P Pel', 'S P Ket', 'S P O Pel', 'S P O Ket', 'S P O Pel Ket'],
            # 'S': ['NP', 'Name'],
            'S': ['NP', 'Name' 'Name Det', ],
            'P': ['VP'], 
            'O': ['NP', 'Name'],
            'S': ['Noun', 'Name'],
            'P': ['Verb', 'VP'], 
            'O': ['Noun', 'Name'],
            'Pel': ['NP', 'PP', 'AdjP', 'NumP', 'VP', 'Name'],
            'Ket': ['PP'],
            'NP': ['Noun Adj'],
            # 'VP': ['Adv Verb', 'Adv Adj Verba', 'Prep Verb', 'Verb Noun', 'Noun Verb'],
            'VP': [ 'Noun Verb',
                    'Pronoun Adv Verb' # Tiang kapah melajah
                    'Adv Verb Noun', # Sering membaca buku, sering makan nasi, sering minum air, sering bermain bola
                    'Verb Adv', # berjalan cepat, Bekerja Keras
                    'Verb Prep Object', # mejalan ke dapur, maplalian ke Taman
                    'Pronoun Verb Adj', # ia mejalan enggal
                    'Pronoun Verb Object' # tiang maem nasi
                    ],
            # 'VP': ['Adv Verb', 'Verb Adv', 'Adv Adj Verba', 'Prep Verb', 'Verb Prep'], # Versi berbagai sumber
            # 'VP': ['Noun Verb', 'Adv Verb', 'Verb Adv', 'Adj Verb', 'Verb Adj', 'Prep Verb', 'Verb Prep', 'Pronoun Verb'],
            'VP': ['Noun intransitiveVerb','Noun transitiveVerb Noun',
                   'Name intransitiveVerb','Name transitiveVerb Name',
                   'Name transitiveVerb Noun','Noun transitiveVerb Name',
                   'Noun contextDependentVerb'],
            'AdjP': ['Adv Adj','Adj Adv'],
            'PP': ['Prep Noun'],
            'NumP': ['Num Noun']
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

        # Examples section
        ttk.Label(main_frame, text="Example sentences with VP predicates:").grid(row=5, column=0, sticky=tk.W, pady=(10,0))
        examples = (
            "1. \"Made\" malajah (Made belajar)\n"
            "2. Ipun sesai makarya (Dia selalu bekerja)\n"
            "3. \"Wayan\" pepes meli baju (Wayan sering membeli baju)\n"
            "4. Ia kapah nongos di Badung (Dia jarang tinggal di Badung)"
        )
        examples_text = tk.Text(main_frame, height=5, width=80, wrap=tk.WORD)
        examples_text.grid(row=6, column=0, sticky=tk.W)
        examples_text.insert('1.0', examples)
        examples_text.configure(state='disabled', bg=self.root.cget('bg'), relief='flat')

    def extract_words_and_names(self, sentence):
        pattern = r'"([^"]+)"|(\S+)'
        matches = re.finditer(pattern, sentence)
        words_and_names = []
        for match in matches:
            if match.group(1) is not None:
                words_and_names.append((match.group(1), True))
            else:
                words_and_names.append((match.group(2), False))
        return words_and_names

    def matches_category(self, remaining_categories, component):
        if not remaining_categories:
            return False, 0
                
        if remaining_categories[0] == component:
            return True, 1

        if component not in self.grammar:
            return False, 0

        # Handle VP patterns specifically
        if component == 'P':
            # Check for single Verb
            if remaining_categories[0] == 'Verb':
                return True, 1
            # Check for Adv + Verb pattern
            elif len(remaining_categories) >= 2 and remaining_categories[0] == 'Adv' and remaining_categories[1] == 'Verb':
                return True, 2
            # Check for Verb + Adv pattern
            elif len(remaining_categories) >= 2 and remaining_categories[0] == 'Verb' and remaining_categories[1] == 'Adv':
                return True, 2

        # For PP (Ket) case
        if (component == 'Ket' or component == 'PP') and len(remaining_categories) >= 2:
            if remaining_categories[0] == 'Prep' and remaining_categories[1] in ['Noun', 'Pronoun', 'Name']:
                return True, 2

        for expansion in self.grammar[component]:
            parts = expansion.split()
            if len(remaining_categories) >= len(parts):
                all_match = True
                for i, part in enumerate(parts):
                    if remaining_categories[i] != part and part not in self.grammar:
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

        words_and_names = self.extract_words_and_names(sentence)
        categories = []
        invalid_words = []
        original_words = []

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

        self.result_text.delete(1.0, tk.END)

        if invalid_words:
            self.result_text.insert(tk.END, f"Unknown words found: {', '.join(invalid_words)}\n\n")
            return

        pattern = ' '.join(categories)
        valid_structure = False
        matching_pattern = None

        # Validate pattern with focus on VP predicates
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
            # Check if predicate is actually a VP
            pred_index = matching_pattern.split().index('P')
            is_vp = False
            
            # Check various VP patterns
            if categories[pred_index] == 'Verb':
                is_vp = True
            elif len(categories) > pred_index + 1 and (
                (categories[pred_index] == 'Adv' and categories[pred_index + 1] == 'Verb') or
                (categories[pred_index] == 'Verb' and categories[pred_index + 1] == 'Adv')
            ):
                is_vp = True
                
            if is_vp:
                self.result_text.insert(tk.END, "Valid sentence with VP predicate!\n")
                self.result_text.insert(tk.END, f"Matching pattern: {matching_pattern}\n")
                
                # Show word roles
                self.result_text.insert(tk.END, "\nWord roles:\n")
                i = 0
                while i < len(original_words):
                    if i < len(original_words) - 1:
                        # Handle Adv + Verb case
                        if categories[i] == 'Adv' and categories[i+1] == 'Verb':
                            self.result_text.insert(tk.END, f"{original_words[i]} {original_words[i+1]}: P (VP)\n")
                            i += 2
                            continue
                        # Handle Verb + Adv case
                        elif categories[i] == 'Verb' and categories[i+1] == 'Adv':
                            self.result_text.insert(tk.END, f"{original_words[i]} {original_words[i+1]}: P (VP)\n")
                            i += 2
                            continue
                        # Handle Prep + Noun case
                        elif categories[i] == 'Prep' and categories[i+1] in ['Noun', 'Pronoun', 'Name']:
                            self.result_text.insert(tk.END, f"{original_words[i]} {original_words[i+1]}: Ket (PP)\n")
                            i += 2
                            continue
                    
                    word = original_words[i]
                    category = categories[i]
                    role = ''
                    if category == 'Name':
                        if i == 0:
                            role = 'Subject'
                        elif i == 2 and len(categories) > 2:
                            role = 'Object'
                        else:
                            role = 'Complement'
                    elif category == 'Verb':
                        role = 'P (VP)'
                    else:
                        role = category
                    self.result_text.insert(tk.END, f"{word}: {role}\n")
                    i += 1
            else:
                self.result_text.insert(tk.END, "Invalid sentence: Predicate is not a VP\n")
                self.result_text.insert(tk.END, "The sentence must contain a verb phrase as predicate\n")
        else:
            self.result_text.insert(tk.END, "Invalid sentence structure.\n")
            self.result_text.insert(tk.END, "Please check the grammar rules and word order.\n")

    def categorize_word(self, word):
        for category, word_list in self.words.items():
            if word.lower() in word_list:
                return category
        return None

def main():
    root = tk.Tk()
    app = BalineseVPParserGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()