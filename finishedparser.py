import tkinter as tk
from tkinter import ttk, scrolledtext
from kamusbali import words, nounCategories, verbCategoryPairs

class BalineseVPParser:
    def __init__(self, root):
        self.root = root
        self.root.title("Balinese VP Parser")
        self.setup_gui()

    def setup_gui(self):
        # Configure the grid layout for the main window
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Input frame
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input text area
        ttk.Label(input_frame, text='Enter Balinese text: (use "" to indicate names)').grid(row=0, column=0, sticky=tk.W)
        self.input_text = scrolledtext.ScrolledText(input_frame, width=50, height=10)
        self.input_text.grid(row=1, column=0, pady=5)

        # Parse button
        ttk.Button(input_frame, text="Parse VP", command=self.parse_text).grid(row=2, column=0, pady=5)

        # Results frame
        results_frame = ttk.Frame(self.root, padding="10")
        results_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Results text area
        ttk.Label(results_frame, text="Parsing Results:").grid(row=0, column=0, sticky=tk.W)
        self.results_text = scrolledtext.ScrolledText(results_frame, width=50, height=10)
        self.results_text.grid(row=1, column=0, pady=5)

    def is_person(self, word):
        # Check if word is in people category or between quotes
        return (word in nounCategories['people'] or 
                (word.startswith('"') and word.endswith('"')))

    def get_word_type(self, word):
        # Remove quotes if present
        clean_word = word.strip('"')
        
        for word_type, word_list in words.items():
            if clean_word in word_list:
                return word_type
        return None

    def is_in_any_noun_category(self, word):
        # Remove quotes if present
        word = word.strip('"')
        for category, words in nounCategories.items():
            if word in words:
                return True
        return False

    def is_valid_vp(self, tokens):
        valid_vps = []
        
        for i in range(len(tokens) - 1):
            # Rule 1: Noun/People/Pronoun + intransitiveVerb
            if ((self.is_in_any_noun_category(tokens[i]) or self.get_word_type(tokens[i]) == 'Pronoun' or self.is_person(tokens[i])) and
                    self.get_word_type(tokens[i + 1]) == 'intransitiveVerb'):
                valid_vps.append({
                    'type': 'Noun/People/Pronoun + IntransitiveVerb',
                    'phrase': f"{tokens[i]} {tokens[i + 1]}"
                })

            # Rule 2: Noun/People/Pronoun + transitiveVerb + Object
            if i < len(tokens) - 2:
                if ((self.is_in_any_noun_category(tokens[i]) or self.get_word_type(tokens[i]) == 'Pronoun' or self.is_person(tokens[i])) and
                        self.get_word_type(tokens[i + 1]) == 'transitiveVerb'):
                    verb = tokens[i + 1]
                    object_word = tokens[i + 2].strip('"')
                    
                    if verb in verbCategoryPairs:
                        valid_categories = verbCategoryPairs[verb]
                        for category in valid_categories:
                            if object_word in nounCategories.get(category, []):
                                valid_vps.append({
                                    'type': 'Noun/People/Pronoun + TransitiveVerb + ValidObject',
                                    'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                                })
                                break

            # Rule 3: Adv + Verb + Noun/Person/Pronoun
            if i < len(tokens) - 2:
                if (self.get_word_type(tokens[i]) == 'Adv' and
                        self.get_word_type(tokens[i + 1]) in ['intransitiveVerb', 'transitiveVerb', 'contextDependentVerb']):
                    third_token = tokens[i + 2].strip('"')
                    
                    if (self.get_word_type(tokens[i + 2]) == 'Pronoun' or 
                            self.is_person(tokens[i + 2]) or 
                            self.is_in_any_noun_category(third_token)):
                        valid_vps.append({
                            'type': 'Adverb + Verb + Noun/Person/Pronoun',
                            'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                        })

            # Rule 4: People/Pronoun + Adv + Verb
            if i < len(tokens) - 2:
                if ((self.get_word_type(tokens[i]) == 'Pronoun' or self.is_person(tokens[i])) and
                        self.get_word_type(tokens[i + 1]) == 'Adv' and
                        self.get_word_type(tokens[i + 2]) in ['intransitiveVerb']):
                    valid_vps.append({
                        'type': 'People/Pronoun + Adverb + Verb',
                        'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                    })

            # Rule 5: People/Pronoun + Verb + Adv
            if i < len(tokens) - 2:
                if ((self.get_word_type(tokens[i]) == 'Pronoun' or self.is_person(tokens[i])) and
                        self.get_word_type(tokens[i + 1]) in ['intransitiveVerb', 'transitiveVerb'] and
                        self.get_word_type(tokens[i + 2]) == 'Adv'):
                    valid_vps.append({
                        'type': 'People/Pronoun + Verb + Adverb',
                        'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                    })

            # Rule 6: Noun/People/Pronoun + contextDependentVerb
            if ((self.is_in_any_noun_category(tokens[i]) or self.get_word_type(tokens[i]) == 'Pronoun' or self.is_person(tokens[i])) and
                    self.get_word_type(tokens[i + 1]) == 'contextDependentVerb'):
                verb = tokens[i + 1]
                if verb in verbCategoryPairs:
                    valid_categories = verbCategoryPairs[verb]
                    noun_category = self.get_noun_category(tokens[i])
                    if noun_category in valid_categories:
                        valid_vps.append({
                            'type': 'Noun/People/Pronoun + ContextDependentVerb',
                            'phrase': f"{tokens[i]} {tokens[i + 1]}"
                        })

            # Rule 7: Det + Noun + Verb
            if i < len(tokens) - 2:
                if (self.get_word_type(tokens[i]) == 'Det' and
                        (self.is_in_any_noun_category(tokens[i + 1]) or self.is_person(tokens[i + 1])) and
                        self.get_word_type(tokens[i + 2]) in ['intransitiveVerb', 'transitiveVerb']):
                    valid_vps.append({
                        'type': 'Determiner + Noun + Verb',
                        'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                    })

            # Rule 8: Noun/People/Pronoun + Verb + Prep + Noun
            if i < len(tokens) - 3:
                if ((self.is_in_any_noun_category(tokens[i]) or self.get_word_type(tokens[i]) == 'Pronoun' or self.is_person(tokens[i])) and
                        self.get_word_type(tokens[i + 1]) in ['intransitiveVerb', 'transitiveVerb'] and
                        self.get_word_type(tokens[i + 2]) == 'Prep' and
                        (self.is_in_any_noun_category(tokens[i + 3]) or self.is_person(tokens[i + 3]))):
                    valid_vps.append({
                        'type': 'Noun/People/Pronoun + Verb + Preposition + Noun',
                        'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]} {tokens[i + 3]}"
                    })

            # Rule 9: Num + Noun + Verb
            if i < len(tokens) - 2:
                if (self.get_word_type(tokens[i]) == 'Num' and
                        self.is_in_any_noun_category(tokens[i + 1]) and
                        self.get_word_type(tokens[i + 2]) in ['intransitiveVerb', 'transitiveVerb']):
                    valid_vps.append({
                        'type': 'Number + Noun + Verb',
                        'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                    })

            # Rule 10: Adj + Noun + Verb
            if i < len(tokens) - 2:
                if (self.get_word_type(tokens[i]) == 'Adj' and
                        self.is_in_any_noun_category(tokens[i + 1]) and
                        self.get_word_type(tokens[i + 2]) in ['intransitiveVerb', 'transitiveVerb']):
                    valid_vps.append({
                        'type': 'Adjective + Noun + Verb',
                        'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                    })

            # Rule 11: People/Pronoun + Adv + Verb (Baraja sesai malajah, Tiang kapah melajah)
            if i < len(tokens) - 2:
                if ((self.is_person(tokens[i]) or self.get_word_type(tokens[i]) == 'Pronoun') and
                        self.get_word_type(tokens[i + 1]) == 'Adv' and
                        self.get_word_type(tokens[i + 2]) in ['intransitiveVerb', 'transitiveVerb']):
                    valid_vps.append({
                        'type': 'People/Pronoun + Adverb + Verb',
                        'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                    })

            # Rule 12: Adv + Verb + Noun (Sering makan nasi)
            if i < len(tokens) - 2:
                if (self.get_word_type(tokens[i]) == 'Adv' and
                        self.get_word_type(tokens[i + 1]) in ['transitiveVerb', 'intransitiveVerb']):
                    third_token = tokens[i + 2].strip('"')
                    verb = tokens[i + 1]
                    
                    if verb in verbCategoryPairs:
                        valid_categories = verbCategoryPairs[verb]
                        for category in valid_categories:
                            if third_token in nounCategories.get(category, []):
                                valid_vps.append({
                                    'type': 'Adverb + Verb + Noun',
                                    'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                                })
                                break

            # Rule 13: Verb + Adv (mejalan enggal)
            if (self.get_word_type(tokens[i]) in ['intransitiveVerb', 'transitiveVerb'] and
                    self.get_word_type(tokens[i + 1]) == 'Adv'):
                valid_vps.append({
                    'type': 'Verb + Adverb',
                    'phrase': f"{tokens[i]} {tokens[i + 1]}"
                })

            # Rule 14: Verb + Prep + Object (mejalan ke dapur)
            if i < len(tokens) - 2:
                if (self.get_word_type(tokens[i]) in ['intransitiveVerb', 'transitiveVerb'] and
                        self.get_word_type(tokens[i + 1]) == 'Prep' and
                        self.is_in_any_noun_category(tokens[i + 2])):
                    valid_vps.append({
                        'type': 'Verb + Preposition + Object',
                        'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                    })

            # Rule 15: Pronoun + Verb + Adj (ia mejalan enggal)
            if i < len(tokens) - 2:
                if (self.get_word_type(tokens[i]) == 'Pronoun' and
                        self.get_word_type(tokens[i + 1]) in ['intransitiveVerb', 'transitiveVerb'] and
                        self.get_word_type(tokens[i + 2]) == 'Adj'):
                    valid_vps.append({
                        'type': 'Pronoun + Verb + Adjective',
                        'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                    })

        return valid_vps

    def check_sentence_structure(self, tokens):
        structures = []
        
        if len(tokens) < 2:  # Need at least subject and predicate
            return structures

        # Helper function to identify objects and complements
        def get_object_type(word):
            word = word.strip('"')
            if self.is_person(word) or self.get_word_type(word) == 'Pronoun':
                return 'person'
            # Check if word exists in any noun category
            if self.is_in_any_noun_category(word):
                return 'object'
            return None

        # Helper function to check if token is a subject
        def is_subject(token):
            return (self.is_person(token) or 
                    self.get_word_type(token) == 'Pronoun' or 
                    self.is_in_any_noun_category(token))

        # Helper function to check if token is a predicate (verb)
        def is_predicate(token):
            return self.get_word_type(token) in ['intransitiveVerb', 'transitiveVerb', 'contextDependentVerb']

        # Helper function to check if token is a complement (Pel)
        def is_complement(token):
            return (self.get_word_type(token) == 'Adj' or 
                    self.get_word_type(token) == 'Num' or 
                    token.strip('"') in nounCategories.get('abstract', []))

        # Helper function to check if token is a description (Ket)
        def is_description(token):
            return (self.get_word_type(token) == 'Adv' or 
                    self.get_word_type(token) == 'Prep' or
                    token.strip('"') in nounCategories.get('places', []))

        structures = []
        i = 0
        
        while i < len(tokens):
            matched = False
            
            # Try longest patterns first
            # SPOPelKet (Subject-Predicate-Object-Complement-Description)
            if i < len(tokens) - 4:
                if (is_subject(tokens[i]) and 
                    is_predicate(tokens[i + 1]) and 
                    get_object_type(tokens[i + 2]) and 
                    is_complement(tokens[i + 3]) and 
                    is_description(tokens[i + 4])):
                    structures.append({
                        'type': 'SPOPelKet (Subject-Predicate-Object-Complement-Description)',
                        'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]} {tokens[i + 3]} {tokens[i + 4]}"
                    })
                    i += 5
                    matched = True
                    continue

            # SPOPel and SPOKet (4-word patterns)
            if i < len(tokens) - 3 and not matched:
                if (is_subject(tokens[i]) and 
                    is_predicate(tokens[i + 1]) and 
                    get_object_type(tokens[i + 2])):
                    if is_complement(tokens[i + 3]):
                        structures.append({
                            'type': 'SPOPel (Subject-Predicate-Object-Complement)',
                            'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]} {tokens[i + 3]}"
                        })
                        i += 4
                        matched = True
                        continue
                    elif is_description(tokens[i + 3]):
                        structures.append({
                            'type': 'SPOKet (Subject-Predicate-Object-Description)',
                            'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]} {tokens[i + 3]}"
                        })
                        i += 4
                        matched = True
                        continue

            # SPO, SPPel, SPKet (3-word patterns)
            if i < len(tokens) - 2 and not matched:
                if is_subject(tokens[i]) and is_predicate(tokens[i + 1]):
                    if get_object_type(tokens[i + 2]):
                        structures.append({
                            'type': 'SPO (Subject-Predicate-Object)',
                            'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                        })
                        i += 3
                        matched = True
                        continue
                    elif is_complement(tokens[i + 2]):
                        structures.append({
                            'type': 'SPPel (Subject-Predicate-Complement)',
                            'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                        })
                        i += 3
                        matched = True
                        continue
                    elif is_description(tokens[i + 2]):
                        structures.append({
                            'type': 'SPKet (Subject-Predicate-Description)',
                            'phrase': f"{tokens[i]} {tokens[i + 1]} {tokens[i + 2]}"
                        })
                        i += 3
                        matched = True
                        continue

            # SP (2-word pattern)
            if i < len(tokens) - 1 and not matched:
                if is_subject(tokens[i]) and is_predicate(tokens[i + 1]):
                    structures.append({
                        'type': 'SP (Subject-Predicate)',
                        'phrase': f"{tokens[i]} {tokens[i + 1]}"
                    })
                    i += 2
                    matched = True
                    continue

            # If no pattern matched, move to next token
            if not matched:
                i += 1

        return structures

    def get_noun_category(self, word):
        # Helper method to get the category of a noun
        word = word.strip('"')
        for category, words in nounCategories.items():
            if word in words:
                return category
        return None

    def parse_text(self):
        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        
        # Get input text and split into tokens
        text = self.input_text.get(1.0, tk.END).strip()
        processed_text = text.lower()
        tokens = processed_text.split()
        
        if not tokens:
            self.results_text.insert(tk.END, "No text to parse!")
            return
        
        # Find valid VPs
        valid_vps = self.is_valid_vp(tokens)
        
        # Find sentence structures
        sentence_structures = self.check_sentence_structure(tokens)
        
        if valid_vps:
            self.results_text.insert(tk.END, "Found Valid Verb Phrases:\n\n")
            for vp in valid_vps:
                self.results_text.insert(tk.END, f"Type: {vp['type']}\n")
                self.results_text.insert(tk.END, f"Phrase: {vp['phrase']}\n")
                self.results_text.insert(tk.END, "-" * 40 + "\n")
        
        if sentence_structures:
            self.results_text.insert(tk.END, "\nFound Sentence Structures:\n\n")
            for structure in sentence_structures:
                self.results_text.insert(tk.END, f"Type: {structure['type']}\n")
                self.results_text.insert(tk.END, f"Phrase: {structure['phrase']}\n")
                self.results_text.insert(tk.END, "-" * 40 + "\n")
        
        if not valid_vps and not sentence_structures:
            self.results_text.insert(tk.END, "No valid structures found!")

def main():
    root = tk.Tk()
    app = BalineseVPParser(root)
    root.mainloop()

if __name__ == "__main__":
    main()