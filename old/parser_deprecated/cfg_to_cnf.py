class CFG_to_CNF:
    def __init__(self):
        self.new_rules = {}
        self.unit_productions = set()
        self.temp_counter = 1
        self.derivations = {}  # Store all possible derivations

    def _find_all_derivations(self, symbol, cfg_rules):
        """Find all possible categories that can be derived from a symbol"""
        if symbol in self.derivations:
            return self.derivations[symbol]

        derivations = {symbol}
        changed = True
        while changed:
            changed = False
            for lhs, rules in cfg_rules.items():
                for rule in rules:
                    if len(rule) == 1 and rule[0] in derivations and lhs not in derivations:
                        derivations.add(lhs)
                        changed = True

        self.derivations[symbol] = derivations
        return derivations

    def convert_to_cnf(self, cfg_rules):
        # First compute all possible derivations
        for symbol in cfg_rules.keys():
            self._find_all_derivations(symbol, cfg_rules)

        # Initialize new rules
        self.new_rules = {}
        
        # Process each rule
        for lhs, productions in cfg_rules.items():
            self.new_rules[lhs] = []
            for prod in productions:
                if len(prod) == 1:
                    if not prod[0].isupper():  # Terminal symbol
                        # Find all categories that can be derived from this terminal
                        term = prod[0]
                        derivs = self._find_all_derivations(lhs, cfg_rules)
                        for deriv in derivs:
                            if deriv not in self.new_rules:
                                self.new_rules[deriv] = []
                            if [term] not in self.new_rules[deriv]:
                                self.new_rules[deriv].append([term])
                    else:  # Unit production
                        derivs = self._find_all_derivations(prod[0], cfg_rules)
                        for deriv in derivs:
                            if [deriv] not in self.new_rules[lhs]:
                                self.new_rules[lhs].append([deriv])
                else:
                    self.new_rules[lhs].append(prod)

        # Handle binary and longer productions
        self._convert_long_productions()
        return self.new_rules

    def _convert_long_productions(self):
        final_rules = {}
        for lhs, productions in self.new_rules.items():
            if lhs not in final_rules:
                final_rules[lhs] = []
            
            for prod in productions:
                if len(prod) > 2:
                    # Convert long production to binary rules
                    current_lhs = lhs
                    remaining = prod.copy()
                    while len(remaining) > 2:
                        new_var = f"X{self.temp_counter}"
                        self.temp_counter += 1
                        if current_lhs not in final_rules:
                            final_rules[current_lhs] = []
                        final_rules[current_lhs].append([remaining[0], new_var])
                        current_lhs = new_var
                        remaining = remaining[1:]
                    if current_lhs not in final_rules:
                        final_rules[current_lhs] = []
                    final_rules[current_lhs].append(remaining)
                else:
                    final_rules[lhs].append(prod)
        
        self.new_rules = final_rules