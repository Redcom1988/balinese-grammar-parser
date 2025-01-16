# Valid Sentences:
# titiang sampun meblanja                                               : 
# i putu dangin punika sesai melajah megambal                         :
# adik tiange kapah melali ka umah timpalne                             : 
# sepedane wayan darta sesai anggone ngatehin bapane ka carik           : 
# ketua pasar punika sampun rauh saking tuni semeng                     : 
# bapakne i putu gede punika pinaka guru olahraga di sekolah tiange   : 
# adin tiange sampun dados mahasiswa baru ring kampus udayana jimbaran  : 
# ragane sampun mekarya saking semeng pisan                             : 
# dane setata manting baju akeh pisan ka tukad unda                     : 
# bapan ipune sampun dados balian sakti saking sue pisan                : 

# Invalid Sentences:
# ibu guru tiange galak pisan ngajahin matematika                       : 
# anake luh jegeg punika dueg pisan mekarya wewantenan                : 
# pianakne pak guru ento seleg pisan melajah komputer di sekolah        : 
# bapakne i putu gede guru olahraga di sekolah tiange                 : 
# ibu puspa punika dosen matematika sane jegeg ring kampus timpal tiange: 
# nasi goreng punika ajengan sane paling demenin tiang            : 
# sepeda baru adin tiange telung pasang lakar abane ka kota surabaya    : 
# sepeda motorne dadue luung pati                                       : 
# bapan tiange ka carik nanem padi uli tuning semengan                  : 
# memene ketut bagus ka yogyakarta ngatehin adine                     : 

# Valid Sentences:
# (S) titiang  (P) sampun meblanja                                               : Worked
# (S) "i putu dangin" punika  (P) sesai melajah  (O)megambal                         : Worked
# (S) adik tiange (P) kapah melali (Ket) ka umah timpalne                             : 
# (S) sepedane wayan darta (P) sesai anggone (Pel) ngatehin bapane (Ket) ka carik           : 
# (S) ketua pasar punika (P) sampun rauh (Ket) saking tuni semeng                     : 
# (S) bapakne "i putu gede" punika (P) pinaka (Pel) guru olahraga (Ket) di sekolah tiange   : 
# (S) adin tiange (P) sampun dados (Pel) mahasiswa baru (Ket) ring kampus udayana jimbaran  : 
# (S) ragane (P) sampun mekarya (Ket) saking semeng pisan                             : 
# (S) dane (P) setata manting (O) baju akeh pisan (Ket) ka tukad unda                     : 
# (S) bapan ipune (P) sampun dados (Pel) balian sakti (Ket) saking sue pisan                : 

# Invalid Sentences:
# (S) ibu guru tiange (P) galak pisan (Pel) ngajahin matematika                       : 
# (S) anake "luh jegeg" punika (P) dueg pisan (Pel) mekarya wewantenan                : 
# (S) pianakne pak guru ento (P) seleg pisan (Pel) melajah komputer (Ket) di sekolah        : 
# (S) bapakne "i putu gede" (P) guru olahraga (Ket) di sekolah tiange                 : 
# (S) ibu puspa punika (P) dosen matematika (Pel) sane jegeg (Ket) ring kampus timpal tiange: 
# (S) nasi goreng punika (P) ajengan (Pel) sane paling demenin tiang               : 
# (S) sepeda baru adin tiange (P) telung pasang (Pel) lakar abane (Ket) ka kota surabaya    : 
# (S) sepeda motorne (P) dadue (Pel) luung pati                                       : 
# (S) bapan tiange (P) ka carik (Pel) nanem padi (Ket) uli tuning semengan                  : 
# (S) memene "ketut bagus" (P) ka yogyakarta (Pel) ngatehin adine                     : 

import tkinter as tk
from tkinter import scrolledtext
import re

class BalineseParser:
    def __init__(self):
        # Grammar rules for Balinese language
        grammar_str = """
            K -> S P | S P Pel | S P Ket | S P Pel Ket
            S -> NP
            P -> PP | VP
            Pel -> VP | NP | Aux Adv | Aux NP
            Ket -> PP | Adv
            NP -> Noun | PropNoun | Pronoun | NP Noun | NP PropNoun | NP Pronoun | Det NP | NP Det | NP Adj | NP PP
            PP -> Prep NP | Prep Adv | PP NumP | PP Adv
            VP -> Verb | Verb VP | Verb NP | Adv VP | Aux VP | Aux Verb
            NumP -> Num | NumP NP | NP NumP
            
            Prep -> 'ka' | 'uli' | 'di' | 'saking' | 'ring' | 'uling' | 'ke'
            Aux -> 'dados' | 'sebilang' | 'prasida' | 'dadi' | 'sesai' | 'sampun' | 'pisan' | 'paling' | 'sane' | 'setata' | 'kapah' | 'lakar'
            Adv -> 'tuni' | 'semengan' | 'ibi' | 'sanja' | 'taun' | 'wai' | 'semeng' | 'peteng' | 'sue' | 'akeh' | 'seleg' | 'dueg' | 'galak'
            Noun -> 'carik' | 'padi' | 'sekolah' | 'sepeda' | 'kantor' | 'desa' | 'kampus' | 'tukang' | 'desan' | 'pasar' | 'dosen' | 'nasi' | 'ajengan' | 'siap' | 'ukud' | 'diri' | 'umah' | 'tingkat' | 'kamarne' | 'matematika' | 'komputer' | 'baju' | 'tukad' | 'balian' | 'mahasiswa' | 'wewantenan' | 'sepedane' | 'motorne' | 'goreng' | 'pasang' | 'kota'
            PropNoun -> 'ketut' | 'bagus' | 'yogyakarta' | 'perbekel' | 'guru' | 'camat' | 'kuta' | 'selatan' | 'jimbaran' | 'parkir' | 'pns' | 'luh' | 'sari' | 'serombolan' | 'wayan' | 'darta' | 'ketua' | 'putu' | 'dangin' | 'gede' | 'udayana' | 'unda' | 'puspa' | 'surabaya'
            Pronoun -> 'bapan' | 'bapak' | 'bu' | 'pak' | 'adin' | 'titiang' | 'ia' | 'timpal-timpal' | 'kulawarga' | 'ibu' | 'timpal' | 'memen' | 'tiange' | 'memene' | 'adine' | 'pianakne' | 'bapane' | 'bapakne' | 'ragane' | 'dane' | 'ipune' | 'anake'
            Det -> 'i' | 'punika' | 'pinaka' | 'ento'
            Adj -> 'selem' | 'demenin' | 'becik' | 'luung' | 'jegeg' | 'jegeg-jegeg' | 'sakti' | 'baru'
            Verb -> 'nanem' | 'ngatehin' | 'ngalihin' | 'melajah' | 'masepedaan' | 'nganggon' | 'meli' | 'anggone' | 'rauh' | 'ngatur' | 'meblanja' | 'megambal' | 'melali' | 'mekarya' | 'manting' | 'ngajahin' | 'abane'
            Num -> '2020' | 'pitung' | 'telung' | 'limang' | 'dadue'
        """
        
        self.grammar = {}
        self.terminals = set()
        self.non_terminals = set()
        
        # Parse the grammar
        for line in grammar_str.strip().split('\n'):
            line = line.strip()
            if line:
                lhs, rhs = line.split('->')
                lhs = lhs.strip()
                self.non_terminals.add(lhs)
                
                if lhs not in self.grammar:
                    self.grammar[lhs] = []
                    
                for prod in rhs.split('|'):
                    symbols = [s.strip().strip("'") for s in prod.strip().split()]
                    self.grammar[lhs].append(symbols)
                    for symbol in symbols:
                        if symbol.startswith("'") or symbol.endswith("'"):
                            self.terminals.add(symbol.strip("'"))

    def cyk_parse(self, sentence):
        # Handle quoted text
        def replace_quoted_text(match):
            return match.group(0).strip('"').replace(' ', '_')
        
        processed_sentence = re.sub(r'"[^"]*"', replace_quoted_text, sentence)
        words = processed_sentence.lower().split()
        n = len(words)
        
        # Initialize parsing table
        table = [[set() for _ in range(n - j)] for j in range(n)]
        
        # Fill in terminal rules
        for i in range(n):
            word = words[i]
            for nt, rules in self.grammar.items():
                for rule in rules:
                    if len(rule) == 1 and rule[0] == word:
                        table[0][i].add(nt)
        
        # Fill in non-terminal rules
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    for nt, rules in self.grammar.items():
                        for rule in rules:
                            if len(rule) == 2:
                                B, C = rule
                                if B in table[k-i][i] and C in table[j-k-1][k+1]:
                                    table[l-1][i].add(nt)
        
        # Format the parsing table for display
        result = "CYK Parsing Table:\n\n"
        for i in range(n-1, -1, -1):
            for j in range(n-i):
                cell_content = ', '.join(sorted(table[i][j])) if table[i][j] else '∅'
                result += f"{cell_content:<20}"
            result += "\n"
        
        result += f"\nInput sentence: {' '.join(words)}\n"
        result += f"\nResult: {'Valid' if 'K' in table[n-1][0] else 'Invalid'} sentence"
        
        return result

class SimpleParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Balinese Parser")
        self.parser = BalineseParser()
        
        # Create GUI elements
        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Input area
        input_frame = tk.Frame(frame)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(input_frame, text="Enter sentence:").pack(side=tk.LEFT)
        self.input_text = tk.Entry(input_frame, width=60)
        self.input_text.pack(side=tk.LEFT, padx=5)
        tk.Button(input_frame, text="Parse", command=self.parse).pack(side=tk.LEFT)
        
        # Output area
        self.output_text = scrolledtext.ScrolledText(frame, height=20, width=80)
        self.output_text.pack(fill=tk.BOTH, expand=True)

    def parse(self):
        sentence = self.input_text.get()
        if sentence:
            result = self.parser.cyk_parse(sentence)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, result)

def main():
    root = tk.Tk()
    app = SimpleParserGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()