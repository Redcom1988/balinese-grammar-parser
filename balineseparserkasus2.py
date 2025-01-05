import tkinter as tk
from tkinter import ttk, messagebox
import re

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

        # Extended word categories
        self.words = {
            'Noun': [
                'liat', 'laib', 'adeg', 'ater', 'ider', 'ayah', 'uruk', 'arep', 'ibing', 'arit',
                'gergaji', 'rauh', 'ukir', 'tegul', 'tebus', 'beli', 'iket', 'tampi', 'uber',
                'gebug', 'kucit', 'kusir', 'togog', 'umah', 'dewa', 'pura', 'meme', 'adi',
                'tiuk', 'leak', 'raksasa', 'jukut', 'motor', 'jukung', 'emas',
                'jaring', 'uyah', 'sate', 'cedok', 'cekalan', 'kursi', 'gunung', 'angin',
                'keneh', 'sepatu', 'baju', 'tanah', 'kayu', 'atma', 'bunyi', 'suarga',
                'neraka', 'alas', 'dharma', 'taksu', 'sukerta', 'genta', 'pelawa', 'tedung',
                'guru', 'pandita', 'raja', 'teben', 'jineng', 'setra', 'tukad', 'segara',
                'canang', 'bhuana', 'bale', 'sanggah', 'pelinggih', 'natah', 'merajan', 'subak', 'carik',
                'tenget', 'balian', 'pecalang', 'kulkul', 'gamelan', 'gender', 'rindik',
                'canangsari', 'banten', 'sesajen', 'kober', 'umbul-umbul', 'gebogan',
                'pecaruan', 'padmasana', 'panggungan', 'gedong', 'paon', 'tembok',
                'lelangit', 'bantang', 'tulang', 'kulit', 'getih', 'lengen', 'lima',
                'jeroan', 'kelapa', 'base', 'don', 'bunga', 'woh', 'padang', 'abing',
                'tegal', 'uma', 'sema', 'pura', 'mrajan', 'jaba', 'kaja', 'kelod',
                'kangin', 'kauh', 'bebanten', 'tirta', 'yadnya', 'penjor', 'layangan', 'baju', 'badung',
                'sanglah', 'pasar', 'warung', 'jalikan', 'ketipat', 'jaja', 'arak', 'tuak', 
                'payuk', 'panci', 'semprong', 'kompor', 'siap', 'sampi', 'celeng', 'bangkung',
                'bikul', 'lelipi', 'katak', 'kedis', 'siap', 'bebek', 'meong', 'cicing',
                'punyan', 'entik', 'biu', 'poh', 'nangka', 'durian', 'salak', 'wani',
                'bingin', 'kepuh', 'delima', 'sumaga', 'jeruk', 'belimbing', 'nyuh',
                'jagung', 'padi', 'kacang', 'ketela', 'kesela', 'tabia', 'bawang',
                'jahe', 'kunyit', 'lengkuas', 'cengkeh', 'pala', 'kemiri', 'kayu'
            ],
            'Verb': [
                'melajah', 'megae', 'maplalian', 'nulis', 'memaca', 'melaib', 'mejalan',
                'negak', 'megedi', 'ulung', 'ngajeng', 'minum', 'teka', 'atoang', 'menek',
                'ngaturang', 'muspa', 'mabanten', 'ngayah', 'metanding', 'ngigel', 'makekawin',
                'makidung', 'nganteb', 'ngaturang', 'mategen', 'malayang', 'nanding',
                'ngastawa', 'masemayut', 'ngarga', 'ngamel', 'ngoton', 'masolah', 'ngocek',
                'nyurat', 'ngukir', 'nyangih', 'ngigel', 'mesuara', 'nganggit', 'ngepung',
                'majalan', 'merebah', 'mebikas', 'mekamben', 'mesaput', 'ngaturang',
                'ngayah', 'metajen', 'megambel', 'megending', 'mekumpul', 'mebanten',
                'mekarya', 'ngadol', 'numbas', 'madaar', 'ngidih', 'nyilih', 'ngutang',
                'ngadep', 'ngisidang', 'mesuun', 'negul', 'ningalin', 'ngerasang', 
                'ngajeng', 'nguberin', 'numbas', 'nongos', 'ajak',
                'ngigel', 'ngebah', 'nyangkol', 'nuturang', 'ngenah', 'ningeh', 'ngadek',
                'ngecap', 'ngetel', 'ngutang', 'nyemak', 'ngejang', 'nyemak', 'ngaba',
                'ngateh', 'nyarup', 'ngecum', 'nginem', 'ngajeng', 'medaar', 'masare',
                'medem', 'bangun', 'matangi', 'makecos', 'makecog', 'makejer', 'magebur',
                'majemuh', 'ngendih', 'ngenyat', 'ngedum', 'ngigel', 'ngecek', 'ngraos',
                'matutur', 'masesandan', 'makeengan', 'makisid', 'makeber', 'nglayang',
                'nyiksik', 'nyangket', 'ngejer', 'ngebug', 'nglungo', 'majalan', 'melaib',
                'nglangi', 'ngeling'
            ],
            'Adj': [
                'alus', 'becik', 'bagus', 'endah', 'gede', 'luas', 'lemah', 'sugih', 'dueg',
                'siteng', 'kenyel', 'banyol', 'mayus', 'ajum', 'bedak', 'seduk', 'betek', 'jaen',
                'barak',
                'ayu', 'jegeg', 'bagus', 'kasub', 'wayah', 'nguda', 'tua', 'bajang',
                'lacur', 'sukil', 'melah', 'jele', 'suci', 'leteh', 'pingit', 'umum',
                'tenget', 'angker', 'sakti', 'wisesa', 'weruh', 'wikan', 'pradnyan',
                'tambet', 'belog', 'ririh', 'jemet', 'mayus', 'demen', 'gedeg', 'sebet',
                'liang', 'emed', 'seleg', 'anteng', 'ramé', 'suung', 'tegeh', 'endep',
                'lantang', 'bawak', 'linggah', 'cupit', 'teleb', 'dayuh', 'anyar',
                'suba', 'tusing', 'nenten', 'lungha', 'rauh', 'peteng', 'galang',
                'jelek', 'beneh', 'patut', 'demen', 'gedeg', 'sebet', 'emed', 'nguda',
                'tua', 'wayah', 'rare', 'cerik', 'kelih', 'gede', 'cenik', 'mokoh',
                'berag', 'keras', 'aluh', 'keren', 'lanying', 'demen', 'jengah', 'sungsut',
                'inguh', 'ibuk', 'sengsara', 'bagia', 'lascarya', 'kejem', 'galak',
                'someh', 'ramah', 'darma', 'adil', 'polos', 'jujur', 'dusta', 'lengit',
                'ilang', 'telah', 'rumpuh', 'seger', 'kebus', 'dingin', 'nyem', 'jemet',
                'males', 'kirangan', 'tabah'
            ],
            'Adv': [
                'kapah', 'sesai', 'dibi', 'benjang', 'kejep', 'tuni', 'puan', 'nyanan',
                'jani', 'semengan', 'tengai', 'sanja', 'wengi',
                'mangkin', 'durung', 'sampun', 'dados', 'nénten', 'gelis', 'alon',
                'becik', 'payu', 'malu', 'sekat', 'uwug', 'rihin', 'pegat', 'telat',
                'enggal', 'serod', 'selid', 'tutug', 'lantas', 'malih', 'kewala',
                'nanghing', 'sakadi', 'minab', 'munguin', 'sasidan', 'wiakti', 'yakti',
                'sajawi', 'sadurung', 'sampunika', 'sapunika', 'asapunika', 'sapunapi',
                'asapunapi', 'menawi', 'meneng', 'meled', 'ngiring', 'dumun', 'mangda',
                'mangkin', 'raris', 'wusan', 'gelis', 'wawu', 'kantun', 'sampun', 'dados',
                'durung', 'kapah', 'malih',
                'nadaksara', 'prajani', 'gelis-gelis', 'alon-alon', 'adeng-adeng',
                'sai-sai', 'pepes', 'terus', 'lantas', 'malih', 'buin', 'suba', 'mara',
                'wau', 'sampun', 'durung', 'nenten', 'ten', 'tusing', 'ngiring', 'dados',
                'bisa', 'prasida', 'mampuh', 'nyidayang', 'sabenehne', 'sayuwakti',
                'sajatine', 'sujatine', 'wiakti', 'sekadi', 'minakadi', 'kadi', 'sakadi',
                'pateh', 'patuh', 'soroh', 'minab', 'jenenga', 'pepes', 'ping', 'wantah',
                'wenten', 'sampun', 'kantun', 'ngararis', 'raris', 'mangkin', 'benjang',
            ],
            'Prep': [
                'ring', 'ba', 'ka', 'saking', 'uli', 'duk', 'olih',
                'di', 'ke', 'uli', 'sig', 'saking', 'antuk', 'ring', 'maring', 'marep',
                'ngajeng', 'duri', 'beten', 'duur', 'tengah', 'samping', 'sisi', 'jaba',
                'jeroan', 'kelod', 'kaja', 'kangin', 'kauh', 'tengahan', 'sisin', 'sedin',
                'bucun', 'diwangan', 'sajabaning', 'sajeroning', 'ring ajeng', 'ring duri',
                'ring tengah', 'ring sisin', 'ring bucun', 'ka jaba', 'ka jeroan',
                'saking jaba', 'saking jeroan', 'olih ring', 'rauh ring', 'kantos ring',
                'ngantos ring', 'sadurung ring', 'sasampun ring', 'sajabaning ring',
                'sajeroning ring', 'sane ring', 'sane maring', 'sane antuk', 'ring', 'di',
                'margi', 'ngangin', 'ngauh', 'ngaja', 'ngelod', 'menek', 'tuun',
                'kebet', 'kelawan', 'sareng', 'teken', 'ajak', 'kayang', 'kanti',
                'sambil', 'sedekan', 'sedek', 'risedek', 'rikala', 'dugase', 'dugas',
                'daweg', 'ritatkala', 'olih', 'antuk', 'ring', 'maring', 'sareng',
                'teken', 'ajak', 'ngajak', 'bareng', 'ngiring', 'sameton', 'nyama',
                'braya', 'kulawarga', 'kadang', 'wargi', 'arsa', 'sumeken', 'ngajengn',
                'sajeroning', 'tengahing', 'saking', 'ngawit', 'kayang', 'rauh', 'ring'
            ],
            'Pronoun': [
                'tiang', 'cang', 'iragane', 'ci', 'ia', 'ida', 'nyane', 'kami', 'iraga',
                'idane', 'dane', 'niki', 'nenten', 'nikanne', 'ikane', 'sapa', 'sapunapi',
                'puniki', 'punapi', 'titiang', 'icang', 'kai', 'jerone', 'ragane', 'gusi',
                'cai', 'iba', 'ipun',
                'gelah', 'dewek', 'awakne', 'ida-dane', 'sira', 'ipun-ipun', 'rerama',
                'okane', 'putrane', 'okan-okane', 'putran-putrane', 'ragan-ragane',
                'sami', 'samian', 'samiyan', 'sinamian', 'parasida', 'parasami',
                'parajana', 'parajanma', 'parajero', 'parasane', 'paranirane',
                'parasapasira', 'parasapasami', 'puniki', 'punika', 'puniku', 'punikine',
                'punikane', 'punikune', 'niki', 'nika', 'niku', 'nikine', 'nikane',
                'nikune', 'ene', 'ento', 'anu', 'ane', 'ne', 'to', 'niki-nika',
                'puniki-punika', 'sira-sira', 'sapasira', 'sapasami', 'sapunapi-sapunapi',
                'manira', 'gelah', 'nira', 'ira', 'ratu', 'cokor', 'palungguh',
                'dane', 'ipun', 'rerama', 'meme', 'bapa', 'biang', 'aji', 'bibi',
                'uwa', 'pekak', 'dadong', 'kakiang', 'niang', 'embok', 'beli',
                'misan', 'mindon', 'kumpi', 'buyut', 'canggah', 'wareng', 'kelab',
                'uduh', 'klabang', 'gantung', 'siwer', 'ratu', 'dewa', 'betara',
                'widhi', 'hyang', 'ida', 'dané', 'ragané', 'ipun', 'titiang',
                'iragang', 'gelahé', 'awakné', 'dewekné', 'ragané', 'idané'
            ]
        }

        self.setup_gui()

    def setup_gui(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input section with example
        ttk.Label(main_frame, text="Enter Balinese Sentence (use \"\" for names):").grid(row=0, column=0, sticky=tk.W)
        self.input_text = ttk.Entry(main_frame, width=60)
        self.input_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

        # Parse button
        ttk.Button(main_frame, text="Parse Sentence", command=self.parse_sentence).grid(row=2, column=0, pady=10)

        # Result section
        ttk.Label(main_frame, text="Parsing Result:").grid(row=3, column=0, sticky=tk.W)
        self.result_text = tk.Text(main_frame, height=20, width=80, wrap=tk.WORD)
        self.result_text.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))

        # Example section
        ttk.Label(main_frame, text="Example sentences:").grid(row=5, column=0, sticky=tk.W, pady=(10,0))
        examples = """
        1. "Rama" ngajeng (Rama makan)
        2. "Adika" nguberin layangan (Adika mengejar layangan)
        3. "Made" numbas baju ring "Kadek" (Made membeli baju dari Kadek)
        4. "Upin" kapah nongos di Badung (Upin jarang tinggal di Badung)
        """
        ttk.Label(main_frame, text=examples).grid(row=6, column=0, sticky=tk.W)

    def extract_words_and_names(self, sentence):
        """
        Extract words and names from the sentence, treating quoted text as names.
        Returns a list of tuples (word, is_name).
        """
        # Pattern to match either:
        # 1. A quoted string (name)
        # 2. A regular word (non-whitespace characters)
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
                    
                if component in self.grammar:
                    matched = False
                    for expansion in self.grammar[component]:
                        if remaining_categories[0] in expansion.split():
                            matched = True
                            current_pattern.append(component)
                            remaining_categories.pop(0)
                            break
                    
                    if not matched:
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
            
            # Show the role of each word
            self.result_text.insert(tk.END, "\nWord roles:\n")
            for word, category in zip(original_words, categories):
                role = ''
                if category == 'Name':
                    if categories.index(category) == 0:
                        role = 'Subject'
                    elif matching_pattern.split()[1] == 'P' and categories.index(category) == 2:
                        role = 'Object'
                    else:
                        role = 'Complement'
                else:
                    role = category
                self.result_text.insert(tk.END, f"{word}: {role}\n")
        else:
            self.result_text.insert(tk.END, "No valid sentence structure found.\n")
            self.result_text.insert(tk.END, "Please check the grammar rules and word order.\n")

    def categorize_word(self, word):
        """Categorize a regular word (non-name)"""
        for category, words in self.words.items():
            if word.lower() in words:
                return category
        return None

def main():
    root = tk.Tk()
    app = BalineseParserGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()