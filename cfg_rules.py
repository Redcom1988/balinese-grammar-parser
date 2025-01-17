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
    "Pronoun -> titiang | tiang | tiange | adin | adine | bapakne | bapane | bapan | dane | memene | ragane | timpal | timpalne | adik | sepedane | ketua | ipune | anake | guru | ibu | motorne | pak | pianakne",
    "Det -> punika | ento",
    "Adj -> galak | jegeg | sane | demenin | paling | akeh | luung | gati | baru | sakti | dueg | seleg | goreng | pati",
    "Verb -> melajah | kapah | melali | anggone | rauh | mekarya | manting | meblanja | dados | ngatehin | nanem | megambal | pinaka | ngajahin | abane | wewantenan",
    "Num -> telung | pitung | 2020"
]