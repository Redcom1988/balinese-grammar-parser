from cfg_to_cnf import CFG_to_CNF
from cfg_pred_pp import cfg_rules

class CYKParser:
    def __init__(self, cfg_rules):
        converter = CFG_to_CNF()
        self.rules = converter.convert_to_cnf(cfg_rules)
        self.table = None

    def _initialize_table(self, length):
        return [[set() for _ in range(length)] for _ in range(length)]

    def _fill_terminals(self, words):
        for i, word in enumerate(words):
            for lhs, rules in self.rules.items():
                for rule in rules:
                    if len(rule) == 1 and rule[0].lower() == word.lower():
                        self.table[0][i].add(lhs)

    def _fill_cell(self, row, col, span):
        for split in range(span - 1):
            for lhs, rules in self.rules.items():
                for rule in rules:
                    if len(rule) == 2:
                        B, C = rule
                        if (B in self.table[split][col] and 
                            C in self.table[row-split-1][col+split+1]):
                            self.table[row][col].add(lhs)

    def parse(self, sentence):
        words = sentence.lower().split()
        n = len(words)
        
        self.table = self._initialize_table(n)
        self._fill_terminals(words)
        
        for span in range(2, n + 1):
            for start in range(n - span + 1):
                self._fill_cell(span-1, start, span)

        parsed_table = [[sorted(list(cell)) if cell else ['[]'] 
                        for cell in row] for row in self.table]
        
        is_valid = 'K' in self.table[n-1][0]
        
        return parsed_table, is_valid

def main():
    # Create parser directly with CFG rules
    parser = CYKParser(cfg_rules)
    
    # Test sentence
    sentence = "titiang sampun meblanja"
    table, is_valid = parser.parse(sentence)
    
    print(f"\nInput sentence: {sentence}")
    for row in table:
        print(row)
    print(f"Valid: {is_valid}")

if __name__ == "__main__":
    main()