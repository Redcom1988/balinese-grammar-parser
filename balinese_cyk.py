from typing import Dict, List, Set, Tuple
from sentences import test_valid_sentences, test_invalid_sentences

class CNFConverter:
    def __init__(self):
        self.iteration = 0
        self.non_terminals = {}
        self.productions = []
    
    def convert_to_cnf(self, cfg_rules: List[str]) -> Dict[str, List[str]]:
        """Convert CFG rules to CNF format."""
        # Split rules into non-terminals and productions
        for index, rule in enumerate(cfg_rules):
            lhs, rhs = rule.split(" -> ")
            self.non_terminals[lhs] = index
            self.productions.append(rhs.split(" | "))
        
        # Sort productions
        for index, rule in enumerate(self.productions):
            for i in range(1, len(self.productions[index])):
                key = self.productions[index][i]
                j = i - 1
                while j >= 0 and key < self.productions[index][j]:
                    self.productions[index][j + 1] = self.productions[index][j]
                    j = j - 1
                self.productions[index][j + 1] = key

        # Convert each production to CNF
        for index, part in enumerate(self.productions):
            temp = self._handle_unit_production(part)
            self.productions[index] = temp
        
        # Create final CNF dictionary
        cnf_rules = {}
        for key, val in self.non_terminals.items():
            cnf_rules[key] = self.productions[val]
        
        return cnf_rules
    
    def _reduce_production(self, unit: List[str]) -> List[str]:
        """Reduce productions with more than two symbols."""
        if len(unit) <= 2:
            return [" ".join(unit)]
            
        temp = []
        new_var = f"X{self.iteration}"
        
        # Combine first two symbols
        combined = f"{unit[0]} {unit[1]}"
        temp.append(combined)
        
        # Create new non-terminal if needed
        if temp not in self.productions:
            self.non_terminals[new_var] = len(self.non_terminals)
            self.productions.append(temp)
            self.iteration += 1
            temp = self._reduce_production([new_var] + unit[2:])
        else:
            existing_var = list(self.non_terminals.keys())[self.productions.index(temp)]
            temp = self._reduce_production([existing_var] + unit[2:])
            
        return temp
    
    def _handle_unit_production(self, part: List[str]) -> List[str]:
        """Handle unit productions and call reduce_production when needed."""
        temp = []
        for unit in part:
            symbols = unit.split()
            if len(symbols) == 1:
                if unit in self.non_terminals:
                    temp.extend(self._handle_unit_production(
                        self.productions[self.non_terminals[unit]]))
                else:
                    return part
            elif len(symbols) > 2:
                temp.extend(self._reduce_production(symbols))
            else:
                temp.append(unit)
        return temp

class CYKParser:
    def __init__(self, cnf_rules: Dict[str, List[str]], start_symbol: str = 'K'):
        self.cnf_rules = cnf_rules
        self.start_symbol = start_symbol
    
    def parse(self, sentence: str) -> bool:
        """Parse a sentence using the CYK algorithm and track structure."""
        words = sentence.lower().split()
        n = len(words)
        table = [[[] for _ in range(n - i)] for i in range(n)]
        
        # Fill base cases with words and their roles
        for i, word in enumerate(words):
            for lhs, rhs in self.cnf_rules.items():
                if word in rhs:
                    table[i][0].append((lhs, word, None, 'terminal'))
        
        # Fill table using CYK algorithm
        for length in range(2, n + 1):
            for col in range(n - length + 1):
                for k in range(length - 1):
                    self._combine_cells(table, col, k, length)
        
        self.print_table_with_structure(table)
        valid = any(item[0] == self.start_symbol for item in table[0][n-1])
        
        if valid:
            print("\nClear Sentence Structure:")
            # Find and print the most appropriate parse
            best_parse = self._find_best_parse(table[0][n-1])
            if best_parse:
                self._print_clear_structure(best_parse, words)
        return valid

    def _find_best_parse(self, possible_parses):
        """Select the most appropriate parse tree based on grammatical structure."""
        def get_parse_score(parse):
            if not isinstance(parse, tuple):
                return 0
                
            # Score based on grammatical completeness
            score = 0
            
            # Prefer non-X rules
            if not parse[0].startswith('X'):
                score += 5
                
            # Prefer complete sentence structures
            if parse[0] == 'K':
                has_subject = False
                has_predicate = False
                has_object = False
                
                if isinstance(parse[1], tuple):
                    if parse[1][0] == 'S':
                        has_subject = True
                        score += 3
                        
                if isinstance(parse[2], tuple):
                    if parse[2][0] == 'P':
                        has_predicate = True
                        score += 3
                    elif parse[2][0] == 'O':
                        has_object = True
                        score += 2
                        
                # Bonus for complete S-P-O structure
                if has_subject and has_predicate:
                    score += 2
                    
            # Prefer structured VP interpretations
            if parse[0] == 'VP':
                if isinstance(parse[1], tuple) and isinstance(parse[2], tuple):
                    if parse[1][0] in ['Aux', 'Verb'] and parse[2][0] == 'Verb':
                        score += 3
                        
            return score

        # Sort parses by score and return the highest scoring valid parse
        scored_parses = [(p, get_parse_score(p)) for p in possible_parses]
        scored_parses.sort(key=lambda x: x[1], reverse=True)
        
        return scored_parses[0][0] if scored_parses else None

    def _combine_cells(self, table, col, k, length):
        """Combine cells according to CNF rules, tracking structure."""
        for left in table[col][k]:
            for right in table[col + k + 1][length - k - 2]:
                production = f"{left[0]} {right[0]}"
                for lhs, rhs in self.cnf_rules.items():
                    if production in rhs:
                        # Check if we're creating a Pel and ensure P exists
                        if lhs == 'Pel':
                            # Check if P exists in earlier positions
                            has_predicate = False
                            for i in range(col):
                                for j in range(len(table[i])):
                                    if any(item[0] == 'P' for item in table[i][j]):
                                        has_predicate = True
                                        break
                            if not has_predicate:
                                continue  # Skip this Pel production if no P exists
                        
                        new_item = (lhs, left, right)
                        if not any(x[0] == lhs and x[1] == left and x[2] == right 
                                for x in table[col][length-1]):
                            table[col][length-1].append(new_item)

    def _print_clear_structure(self, node, words, level=0):
        """Print a clear, simplified structure based on grammatical categories."""
        if not node:
            return

        indent = "  " * level
        components = {
            'S': 'Subject',
            'P': 'Predicate',
            'O': 'Object',
            'Pel': 'Complement',
            'Ket': 'Explanation',
            'NP': 'Noun Phrase',
            'VP': 'Verb Phrase',
            'SimpleVP': 'Simple Verb',
            'ComplexVP': 'Compound Verb',
            'AuxVP': 'Auxiliary Verb Phrase',
            'PP': 'Prepositional Phrase',
        }

        if isinstance(node[1], str):  # Terminal node
            label = components.get(node[0], node[0])
            print(f"{indent}{label}: {node[1]}")
        else:
            label = components.get(node[0], node[0])
            print(f"{indent}{label}")
            if node[1]:
                self._print_clear_structure(node[1], words, level + 1)
            if node[2]:
                self._print_clear_structure(node[2], words, level + 1)

    def print_table_with_structure(self, table):
        """Print the parsing table as a right triangle with the longest row at the bottom."""
        n = len(table)
        if n == 0:
            return

        # Calculate the maximum width needed for cell content
        max_width = 0
        for row in table:
            for cell in row:
                content = ', '.join(sorted(set(item[0] for item in cell if not item[0].startswith('X'))))
                max_width = max(max_width, len(content))
        
        # Ensure minimum width and add padding
        cell_width = max(max_width + 2, 10)
        
        print("\nParsing Table:")
        
        # Helper function to create horizontal separator
        def create_separator(num_cells):
            return ("+" + "-" * cell_width) * num_cells + "+"
        
        # Print from top to bottom
        for i in range(n-1, -1, -1):
            # Print separator
            print(create_separator(n-i))
            
            # Print cells
            row_content = "|"
            for j in range(n-i):
                cell = table[j][i]
                content = ', '.join(sorted(set(item[0] for item in cell if not item[0].startswith('X'))))
                if not content:
                    content = "∅"  # Use empty set symbol for empty cells
                row_content += f"{content:^{cell_width}}|"
            print(row_content)
        
        # Print final separator
        print(create_separator(n))
        
        # Print position indicators
        pos_line = "|"
        for j in range(n):
            pos_line += f"{'Pos ' + str(j):^{cell_width}}|"
        print(pos_line)
        print(create_separator(n))

def main():
    cfg_rules = [
    # Basic sentence structures including S P O patterns
        "K -> S P O | S P | S P O Ket | S P Pel | S P Ket | S P Pel Ket",
        
        # Core components
        "S -> NP",
        "P -> VP | Adj Adv | VP Adv | ka PP",
        "Pel -> Adj PP | NumP PP | NP Pronoun | NP | SimpleVP NP | NP Adj",
        "O -> NP | Verb | NP AdjP",
        "Ket -> PP | PP PP | Adv",

        
        # Phrase structures
        "NP -> Noun | PropNoun | Pronoun | Det NP | NP Noun | NP PropNoun | NP Det | NP NumP | Noun Pronoun | Pronoun Pronoun",
        "PP -> Prep | Prep NP | PP AdvP",

        "VP -> SimpleVP | ComplexVP | AuxVP | Verb Pronoun", 
        "SimpleVP -> Verb", 
        "ComplexVP -> Verb Verb", 
        "AuxVP -> Aux SimpleVP", 
        "AdjP -> Adj Adv | Adj Aux",

        "NumP -> Num | Num Noun | NumP Adv",
        "AdvP -> Adv Adv",
        
        # Terminals
        "Prep -> ka | uli | di | saking | ring | uling",
        "Aux -> dados | sesai | prasida | dadi | sesai | sampun | pisan | paling | sane | setata | lakar",
        "Adv -> tuning | tuni | semengan | ibi | sanja | taun | wai | semeng | peteng | sue | pisan",
        "Noun -> carik | padi | sekolah | sepeda | kantor | desa | kampus | tukang | pasar | dosen | nasi | ajengan | siap | ukud | baju | mahasiswa | olahraga | balian | komputer | sepatu | kota | motor | umah | olahraga | matematika | pasang",
        "PropNoun -> i | putu | dangin | wayan | darta | gede | kampus | udayana | jimbaran | tukad | unda | yogyakarta | ketut | bagus | luh | jegeg | puspa | surabaya | dadue",
        "Pronoun -> titiang | tiang | tiange | adin | adine | bapakne | bapane | bapan | dane | memene | ragane | timpal | timpalne | adik | sepedane | ketua | ipune | anake | guru | ibu | motorne",
        "Det -> punika | ento",
        "Adj -> galak | jegeg | sane | demenin | paling | akeh | luung | gati | baru | sakti | dueg | seleg | goreng",
        "Verb -> melajah | kapah | melali | anggone | rauh | mekarya | manting | meblanja | dados | ngatehin | nanem | megambal | pinaka | ngajahin | abane | wewantenan",
        "Num -> telung | pitung | 2020"
    ]
    

    
    
    # Convert CFG to CNF and create parser
    converter = CNFConverter()
    cnf_rules = converter.convert_to_cnf(cfg_rules)
    parser = CYKParser(cnf_rules)
    
    print("Valid sentences:")
    for sentence in test_valid_sentences:
        print(f"\nParsing sentence: {sentence}")
        is_valid = parser.parse(sentence)
        print(f"Valid: {is_valid}")

    print("\nInvalid sentences:")
    for sentence in test_invalid_sentences:
        print(f"\nParsing sentence: {sentence}")
        is_valid = parser.parse(sentence)
        print(f"Valid: {is_valid}")

if __name__ == "__main__":
    main()