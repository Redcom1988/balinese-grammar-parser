import re
from typing import List, Dict, Set, Tuple
import logging
from datetime import datetime

# Configure logging
def setup_logging():
    """Configure logging with both file and console handlers."""
    # Create a unique log filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_filename = f'balinese_parser_{timestamp}.log'
    
    # Configure the root logger
    logger = logging.getLogger('BalineseParser')
    logger.setLevel(logging.DEBUG)
    
    # Create file handler
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

class BalineseParserRevised:
    def __init__(self):
        # Initialize logger
        self.logger = logging.getLogger('BalineseParser')
        self.logger.info("Initializing Balinese Parser")

        # Define the grammar rules exactly as specified
        self.grammar_rules = {
            # Sentence-level rules (K)
            'K': {
                ('S', 'P', 'Pel', 'O'),
                ('S', 'P', 'Pel', 'Ket'),
                ('S', 'P', 'Ket'),
                ('S', 'P', 'O', 'Ket'),
                ('S', 'P', 'O', 'Pel'),
                ('S', 'P', 'O'),
                ('S', 'P', 'Ket'),
                ('S', 'P')
            },
            
            # Main component rules
            'S': {('NP',)},
            'P': {('VP',)},
            'O': {('NP',)},
            'Pel': {('NP',), ('VP',)},
            'Ket': {('NP',), ('VP',), ('NumP',)},
            
            # Phrase structure rules
            'NP': {
                ('Noun',),
                ('PropNoun',),
                ('Pronoun',),
                ('NP', 'Noun'),
                ('NP', 'PropNoun'),
                ('NP', 'Pronoun'),
                ('NP', 'Verb'),
                ('Adv', 'NP'),
                ('Noun', 'Adv', 'Adv'),
                ('PP',),
                ('Adj', 'NP'),
                ('NP', 'Adj')
            },
            
            'VP': {
                ('Verb',),
                ('Verb', 'NP'),
                ('Prep', 'VP'),
                ('VP', 'Prep'),
                ('AdjP', 'VP'),
                ('Verb', 'Adj'),
                ('Adv', 'Verb')
            },
            
            'PP': {
                ('Prep', 'NP'),
                ('Prep', 'Adj')
            },
            
            'AdjP': {
                ('Adj',),
                ('Adv', 'Adj')
            },
            
            'NumP': {
                ('Prep', 'Num', 'NP'),
                ('Num',),
                ('Num', 'Noun')
            }
        }
        
        # Define terminal symbols (words) for each category
        self.terminals = {
            'Noun': {
                'aji', 'semengan', 'tugas', 'gendingan', 'kamarnyane', 'pakaryan',
                'tugas', 'biang', 'sepatu', 'semeton', 'makesami', 'perusahaan',
                'tegal', 'beburon', 'jinah', 'semester', 'bulane', 'benjang',
                'penyadane', 'daftar', 'pakaryan', 'ajah-ajahan', 'nasi', 'goreng',
                'carang', 'kayu', 'pabalihan', 'horor', 'kuaca', 'boneka', 'trewelu',
                'matematika', 'bola', 'benjang', 'gajih', 'kantornyane', 'pangenah',
                'agra', 'giri', 'korban', 'makesami', 'genah', 'parindikan', 'tu',
                'biang', 'ajengan', 'bekel', 'adi', 'okan', 'dane', 'istri', 'taban',
                'ibu', 'guru', 'sisiane', 'bapak', 'kepala', 'sekolah', 'pawarah-warah',
                'aji', 'dumunan', 'ratu', 'peranda', 'sarenan', 'baler', 'pak',
                'camat', 'wantuan', 'krama', 'dayu', 'mangkin', 'ica'
            },
            'PropNoun': {
                'nina', 'jeno', 'dito', 'gita', 'sinta', 'andi', 'rani', 'rina'
            },
            'Pronoun': {
                'iraga', 'tiang', 'ragane', 'punika', 'nika', 'idane', 'ida', 'ipun'
            },
            'Adv': {
                'kari', 'sane', 'jagi', 'patut', 'wikan', 'prasida', 'dados',
                'nenten', 'durung', 'sampun', 'tur', 'kantun'
            },
            'Adj': {
                'baru', 'singkat', 'keras', 'tua', 'hangat', 'baik', 'lama',
                'miskin', 'santai', 'dekat', 'rapi', 'rapat'
            },
            'Prep': {
                'ring', 'ka', 'ke', 'para', 'majeng'
            },
            'Verb': {
                'mekarya', 'ngaryaning', 'mirengang', 'ngemolihang', 'muput',
                'kaatur', 'numbasang', 'adung', 'lunga', 'malajah', 'naurin',
                'nyatetin', 'mandakin', 'nyakan', 'ngetep', 'mabalih', 'numbas',
                'megending', 'arep', 'kelas', 'maduwe', 'muput', 'karya', 'nyumu',
                'palalianan', 'ngemolihang', 'kaevakuasi', 'ngardiang', 'ngaksi',
                'rabin', 'mobot', 'makolem', 'nunas', 'usan', 'ngicenin', 'budal',
                'micayang', 'maputra'
            }
        }
        self.logger.debug(f"Initialized grammar with {len(self.grammar_rules)} rules and {len(self.terminals)} terminal categories")

    def cyk_parse(self, words: List[str]) -> Dict[Tuple[int, int], Set[str]]:
        """
        Implements the CYK parsing algorithm for the Balinese grammar.
        Returns a parsing table containing all possible constituents for each span.
        """
        self.logger.info(f"Starting CYK parsing for input: {' '.join(words)}")
        n = len(words)
        table = {}
        
        # Initialize the base level of the table with terminal symbols
        self.logger.debug("Initializing base level of CYK table")
        for i in range(n):
            word = words[i].lower()
            table[i, i] = set()

            # Log word processing
            self.logger.debug(f"Processing word at position {i}: '{word}'")
            
            # Check each terminal category
            found_categories = []
            for category, word_set in self.terminals.items():
                if word in word_set:
                    table[i, i].add(category)
                    found_categories.append(category)

            if found_categories:
                self.logger.debug(f"Word '{word}' matches categories: {found_categories}")
            else:
                self.logger.warning(f"Word '{word}' not found in any terminal category")
                    
            # Add categories that can derive this terminal
            for category, rules in self.grammar_rules.items():
                for rule in rules:
                    if len(rule) == 1 and rule[0] in table[i, i]:
                        table[i, i].add(category)
                        self.logger.debug(f"Added derived category {category} for word '{word}'")
        
        # Fill in the rest of the table
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                table[start, end] = set()
                
                self.logger.debug(f"Processing span ({start}, {end})")
                # Try all possible splits of the current span
                for mid in range(start, end):
                    # Look at all pairs of categories from the two spans
                    for left_cat in table[start, mid]:
                        for right_cat in table[mid + 1, end]:
                            # Check if this pair can form a larger constituent
                            for category, rules in self.grammar_rules.items():
                                if (left_cat, right_cat) in rules:
                                    table[start, end].add(category)
                                    self.logger.debug(
                                        f"Found valid combination: {left_cat} + {right_cat} -> {category} "
                                        f"for span ({start}, {end})"
                                    )

        return table

    def extract_components(self, sentence: str) -> Dict[str, str]:
        """Extracts labeled components from the input sentence."""
        self.logger.info(f"Extracting components from sentence: {sentence}")
        components = {}
        pattern = r'([SPOK][a-z]*)\s*\((.*?)\)'
        matches = re.findall(pattern, sentence)
        
        for label, content in matches:
            components[label] = content.strip()
            self.logger.debug(f"Extracted component {label}: '{content.strip()}'")
            
        self.logger.debug(f"Found {len(components)} components: {list(components.keys())}")
        return components

    def parse_sentence(self, sentence: str) -> Dict[str, bool]:
        """
        Parses a Balinese sentence and verifies its structure according to the grammar.
        Returns the validity of each component and the complete parse tree.
        """
        self.logger.info(f"Starting to parse sentence: {sentence}")
        
        # Extract labeled components
        components = self.extract_components(sentence)
        results = {}
        parse_details = {}
        
        # Parse each component
        for label, content in components.items():
            self.logger.debug(f"Parsing component {label}: '{content}'")
            words = content.split()
            parse_table = self.cyk_parse(words)
            parse_details[label] = parse_table[0, len(words)-1]
            
            # Verify component according to grammar rules
            if label == 'S':
                results[label] = 'NP' in parse_table[0, len(words)-1]
            elif label == 'P':
                results[label] = 'VP' in parse_table[0, len(words)-1]
            elif label == 'O':
                results[label] = 'NP' in parse_table[0, len(words)-1]
            elif label == 'Pel':
                results[label] = any(cat in parse_table[0, len(words)-1] 
                                   for cat in ['NP', 'VP'])
            elif label == 'Ket':
                results[label] = any(cat in parse_table[0, len(words)-1] 
                                   for cat in ['NP', 'VP', 'NumP'])
                
            self.logger.debug(f"Component {label} validity: {results[label]}")
            self.logger.debug(f"Parse details for {label}: {parse_details[label]}")
        
        # Verify overall sentence structure
        component_sequence = tuple(components.keys())
        results['K'] = component_sequence in self.grammar_rules['K']
        
        self.logger.info(f"Overall sentence structure validity: {results['K']}")
        self.logger.debug(f"Component sequence: {component_sequence}")
        
        return results, parse_details

def test_parser():
    """Test function to demonstrate parser usage."""
    # Setup logging
    logger = setup_logging()
    logger.info("Starting parser tests")
    
    parser = BalineseParserRevised()
    
    # Test sentences from different patterns
    test_sentences = [
        "S (tiang) P (mekarya) Pel (guru) O (matematika)",
        "S (bapak) P (lunga) Ket (ring sekolah)",
        "S (nina) P (malajah) O (matematika) Ket (ring kelas)",
        "S (ipun) P (numbas) O (nasi)",
    ]
    
    for sentence in test_sentences:
        logger.info(f"\nTesting sentence: {sentence}")
        results, details = parser.parse_sentence(sentence)
        
        logger.info("Component validity:")
        for component, is_valid in results.items():
            logger.info(f"{component}: {'Valid' if is_valid else 'Invalid'}")
            
        logger.debug("Parsing details:")
        for component, categories in details.items():
            logger.debug(f"{component} contains: {categories}")
    
    logger.info("Completed all parser tests")

if __name__ == "__main__":
    test_parser()