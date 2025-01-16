from typing import Dict, List, Set

class CYK_Parser:
    def __init__(self, cnf_rules: Dict[str, List[str]], start_symbol: str = 'K'):
        self.cnf_rules = cnf_rules
        self.start_symbol = start_symbol
    
    def parse(self, sentence: str) -> bool:
        words = sentence.lower().split()
        n = len(words)
        table = [[set() for j in range(n - i)] for i in range(n)]
        
        self._fill_base_cases(table, words)
        self._fill_table(table, n)
        self._print_table(table)
        
        return self.start_symbol in table[0][n-1]
    
    def _fill_base_cases(self, table: List[List[Set[str]]], words: List[str]):
        for i, word in enumerate(words):
            for lhs, rhs in self.cnf_rules.items():
                if word in rhs:
                    table[i][0].add(lhs)
    
    def _fill_table(self, table: List[List[Set[str]]], n: int):
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                for partition in range(1, length):
                    left_cell = table[start][partition-1]
                    right_cell = table[start+partition][length-partition-1]
                    
                    for left_symbol in left_cell:
                        for right_symbol in right_cell:
                            production = f"{left_symbol} {right_symbol}"
                            
                            # Check if this combination produces any non-terminal
                            for lhs, rhs in self.cnf_rules.items():
                                if production in rhs:
                                    table[start][length-1].add(lhs)
    
    def _print_table(self, table: List[List[Set[str]]]):
        """Print the CYK parsing table in a readable format."""
        for i, row in enumerate(table):
            print(f"Length {i+1}:")
            for j, cell in enumerate(row):
                if cell:
                    print(f"  Position {j}: {sorted(cell)}")
            print()

    def print_parse_result(self, sentence: str):
        """Print whether the sentence is valid according to the grammar."""
        is_valid = self.parse(sentence)
        print(f"Sentence: {sentence}")
        print(f"Is valid Balinese sentence: {is_valid}\n")

def get_cnf_rules():
    """Returns the CNF rules for Balinese grammar."""
    return  {
        "K": ["S P", "S P Pel", "S P Ket", "S P Pel Ket"],
        "S": ["NP"],
        "P": ["PP"],
        "Pel": ["VP", "NP", "Aux Adv", "Aux NP"],
        "Ket": ["PP"],
        "NP": ["Noun", "PropNoun", "Pronoun", "NP Noun", "NP PropNoun", "NP Pronoun", 
                "Det NP", "NP Det", "NP Adj"],
        "PP": ["Prep NP", "Prep Adv", "PP NumP", "PP Adv"],
        "VP": ["Verb", "Verb VP", "Verb NP", "Adv VP", "Aux VP"],
        "NumP": ["Num", "NumP NP", "NP NumP"],
        "Prep": ["ka", "uli", "di", "saking", "ring", "uling"],
        "Aux": ["dados", "sebilang", "prasida", "dadi", "sesai", "sampun", "pisan", 
                "paling", "sane"],
        "Adv": ["tuni", "semengan", "ibi", "sanja", "taun", "wai", "semeng", "peteng"],
        "Noun": ["carik", "padi", "sekolah", "sepeda", "kantor", "desa", "kampus", 
                "tukang", "desan", "pasar", "dosen", "nasi", "ajengan", "siap", "ukud"],
        "PropNoun": ["i", "ketut", "bagus", "yogyakarta", "perbekel", "guru", "camat", 
                    "kuta", "selatan", "jimbaran", "parkir", "pns", "luh", "sari", "sen"],
        "Pronoun": ["bapan", "bapak", "bu", "pak", "adin", "tiang", "titiang", "ia", 
                    "timpal-timpal", "kulawarga", "ibu", "timpal", "memen", "tiange", "meme"],
        "Det": ["punika", "ento"],
        "Adj": ["selem", "demenin", "becik", "luung", "jegeg", "jegeg-jegeg", "ilang"],
        "Verb": ["nanem", "ngatehin", "ngalihin", "melajah", "masepedaan", "nganggon", 
                "meli", "anggone", "rauh", "ngatur", "pinaka"],
        "Num": ["2020", "pitung", "telung", "limang"]
    }

def main():
    # Initialize parser with CNF rules
    parser = CYK_Parser(get_cnf_rules())

    # Test some sentences
    test_sentences = [
        "tiang melajah ring sekolah",  # I study at school
        "ia meli sepeda",  # He/she buys a bicycle
        "bapak nganggon sepeda ring kantor"  # Father uses a bicycle at the office
    ]

    for sentence in test_sentences:
        parser.print_parse_result(sentence)

if __name__ == "__main__":
    main()