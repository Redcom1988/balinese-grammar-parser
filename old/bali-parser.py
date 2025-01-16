from typing import List, Dict, Set, Tuple
import re
import tkinter as tk
from tkinter import ttk, scrolledtext
from datetime import datetime

class BalineseParser:
    def __init__(self):
        # Initialize grammar rules
        self.grammar_rules = {
            'K': {('S', 'P', 'Pel', 'Ket'), ('S', 'P', 'Pel'), ('S', 'P', 'Ket'), 
                ('S', 'P', 'O', 'Ket'), ('S', 'P', 'O', 'Pel'), ('S', 'P', 'O'), ('S', 'P')},
            # Sentence structure rules
            'S': {('NP',)},  # Fixed tuple syntax
            'P': {('VP',)},  # Fixed tuple syntax
            'O': {('NP',)},
            'Pel': {('NP',), ('PP',), ('AdjP',)},
            'Ket': {('PP',), ('AdvP',)},
            
            # Phrase structure rules
            'NP': {('Noun',)},  # Simplified for clarity
            'VP': {('Verb',), ('Adv', 'Verb')},
            'AdjP': {('Adj',), ('Adv', 'Adj')},
            'PP': {('Prep', 'NP')},
            'NumP': {('Num',), ('Num', 'Det')},
        }   
        
        # Initialize word classes with common Balinese words
        self.word_classes = {
            'Noun': {
                'warung',      # restaurant
                'jaja',        # snack
                'umah',        # house
                'nasi',        # rice
                'siap',        # chicken
                'sampi',       # cow
                'sekolah',     # school
                'buku',        # book
                'meja',        # table
                'kursi'        # chair
            },
            'Verb': {
                'ngajeng',     # eat
                'medem',       # sleep
                'malaib',      # run
                'negak',       # sit
                'majalan',     # walk
                'nginum',      # drink
                'nulis',       # write
                'maca',        # read
                'madagang',    # sell
                'meli'         # buy
            },
            'Adj': {
                'jegeg',       # beautiful
                'bagus',       # good
                'gede',        # big
                'cenik',       # small
                'putih',       # white
                'selem',       # black
                'anyar',       # new
                'tua',         # old
                'jelek',       # bad
                'becik'        # nice
            },
            'Adv': {
                'jani',        # now
                'ibi',         # yesterday
                'mani',        # tomorrow
                'enggal',      # quickly
                'adeng',       # slowly
                'sai',         # often
                'kadang',      # sometimes
                'pelan',       # slowly
                'sampun',      # already
                'durung'       # not yet
            },
            'Pronoun': {
                'tiang',       # I (polite)
                'icang',       # I (casual)
                'ia',          # he/she
                'ipun',        # he/she (polite)
                'cai',         # you (casual)
                'ragane',      # you (polite)
                'ida',         # he/she (very polite)
                'iraga',       # we
                'gang',        # I (very casual)
                'nika'         # that
            },
            'Num': {
                'besik',       # one
                'dua',         # two
                'telu',        # three
                'pat',         # four
                'lima',        # five
                'nem',         # six
                'pitu',        # seven
                'kutus',       # eight
                'sia',         # nine
                'dasa'         # ten
            },
            'Prep': {
                'di',          # in/at
                'ka',          # to
                'uli',         # from
                'ring',        # in/at (polite)
                'saking',      # from (polite)
                'sareng',      # with (polite)
                'ajak',        # with
                'ke',          # to
                'sig',         # at
                'antuk'        # by
            },
            'Det': {
                'puniki',      # this
                'punika',      # that
                'ene',         # this (casual)
                'ento',        # that (casual)
                'niki',        # this (polite)
                'nika',        # that (polite)
                'ne',          # this
                'to',          # that
                'sane',        # which/that
                'sami'         # all
            }
        }

    def tokenize(self, sentence: str) -> List[str]:
        """Tokenize the input sentence and handle quoted names."""
        # Find all quoted names and temporarily replace them
        names = re.findall(r'"([^"]*)"', sentence)
        for i, name in enumerate(names):
            sentence = sentence.replace(f'"{name}"', f'_NAME_{i}_')
        
        # Split the sentence into tokens
        tokens = sentence.strip().split()
        
        # Replace the name placeholders back
        for i, name in enumerate(names):
            for j, token in enumerate(tokens):
                if token == f'_NAME_{i}_':
                    tokens[j] = f'"{name}"'
        
        return tokens

    def get_word_class(self, word: str) -> Set[str]:
        """Determine the word class of a token."""
        # Handle quoted names as nouns
        if word.startswith('"') and word.endswith('"'):
            return {'Noun'}
        
        # Check all word classes for the word
        classes = set()
        for word_class, words in self.word_classes.items():
            if word in words:
                classes.add(word_class)
        return classes or {'Unknown'}

    def cyk_parse(self, sentence: str) -> Dict[Tuple[int, int], Set[str]]:
        tokens = self.tokenize(sentence)
        n = len(tokens)
        table = {}
        
        # First row: initialize with word classes and check grammar rules
        for i in range(n):
            word_classes = self.get_word_class(tokens[i])
            phrases = set(word_classes)  # Start with basic word classes
            
            # Keep applying rules until no new phrases can be added
            added = True
            while added:
                added = False
                for lhs, rhs_set in self.grammar_rules.items():
                    for rhs in rhs_set:
                        if len(rhs) == 1 and rhs[0] in phrases and lhs not in phrases:
                            phrases.add(lhs)
                            added = True
            
            table[i, i] = phrases
        
        # Fill in the rest of the table
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                table[start, end] = set()
                
                # Try all possible splits of this span
                for split in range(start, end):
                    left_constituents = table[start, split]
                    right_constituents = table[split + 1, end]
                    
                    # Check all grammar rules
                    for lhs, rhs_set in self.grammar_rules.items():
                        for rhs in rhs_set:
                            if len(rhs) == 2:
                                if rhs[0] in left_constituents and rhs[1] in right_constituents:
                                    table[start, end].add(lhs)
                                    
                    # Special handling for full sentence
                    if start == 0 and end == n-1:
                        for split in range(start, end):
                            if 'S' in table[start, split] and 'P' in table[split+1, end]:
                                table[start, end].add('K')
        
        return table
    
    def identify_sentence_parts(self, table: Dict[Tuple[int, int], Set[str]], tokens: List[str]) -> str:
        """Show the CYK parsing table structure and results with detailed information."""
        n = len(tokens)
        result = []
        
        # Add timestamp and user info
        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        result.append(f"Current Date and Time (UTC - YYYY-MM-DD HH:MM:SS formatted): {current_time}")
        result.append(f"Current User's Login: Redcom1988\n")
        
        # Show input information
        result.append(f"Input Sentence: {' '.join(tokens)}")
        result.append(f"Tokens: {' '.join(tokens)}\n")
        
        # Show sentence structure
        result.append("Sentence structure:")
        # Find VP combinations first for sentence structure
        vp_spans = {}
        for i in range(n-1):
            for j in range(i+1, n):
                if 'VP' in table.get((i, j), set()):
                    vp_spans[(i, j)] = ' '.join(tokens[i:j+1])
        
        # Construct main sentence structure
        i = 0
        sentence_parts = []
        while i < n:
            word = tokens[i]
            word_classes = table.get((i, i), set())
            
            # Check if this is the start of a VP
            is_part_of_vp = False
            for (start, end), vp_text in vp_spans.items():
                if i == start:
                    sentence_parts.append(f"P ({vp_text})")
                    i = end + 1
                    is_part_of_vp = True
                    break
            
            if not is_part_of_vp:
                if 'S' in word_classes:
                    sentence_parts.append(f"S ({word})")
                elif 'P' in word_classes:
                    sentence_parts.append(f"P ({word})")
                else:
                    sentence_parts.append(f"? ({word})")
                i += 1
        
        result.append(' '.join(sentence_parts))
        
        # Show detailed phrase structure
        result.append("\nPhrase structure:")
        
        # First table row (individual words)
        result.append("\n1st table row")
        for i in range(n):
            phrases = table.get((i, i), set())
            sorted_phrases = sorted(phrases)
            result.append(f"{', '.join(sorted_phrases)} ({tokens[i]}) at [{i}, 0]")
        
        # Second table row (pairs of words)
        if n >= 2:
            result.append("\n2nd table row")
            for i in range(n-1):
                phrases = table.get((i, i+1), set())
                text = ' '.join(tokens[i:i+2])
                if phrases:
                    sorted_phrases = sorted(phrases)
                    result.append(f"{', '.join(sorted_phrases)} ({text}) at [{i}, 1]")
                else:
                    result.append(f"no combination ({text}) at [{i}, 1]")
        
        # Third table row (three or more words)
        if n >= 3:
            result.append("\n3rd table row")
            phrases = table.get((0, n-1), set())
            text = ' '.join(tokens[0:n])
            if phrases:
                sorted_phrases = sorted(phrases)
                result.append(f"{', '.join(sorted_phrases)} ({text}) at [0, 2]")
            else:
                result.append(f"no combination ({text}) at [0, 2]")
        
        return '\n'.join(result)

    def print_parse_tree(self, table: Dict[Tuple[int, int], Set[str]], tokens: List[str]):
        """Print the sentence parts instead of parse tree."""
        tokens = self.tokenize(' '.join(tokens))
        result = self.identify_sentence_parts(table, tokens)
        print(result)

class BalineseParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Balinese Sentence Parser")
        self.parser = BalineseParser()
        
        # Configure main window
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input frame
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding="5")
        input_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Input field
        ttk.Label(input_frame, text="Enter Balinese sentence:").grid(row=0, column=0, padx=5, pady=5)
        self.sentence_input = ttk.Entry(input_frame, width=60)
        self.sentence_input.grid(row=0, column=1, padx=5, pady=5)
        
        # Parse button
        ttk.Button(input_frame, text="Parse", command=self.parse_sentence).grid(row=0, column=2, padx=5, pady=5)
        
        # Output frame
        output_frame = ttk.LabelFrame(main_frame, text="Parse Result", padding="5")
        output_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Output text area
        self.output_text = scrolledtext.ScrolledText(output_frame, width=80, height=20)
        self.output_text.grid(row=0, column=0, padx=5, pady=5)
        
        # Word classes frame
        word_classes_frame = ttk.LabelFrame(main_frame, text="Available Words", padding="5")
        word_classes_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Create notebook for word classes
        self.word_classes_notebook = ttk.Notebook(word_classes_frame)
        self.word_classes_notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create tabs for each word class
        for word_class, words in self.parser.word_classes.items():
            frame = ttk.Frame(self.word_classes_notebook)
            self.word_classes_notebook.add(frame, text=word_class)
            
            # Add scrolled text widget for words
            text_widget = scrolledtext.ScrolledText(frame, width=70, height=4)
            text_widget.pack(expand=True, fill='both')
            text_widget.insert(tk.END, ', '.join(sorted(words)))
            text_widget.configure(state='disabled')

    def parse_sentence(self):
        # Clear previous output
        self.output_text.delete(1.0, tk.END)
        
        # Get input sentence
        sentence = self.sentence_input.get().strip()
        
        if not sentence:
            self.output_text.insert(tk.END, "Please enter a sentence to parse.")
            return
        
        # Parse the sentence
        parse_table = self.parser.cyk_parse(sentence)
        tokens = self.parser.tokenize(sentence)    
        
        self.output_text.insert(tk.END, f"Input Sentence: {sentence}\n")
        self.output_text.insert(tk.END, f"Tokens: {' '.join(tokens)}\n\n")
        
        # Add parsing results
        result = self.parser.identify_sentence_parts(parse_table, tokens)
        self.output_text.insert(tk.END, result)

def main():
    root = tk.Tk()
    app = BalineseParserGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()