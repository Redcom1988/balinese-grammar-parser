import tkinter as tk
from tkinter import ttk, scrolledtext

# GUI class remains the same
class BalineseSyntaxParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Balinese Syntax Parser")
        self.root.geometry("800x600")
        
        self.parser = BalineseParser()
        self.create_widgets()
        
    def create_widgets(self):
        input_frame = ttk.LabelFrame(self.root, text="Input", padding="10")
        input_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(input_frame, text="Enter Balinese sentence:").pack(anchor="w")
        self.sentence_input = ttk.Entry(input_frame, width=70)
        self.sentence_input.pack(fill="x", pady=5)
        
        ttk.Button(input_frame, text="Parse Sentence", command=self.parse_sentence).pack(pady=5)
        
        output_frame = ttk.LabelFrame(self.root, text="Parse Results", padding="10")
        output_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, height=20)
        self.output_text.pack(fill="both", expand=True)
        
    def parse_sentence(self):
        self.output_text.delete(1.0, tk.END)
        sentence = self.sentence_input.get().strip()
        
        if not sentence:
            self.output_text.insert(tk.END, "Please enter a sentence to parse.")
            return
            
        is_valid, derivation = self.parser.parse_with_derivation(sentence)
        
        if is_valid:
            self.output_text.insert(tk.END, "✅ Valid Balinese sentence\n\n")
        else:
            self.output_text.insert(tk.END, "❌ Invalid Balinese sentence\n\n")
            
        self.output_text.insert(tk.END, "Derivation steps:\n")
        for step in derivation:
            self.output_text.insert(tk.END, f"{step}\n")

class BalineseParser:
    def __init__(self):
        # Grammar rules remain the same
        self.grammar = {
            'K': [
                ['S', 'P'],
                ['S', 'P', 'O'],
                ['S', 'P', 'Pel'],
                ['S', 'P', 'Ket'],
                ['S', 'P', 'O', 'Pel'],
                ['S', 'P', 'O', 'Ket'],
                ['S', 'P', 'Pel', 'Ket'],
                ['S', 'P', 'O', 'Pel', 'Ket']
            ]
        }

        # Lexicon remains largely the same but with 'timpalne' added
        self.lexicon = {
            'Noun': [
                'titiang', 'tiang', 'putu', 'dangin', 'adik', 'tiange', 'sepedane',
                'ketua', 'pasar', 'bapakne', 'guru', 'sekolah',
                'adin', 'mahasiswa', 'ragane', 'dane', 'baju', 'bapan', 'ipune',
                'balian', 'ibu', 'matematika', 'anake', 'luh', 'pianakne', 'pak',
                'komputer', 'puspa', 'dosen', 'kampus', 'timpal', 'nasi', 'umah',
                'goreng', 'ajengan', 'sepatu', 'pasang', 'motorne', 'padi', 'memene',
                'ketut', 'bagus', 'perbekel', 'sanja', 'semengan', 'camat', 'kuta',
                'selatan', 'kantor', 'desa', 'parkir', 'pns', 'sari', 'serombotan',
                'kamar', 'olahraga', 'yogyakarta', 'surabaya', 'timpalne', 'bapane',
                'carik'
            ],
            'Verb': [
                'meblanja', 'melajah', 'megambal', 'melali', 'ngatehin', 'rauh',
                'pinaka', 'dados', 'mekarya', 'manting', 'ngajahin', 'mekarya',
                'ngatur', 'ngubadin', 'nanem', 'ngalihin', 'masepedaan', 'nganggon',
                'meli', 'ilang', 'abane', 'anggone'
            ],
            'Adj': [
                'galak', 'dueg', 'paling', 'bagus', 'seleg', 'males', 'kapah',
                'gedeg', 'becik', 'luung', 'sakti', 'jegeg', 'baru'
            ],
            'Adv': [
                'sampun', 'sesai', 'kapah', 'pisan', 'saking', 'tuni', 'semeng',
                'setata', 'akeh', 'sue', 'pesan', 'lakar'
            ],
            'Prep': [
                'ka', 'di', 'ring', 'saking', 'uli'
            ],
            'Det': [
                'punika', 'puniki', 'ento', 'nika'
            ],
            'Pronoun': [
                'ia', 'ipun', 'ragane', 'titiang', 'tiang'  
            ],
            'Num': [
                'telung', 'dadue', 'dasa', 'duang', 'lelima', 'pitung', 'limang'
            ]
        }

    def tokenize(self, sentence):
        tokens = []
        current_token = ''
        in_quotes = False
        
        for char in sentence.lower():
            if char == '"':
                if in_quotes:
                    if current_token:
                        tokens.append(f'"{current_token}"')
                        current_token = ''
                in_quotes = not in_quotes
            elif char.isspace() and not in_quotes:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
            else:
                current_token += char
                
        if current_token:
            tokens.append(current_token)
            
        return tokens

    def get_word_category(self, word, derivation):
        if word.startswith('"') and word.endswith('"'):
            derivation.append(f"Quoted phrase '{word}' recognized as Noun")
            return 'Noun'
            
        for category, words in self.lexicon.items():
            if word.strip('"') in words:
                derivation.append(f"Word '{word}' recognized as {category}")
                return category
                
        derivation.append(f"❌ Unknown word: {word}")
        return None

    def build_phrase_structure(self, categories, derivation):
        """Build phrase structure with improved compound noun and predicate handling."""
        i = 0
        while i < len(categories):
            # Handle compound nouns (e.g., "adik tiange")
            if i < len(categories) - 1:
                if categories[i] == 'Noun' and categories[i + 1] == 'Noun':
                    derivation.append(f"Combining compound noun: {categories[i]} + {categories[i + 1]} → NP")
                    categories[i:i + 2] = ['NP']
                    continue

                # Handle Adj/Adv + Verb as predicate
                if (categories[i] in ['Adj', 'Adv']) and categories[i + 1] == 'Verb':
                    derivation.append(f"Combining {categories[i]} + Verb → VP")
                    categories[i:i + 2] = ['VP']
                    continue
                
                # Handle PP formation
                if categories[i] == 'Prep':
                    if i + 2 < len(categories) and categories[i + 1] == 'Noun' and categories[i + 2] == 'Noun':
                        # Handle PPs with compound nouns
                        derivation.append(f"Combining Prep + compound noun → PP")
                        categories[i:i + 3] = ['PP']
                        continue
                    elif categories[i + 1] in ['NP', 'Noun']:
                        derivation.append(f"Combining Prep + {categories[i + 1]} → PP")
                        categories[i:i + 2] = ['PP']
                        continue

            # Basic category conversions
            if categories[i] == 'Noun':
                categories[i] = 'NP'
                derivation.append(f"Converting Noun → NP")
            elif categories[i] == 'Verb':
                categories[i] = 'VP'
                derivation.append(f"Converting Verb → VP")
            
            i += 1
        
        return categories

    def identify_sentence_parts(self, categories, derivation):
        """Identify sentence parts with improved predicate handling."""
        if len(categories) < 2:
            return None
            
        # First NP is always S
        if categories[0] in ['NP']:
            categories[0] = 'S'
            derivation.append("First NP identified as Subject (S)")
            
        # Identify predicate
        if len(categories) > 1:
            if categories[1] in ['VP', 'NP', 'Adj', 'NumP', 'PP']:
                categories[1] = 'P'
                derivation.append(f"Second constituent identified as Predicate (P)")
                
        # All remaining PPs are Ket
        for i in range(2, len(categories)):
            if categories[i] == 'PP':
                categories[i] = 'Ket'
                derivation.append(f"PP at position {i+1} identified as Keterangan (Ket)")
                    
        return categories

    def parse_with_derivation(self, sentence):
        derivation = []
        
        tokens = self.tokenize(sentence)
        derivation.append("Tokens: " + " | ".join(tokens))
        
        categories = []
        for token in tokens:
            category = self.get_word_category(token, derivation)
            if category is None:
                return False, derivation
            categories.append(category)
            
        derivation.append("\nInitial categories: " + " ".join(categories))
        
        # Build phrase structure
        categories = self.build_phrase_structure(categories, derivation)
        derivation.append("\nPhrase structure: " + " ".join(categories))
        
        # Identify sentence parts
        categories = self.identify_sentence_parts(categories, derivation)
        if not categories:
            derivation.append("\n❌ Could not identify main sentence parts")
            return False, derivation
            
        derivation.append("\nFinal structure: " + " ".join(categories))
        
        # Check if matches valid pattern
        pattern_match = False
        for pattern in self.grammar['K']:
            if len(categories) == len(pattern):
                if all(cat == exp for cat, exp in zip(categories, pattern)):
                    pattern_match = True
                    derivation.append(f"\n✅ Matches valid pattern: {' '.join(pattern)}")
                    break
                    
        if not pattern_match:
            derivation.append("\n❌ Does not match any valid sentence pattern")
            
        return pattern_match, derivation

def main():
    root = tk.Tk()
    app = BalineseSyntaxParserGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# Valid Words:
# titiang sampun meblanja                                               : Worked
# "i putu dangin" punika sesai melajah megambal                         :
# adik tiange kapah melali ka umah timpalne                             : 
# sepedane wayan darta sesai anggone ngatehin bapane ka carik           :
# ketua pasar punika sampun rauh saking tuni semeng                     :
# bapakne "i putu gede" punika pinaka guru olahraga di sekolah tiange   :
# adin tiange sampun dados mahasiswa baru ring kampus udayana jimbaran  :
# ragane sampun mekarya saking semeng pisan                             :
# dane setata manting baju akeh pisan ka tukad unda                     :
# bapan ipune sampun dados balian sakti saking sue pisan                :

# Invalid Words:
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