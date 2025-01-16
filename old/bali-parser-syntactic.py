# Valid Sentences:
# titiang sampun meblanja                                               : Worked
# "i putu dangin" punika sesai melajah megambal                         : Worked
# adik tiange kapah melali ka umah timpalne                             : 
# sepedane wayan darta sesai anggone ngatehin bapane ka carik           :
# ketua pasar punika sampun rauh saking tuni semeng                     :
# bapakne "i putu gede" punika pinaka guru olahraga di sekolah tiange   :
# adin tiange sampun dados mahasiswa baru ring kampus udayana jimbaran  :
# ragane sampun mekarya saking semeng pisan                             :
# dane setata manting baju akeh pisan ka tukad unda                     :
# bapan ipune sampun dados balian sakti saking sue pisan                :

# Invalid Sentences:
# ibu guru tiange galak pisan ngajahin matematika                       :
# anake "luh jegeg" punika dueg pisan mekarya wewantenan                :
# pianakne pak guru ento seleg pisan melajah komputer di sekolah        :
# bapakne "i putu gede" guru olahraga di sekolah tiange                 :
# ibu puspa punika dosen matematika sane jegeg ring kampus timpal tiange:
# nasi goreng punika ajengan lakar abane ka kota surabaya               :
# sepeda baru adin tiange telung pasang lakar abane ka kota surabaya    :
# sepeda motorne dadue luung pati                                       :
# bapan tiange ka carik nanem padi uli tuning semengan                  :
# memene "ketut bagus" ka yogyakarta ngatehin adine                     :

import tkinter as tk
from tkinter import ttk, scrolledtext

class BalineseSyntaxParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Balinese Syntax Parser")
        self.root.geometry("800x600")
        
        # Initialize parser
        self.parser = BalineseParser()
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Input frame
        input_frame = ttk.LabelFrame(self.root, text="Input", padding="10")
        input_frame.pack(fill="x", padx=10, pady=5)
        
        # Sentence input
        ttk.Label(input_frame, text="Enter Balinese sentence:").pack(anchor="w")
        self.sentence_input = ttk.Entry(input_frame, width=70)
        self.sentence_input.pack(fill="x", pady=5)
        
        # Parse button
        ttk.Button(input_frame, text="Parse Sentence", command=self.parse_sentence).pack(pady=5)
        
        # Output frame
        output_frame = ttk.LabelFrame(self.root, text="Parse Results", padding="10")
        output_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Results text area
        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, height=20)
        self.output_text.pack(fill="both", expand=True)
        
    def parse_sentence(self):
        self.output_text.delete(1.0, tk.END)
        sentence = self.sentence_input.get().strip()
        
        if not sentence:
            self.output_text.insert(tk.END, "Please enter a sentence to parse.")
            return
            
        # Parse the sentence
        is_valid, derivation = self.parser.parse_with_derivation(sentence)
        
        # Display results
        if is_valid:
            self.output_text.insert(tk.END, "✅ Valid Balinese sentence\n\n")
        else:
            self.output_text.insert(tk.END, "❌ Invalid Balinese sentence\n\n")
            
        self.output_text.insert(tk.END, "Derivation steps:\n")
        for step in derivation:
            self.output_text.insert(tk.END, f"{step}\n")

class BalineseParser:
    def __init__(self):
        # Grammar rules using only allowed POS
        self.grammar = {
            'K': [
                ['S', 'P', 'O', 'Pel', 'Ket'], 
                ['S', 'P', 'O', 'Pel'],     
                ['S', 'P', 'O', 'Ket'],
                ['S', 'P', 'Pel'],
                ['S', 'P', 'O'],                            
                ['S', 'P', 'Ket'],
                ['S', 'P']
            ],
            'S': [['NP']],
            'P': [['VP'], ['NP'], ['AdjP'], ['NumP'], ['PP']],
            'O': [['NP']],
            'Pel': [['NP'], ['AdjP'], ['NumP'], ['VP']],
            'Ket': [['PP']],
            
            # Phrase structure rules using only allowed POS
            'NP': [
                ['Noun'],
                ['Pronoun'],
                ['NP', 'Det'],
                ['NP', 'Adj'],  # For constructions like "mobil anyar"
                ['Noun', 'Adj'],  # Direct combination of Noun + Adj
                ['Noun', 'Pronoun'],  # For possessive constructions like "bapan ipune"
                ['Noun', 'NP'],  # For compound nouns
                ['Num', 'NP'],
                ['NP', 'Prep', 'NP'],
                ['Noun', 'Adj', 'Det'],
                ['NP', 'Adj', 'Det']
            ],
            'VP': [
                ['Verb'],
                ['Adv', 'Verb'],
                ['Verb', 'Adv'],
                ['Verb', 'NP'],
                ['Verb', 'PP'],
                ['AdjP', 'Verb'],
                ['Verb', 'AdjP'],
                ['Adv', 'VP']
            ],
            'AdjP': [
                ['Adj'],
                ['Adv', 'Adj'],
                ['Adj', 'Adv'],
            ],
            'PP': [
                ['Prep', 'NP'],
                ['Prep', 'Pronoun']
            ],
            'NumP': [
                ['Num'],
                ['Num', 'Noun']
            ]
        }
        
        self.word_categories = []
        self.np_types = []

        # Lexicon with allowed POS categories
        self.lexicon = {
            'Noun': [
                'meme', 'bapa', 'adi', 'beli', 'embok', 'pekak', 'dadong', 'rerama',
                'guru', 'murid', 'jero', 'balian', 'dewa', 'leak', 'raksasa',
                'memenne', 'bapan', 'nyama', 'nyamane', 'embokne', 'ipune',
                'umah', 'pura', 'carik', 'tegal', 'pasar', 'sekolah', 'warung',
                'jineng', 'paon', 'merajan', 'tukad', 'segara', 'gedong', 'wantilan',
                'bale', 'subak', 'sawah', 'natah', 'tembok', 'kori', 'sanggah',
                'padmasana', 'Jakarta', 'abian', 'desa', 'desane', 'toko',
                'buku', 'meja', 'kursi', 'tiuk', 'gergaji', 'komputer', 'motor',
                'jukung', 'baju', 'sepatu', 'canang', 'banten', 'topeng', 'gamelan',
                'kulkul', 'gedebong', 'tampul', 'keris', 'pangawin', 'mobil', 'pipis',
                'hadiah', 'pupur', 'kambing', 'yeh', 'bubuh', 'sumsum', 'tresna',
                'dharma', 'karma', 'suka', 'duka', 'dasar', 'negara', 'negarane',
                'koperasi', 'ketua', 'anak', 'anake', 'lanang', 'luh', 'mahasiswa',
                'made', 'dangin', 'dian', 'carikne', 'gega', 'gegaene', 'ukud', 'adik',
                'timpalne', 'ibu', 'matematika'
            ],
            
            'Verb': [
                'malajah', 'melaib', 'malaib', 'menek', 'tuun', 'teka', 'luas',
                'matulak', 'mlali', 'ngadeg', 'negak', 'melajah', 'megae', 'nulis',
                'memaca', 'ngajeng', 'minum', 'sirep', 'ngidih', 'meli', 'ngadep',
                'metakon', 'ngorahang', 'ngae', 'magarapan', 'menahin', 'magae',
                'nongos', 'makarya', 'ngigel', 'makidung', 'matembang', 'masolah',
                'mabanten', 'ngaturang', 'matetulungan', 'masayut', 'ngayah',
                'malukat', 'mapuja', 'masuryak', 'ngetis', 'maselselin', 'polih',
                'numbas', 'dados', 'pinaka', 'ngamaang', 'nyemakang', 'ngelah',
                'mekarya', 'malajah', 'ngai', 'meliang', 'pinika', 'meblanja', 'megambal',
                'melali', 'ngajahin'
            ],
            
            'Adj': [
                'gede', 'cenik', 'lantang', 'bawak', 'tegeh', 'endep', 'ageng',
                'alit', 'bunter', 'barak', 'putih', 'selem', 'kuning', 'ijo',
                'jegeg', 'bagus', 'melah', 'jelek', 'dueg', 'belog', 'becik',
                'rajin', 'males', 'seleg', 'kendel', 'takut', 'gedeg', 'demen',
                'panes', 'dingin', 'basang', 'tuh', 'belus', 'tua', 'bajang',
                'wayah', 'anyar', 'let', 'maal', 'cerik', 'liu', 'jemet', 'galak'
            ],
            
            'Adv': [
                'sesai', 'pepes', 'kapah', 'tusing', 'paling', 'jani', 'mani',
                'ibi', 'puan', 'telun', 'semengan', 'tengai', 'sanja', 'peteng',
                'nyanan', 'suud', 'suba', 'aluh', 'adeng', 'becat', 'jemet',
                'melah', 'pisan', 'sanget', 'bas', 'banget', 'bes', 'jagi', 'sampun'
            ],
            
            'Pronoun': [
                'tiang', 'icang', 'titiang', 'gelah', 'manira', 'kami', 'iraga',
                'cai', 'ragane', 'jerone', 'ida', 'ratu', 'cokor', 'palungguh',
                'ia', 'ipun', 'dane', 'ida', 'dané', 'niki', 'ene',
                'puniki', 'punika', 'ika', 'nike', 'tiange'
            ],
            
            'Num': [
                'besik', 'dua', 'telu', 'pat', 'lima', 'nem', 'pitu', 'kutus',
                'sia', 'dasa', 'kabesik', 'kadua', 'katelu', 'kapat', 'kalima',
                'padua', 'patelu', 'papitu', 'limang', 'duang'
            ],
            
            'Prep': [
                'di', 'ka', 'uli', 'ring', 'ke', 'sig', 'ba', 'beten', 'duur',
                'tengah', 'samping', 'ajeng', 'dori', 'kauh', 'kangin', 'kaja',
                'kelod', 'teken', 'sareng', 'kayang', 'nganti', 'kanti', 'olih',
                'antuk', 'manut', 'sejaba'
            ],
            
            'Det': [
                'puniki', 'punika', 'eni', 'ento', 'ene', 'nika', 'puniku',
                'nike', 'iki', 'ika'
            ]
        }

    def get_word_category(self, word):
        """Find the lexical category of a word."""
        if word.startswith('"') and word.endswith('"'):
            return 'Noun'
            
        for category, words in self.lexicon.items():
            if word.lower() in words:
                return category
        return None

    def parse_with_derivation(self, sentence):
        """Parse a sentence and return the derivation steps."""
        derivation = []
        self.np_types = []
        
        # Process custom nouns in quotes
        processed_words = []
        current_word = ""
        in_quotes = False
        
        for char in sentence:
            if char == '"':
                in_quotes = not in_quotes
                if not in_quotes:
                    processed_words.append(f'"{current_word}"')
                    current_word = ""
                continue
            if in_quotes:
                current_word += char
            elif char.isspace():
                if current_word:
                    processed_words.append(current_word)
                    current_word = ""
            else:
                current_word += char
        if current_word:
            processed_words.append(current_word)
                
        # Get word categories
        self.word_categories = []
        for word in processed_words:
            category = self.get_word_category(word)
            if category is None:
                derivation.append(f"❌ Unknown word: {word}")
                return False, derivation
            self.word_categories.append(category)
            derivation.append(f"Word '{word}' recognized as {category}")
        
        # First pass: combine phrases
        i = 0
        while i < len(self.word_categories):
            # Process three-word patterns first
            if i < len(self.word_categories) - 2:
                # Handle three-word NP (Noun + Adj + Det)
                if (self.word_categories[i] == 'Noun' and
                    self.word_categories[i + 1] == 'Adj' and
                    self.word_categories[i + 2] == 'Det'):
                    derivation.append(f"Combined: Noun + Adj + Det → NP (determined)")
                    self.word_categories[i:i + 3] = ['NP']
                    self.np_types.append((i, 'determined'))
                    continue
                # Handle PP (Prep + Noun + Pronoun)
                if (self.word_categories[i] == 'Prep' and
                    self.word_categories[i + 1] == 'Noun' and
                    self.word_categories[i + 2] == 'Pronoun'):
                    derivation.append(f"Combined: Prep + Noun + Pronoun → PP")
                    self.word_categories[i:i + 3] = ['PP']
                    self.np_types.append((i, 'compound'))
                    continue
            
            # Then process two-word patterns
            if i < len(self.word_categories) - 1:
                # Process Adv + Verb
                if (self.word_categories[i] == 'Adv' and 
                    self.word_categories[i + 1] == 'Verb'):
                    derivation.append(f"Combined: Adv + Verb → VP")
                    self.word_categories[i:i + 2] = ['VP']
                    continue
                
                # Adjective combinations
                if self.word_categories[i] == 'Adj':
                    if self.word_categories[i + 1] == 'Adv':
                        derivation.append(f"Combined: Adj + Adv → AdjP")
                        self.word_categories[i:i + 2] = ['AdjP']
                        continue
                
                # Noun combinations
                if self.word_categories[i] == 'Noun':
                    if (i + 2 >= len(self.word_categories) or self.word_categories[i + 2] != 'Noun') and self.word_categories[i + 1] == 'Verb':
                        derivation.append(f"Combined: Noun + Verb → NP (compound)")
                        self.word_categories[i:i + 2] = ['NP']
                        self.np_types.append((i, 'compound'))
                        continue
                    elif self.word_categories[i + 1] == 'Noun':
                        derivation.append(f"Combined: Noun + Noun → NP (compound)")
                        self.word_categories[i:i + 2] = ['NP']
                        self.np_types.append((i, 'compound'))
                        continue
                    elif (i + 2 >= len(self.word_categories) or self.word_categories[i + 2] != 'Adv') and self.word_categories[i + 1] == 'Adj':
                        derivation.append(f"Combined: Noun + Adj → NP (modified)")
                        self.word_categories[i:i + 2] = ['NP']
                        self.np_types.append((i, 'modified'))
                        continue
                    elif self.word_categories[i + 1] == 'Pronoun':
                        derivation.append(f"Combined: Noun + Pronoun → NP (determined)")
                        self.word_categories[i:i + 2] = ['NP']
                        self.np_types.append((i, 'determined'))
                        continue
                
                # Number combinations
                if self.word_categories[i] == 'Num':
                    if self.word_categories[i + 1] == 'Noun':  # Changed from 'Unit' to handle classifiers
                        derivation.append(f"Combined: Num + Noun → NumP")
                        self.word_categories[i:i + 2] = ['NumP']
                        continue
                
                # Preposition combinations
                if self.word_categories[i] == 'Prep':
                    if self.word_categories[i + 1] in ['Noun', 'NP']:
                        derivation.append(f"Combined: Prep + Noun → PP")
                        self.word_categories[i:i + 2] = ['PP']
                        continue
                
            # Convert single categories to phrases where appropriate
            if self.word_categories[i] == 'Verb':
                derivation.append(f"Combined: Verb → VP")
                self.word_categories[i:i + 1] = ['VP']
            elif self.word_categories[i] == 'Noun':
                derivation.append(f"Combined: Noun → NP")
                self.word_categories[i:i + 1] = ['NP']
                self.np_types.append((i, 'basic'))  # Maintain tuple structure
                
            i += 1

        # Try to match pattern
        for pattern in self.grammar['K']:
            derivation.append(f"\nAttempting to match pattern: {' '.join(pattern)}")
            
            # Skip patterns that don't match the length of our word categories
            if len(self.word_categories) != len(pattern):
                continue
                
            # Try to match the current pattern
            match = True
            temp_categories = self.word_categories.copy() 
            
            for i, (cat, target) in enumerate(zip(temp_categories, pattern)):
                if not self._can_derive_with_steps(cat, target, i, derivation):
                    match = False
                    break
                    
            if match:
                derivation.append(f"✓ Matches valid pattern: {' '.join(pattern)}")
                return True, derivation

        derivation.append("\n❌ Does not match any valid sentence pattern")
        return False, derivation

    def _try_pattern_match(self, categories, pattern, derivation):
        """Try to match a specific pattern."""
        if len(categories) != len(pattern):
            return False
            
        for i, (cat, target) in enumerate(zip(categories, pattern)):
            if cat == target:
                continue
                
            # Try deriving current category to target
            if target == 'S':
                if cat in ['Noun', 'NP']:
                    derivation.append(f"Derivation: {cat} → NP → S")
                    categories[i] = 'S'
                    continue
            elif target == 'P':
                if cat in ['Verb', 'VP']:
                    derivation.append(f"Derivation: {cat} → P")
                    categories[i] = 'P'
                    continue
                    
            return False
            
        return True

    def _check_pattern_with_derivation(self, word_categories, pattern, derivation):
        """Check if word categories match the pattern."""
        if len(word_categories) != len(pattern):
            return False
            
        derivation.append("\nAttempting to match pattern: " + " ".join(pattern))
        
        for i, (word_cat, pattern_cat) in enumerate(zip(word_categories, pattern)):
            if not self._can_derive_with_steps(word_cat, pattern_cat, i, derivation):
                return False
                
        return True

    def _can_derive_with_steps(self, current_category, target_category, position, derivation):
        """Enhanced derivation checking with all Balinese sentence patterns."""
        current_np_type = None
        for pos, np_type in self.np_types:
            if pos == position:
                current_np_type = np_type
                break

        # Direct match
        if current_category == target_category:
            derivation.append(f"Direct match: {current_category} → {target_category}")
            return True
                
        # NP derivations
        if target_category == 'NP':
            if current_category in ['Pronoun', 'Noun']:
                derivation.append(f"Derivation: {current_category} → NP")
                return True
                
        # Subject derivations
        if target_category == 'S':
            if current_category in ['Pronoun', 'Noun', 'NP']:
                derivation.append(f"Derivation: {current_category} → NP → S")
                return True
                
        # Predicate derivations
        if target_category == 'P':
            if current_category in ['Verb', 'VP', 'AdjP']:
                derivation.append(f"Derivation: {current_category} → P")
                return True
                    
        # Object derivations
        if target_category == 'O':
            if current_category == 'NP':
                if current_np_type in ['determined', 'modified']:
                    derivation.append(f"Derivation: {current_np_type} NP → O")
                    return True
                elif current_np_type == 'basic':
                    derivation.append(f"Derivation: basic NP → O")
                    return True

        # Pelengkap derivations        
        if target_category == 'Pel':
            if current_category == 'NP':
                # Check if it's a `compound` type NP
                if current_np_type == 'compound':
                    derivation.append(f"Derivation: compound NP → Pel")
                    return True
                # Explicitly resolve the ambiguity for `modified` NP
                elif current_np_type == 'basic':
                    derivation.append(f"Derivation: basic NP → Pel")
                    return True
                elif current_np_type == 'modified':
                    if self.resolve_modified_np_conflict(position):
                        derivation.append(f"Derivation: modified NP → Pel")
                        return True
                    else:
                        derivation.append(f"Derivation conflict: modified NP not resolved as Pel")
                        return False
            elif current_category == 'NumP':
                derivation.append(f"Derivation: NumP → Pel")
                return True
            elif current_category == 'VP':
                derivation.append(f"Derivation: VP → Pel")
                return True
            elif current_category == 'AdjP':
                derivation.append(f"Derivation: AdjP → Pel")
                return True

                
        # Keterangan (adverb) derivations
        if target_category == 'Ket':
            if current_category in ['PP', 'AdjP']:
                derivation.append(f"Derivation: {current_category} → Ket")
                return True
                
        return False
    
    def resolve_modified_np_conflict(self, position):
        """
        Resolve ambiguity for modified NP. 
        Returns True if it should derive to Pel, False otherwise.
        """
        # Example heuristic: Check surrounding word categories or other criteria
        if position > 0 and self.word_categories[position - 1] in ['Verb', 'VP']:
            # If preceded by a Verb/VP, likely to be Pelengkap
            return False
        if position < len(self.word_categories) - 1 and self.word_categories[position + 1] in ['Prep', 'PP']:
            # If followed by Prep/PP, likely not Pelengkap
            return True
        # Default decision
        return True


def main():
    root = tk.Tk()
    app = BalineseSyntaxParserGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()