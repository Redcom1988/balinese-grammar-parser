words = {
    # Kata Benda
    # 'Noun': [
    #     'liat', 'laib', 'adeg', 'ater', 'ider', 'ayah', 'uruk', 'arep', 'ibing', 'arit',
    #     'gergaji', 'rauh', 'ukir', 'tegul', 'tebus', 'beli', 'iket', 'tampi', 'uber',
    #     'gebug', 'kucit', 'kusir', 'togog', 'umah', 'dewa', 'pura', 'meme', 'adi',
    #     'tiuk', 'leak', 'raksasa', 'jukut', 'motor', 'jukung', 'emas',
    #     'jaring', 'uyah', 'sate', 'cedok', 'cekalan', 'kursi', 'gunung', 'angin',
    #     'keneh', 'sepatu', 'baju', 'tanah', 'kayu', 'atma', 'bunyi', 'suarga',
    #     'neraka', 'alas', 'dharma', 'taksu', 'sukerta', 'genta', 'pelawa', 'tedung',
    #     'guru', 'pandita', 'raja', 'teben', 'jineng', 'setra', 'tukad', 'segara',
    #     'canang', 'bhuana', 'bale', 'sanggah', 'pelinggih', 'natah', 'merajan', 'subak', 'carik',
    #     'tenget', 'balian', 'pecalang', 'kulkul', 'gamelan', 'gender', 'rindik',
    #     'canangsari', 'banten', 'sesajen', 'kober', 'umbul-umbul', 'gebogan',
    #     'pecaruan', 'padmasana', 'panggungan', 'gedong', 'paon', 'tembok',
    #     'lelangit', 'bantang', 'tulang', 'kulit', 'getih', 'lengen', 'lima',
    #     'jeroan', 'kelapa', 'base', 'don', 'bunga', 'woh', 'padang', 'abing',
    #     'tegal', 'uma', 'sema', 'pura', 'mrajan', 'jaba', 'kaja', 'kelod',
    #     'kangin', 'kauh', 'bebanten', 'tirta', 'yadnya', 'penjor', 'layangan', 'baju', 'badung',
    #     'sanglah', 'pasar', 'warung', 'jalikan', 'ketipat', 'jaja', 'arak', 'tuak', 
    #     'payuk', 'panci', 'semprong', 'kompor', 'siap', 'sampi', 'celeng', 'bangkung',
    #     'bikul', 'lelipi', 'katak', 'kedis', 'siap', 'bebek', 'meong', 'cicing',
    #     'punyan', 'entik', 'biu', 'poh', 'nangka', 'durian', 'salak', 'wani',
    #     'bingin', 'kepuh', 'delima', 'sumaga', 'jeruk', 'belimbing', 'nyuh',
    #     'jagung', 'padi', 'kacang', 'ketela', 'kesela', 'tabia', 'bawang',
    #     'jahe', 'kunyit', 'lengkuas', 'cengkeh', 'pala', 'kemiri', 'kayu',
    #     'jelanan', 'ampik', 'kakus', 'undagan', 'sinduk', 'caratan', 'sembe', 'yeh',
    #     'endut', 'bias', 'bulaan', 'tiing', 'celagih', 'gadung', 'kesuna', 'jepun',
    #     'gelang', 'kalung', 'subeng', 'udeng', 'kamben', 'saput', 'daksina', 'kajang',
    #     'dulang', 'sokasi', 'tamiang', 'sampian', 'bebed', 'bebungkilan', 'kebaya',
    #     'wastra', 'umpal', 'tepeng', 'kuskusan', 'dangdang', 'paso', 'jun', 'gentong',
    #     'pane', 'kekeb', 'kau', 'tempeh', 'penarak', 'bokor', 'wadah', 'pabuan',
    #     'cecepan', 'coblong', 'lumur', 'kecer', 'kendang', 'suling', 'gong', 'kempur',
    #     'kempli', 'gangsa', 'kantil', 'jegog', 'klentung', 'keropak', 'lontar',
    #     'prasi', 'pecanangan', 'sibuh', 'pedupaan', 'plangkiran', 'dapetan', 'penuntun',
    #     'telabah', 'carik', 'pekaseh', 'pemangku', 'klian', 'penjor', 'sanggah',
    #     'pelinggih', 'palinggih', 'tumpek', 'galungan', 'kuningan', 'saraswati',
    #     'pekarangan', 'tetaring', 'kelir', 'langse', 'aling-aling', 'klatkat',
    #     'pemesuan', 'pemrajan', 'piasan', 'penyengker', 'angkul-angkul', 'candi',
    #     'kori', 'tapakan', 'kemulan', 'taksu', 'rong', 'tugu', 'palih', 'undag',
    #     'pengubengan', 'pangapit', 'pamedal', 'jogan', 'saka', 'sunduk', 'sineb',
    #     'tetekeh', 'tiang', 'tugeh', 'dedari', 'penunggu', 'balian', 'tapel',
    #     'rangda', 'barong', 'jauk', 'telek', 'topeng', 'legong', 'pendet',
    #     'rejang', 'baris', 'sanghyang', 'kecak', 'gambuh', 'arja', 'wayang',
    #     'dalang', 'geguntangan', 'kendang', 'cengceng', 'gangsa', 'reong',
    #     'trompong', 'kajar', 'kempul', 'kemong', 'jegogan', 'jublag', 'penyacah',
    #     'kantilan', 'pemade', 'kenong', 'kelentang', 'kelentung',
    #     'kekawin', 'kidung', 'geguritan', 'peparikan', 'sendor', 'sunari', 'sesapi',
    #     'rebab', 'seruling', 'cendekan', 'pepesan', 'lawar', 'betutu', 'urutan',
    #     'timbungan', 'bantal', 'tum', 'sate', 'komoh', 'rujak', 'sambal', 'jukut',
    #     'pesan', 'gecok', 'urab', 'serombotan', 'plecing', 'sambel', 'sumping',
    #     'jaja', 'dodol', 'begina', 'satuh', 'bendu', 'lempog', 'klepon', 'tulung',
    #     'nagasari', 'apem', 'bubuh', 'tepeng', 'timpan', 'laklak', 'panggang',
    #     'pepes', 'urap', 'blayag', 'temisi', 'besisit', 'timbung', 'saur', 'siap',
    #     'gedang', 'belimbing', 'ceroring', 'delima', 'durén', 'jambu', 'juét',
    #     'manggis', 'nangka', 'nyambu', 'paya', 'sotong', 'tibah', 'wani',
    #     'bengkuang', 'boni', 'buluan', 'bunut', 'kepundung', 'kuweni', 'sentul',
    #     'silik', 'srikaya', 'sukun', 'tin', 'tingkih', 'timbul', 'rambutan', 'sekolah',
    #     'alit-alite', 'meja'
    # ],
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
        'mangkin', 'raris', 'wusan', 'wawu', 'kantun', 'dados',
        'durung', 'kapah', 'malih',
        'nadaksara', 'prajani', 'gelis-gelis', 'alon-alon', 'adeng-adeng',
        'sai-sai', 'pepes', 'terus', 'lantas', 'malih', 'buin', 'suba', 'mara',
        'wau', 'durung', 'nenten', 'ten', 'tusing', 'ngiring', 'dados',
        'bisa', 'prasida', 'mampuh', 'nyidayang', 'sabenehne', 'sayuwakti',
        'sajatine', 'sujatine', 'wiakti', 'sekadi', 'minakadi', 'kadi', 'sakadi',
        'pateh', 'patuh', 'soroh', 'minab', 'jenenga', 'pepes', 'ping', 'wantah',
        'wenten', 'kantun', 'ngararis', 'raris', 'mangkin', 'pisan', 'jagi'
    ],
    'Prep': [
        'ring', 'ba', 'ka', 'saking', 'uli', 'duk', 'olih',
        'di', 'ke', 'uli', 'sig', 'antuk', 'maring', 'marep',
        'duri', 'beten', 'duur', 'tengah', 'samping', 'sisi', 'jaba',
        'kelod', 'kaja', 'kangin', 'kauh', 'tengahan', 'sisin', 'sedin',
        'bucun', 'diwangan', 'sajabaning', 'sajeroning', 'ring ajeng', 'ring duri',
        'ring tengah', 'ring sisin', 'ring bucun', 'ka jaba', 'ka jeroan',
        'saking jaba', 'saking jeroan', 'olih ring', 'rauh ring', 'kantos ring',
        'ngantos ring', 'sadurung ring', 'sasampun ring', 'sajabaning ring',
        'sajeroning ring', 'sane ring', 'sane maring', 'sane antuk', 'ring', 'di',
        'margi', 'ngangin', 'ngauh', 'ngaja', 'ngelod', 'menek', 'tuun',
        'kebet', 'kelawan', 'sareng', 'teken', 'ajak', 'kayang', 'kanti',
        'sambil', 'sedekan', 'sedek', 'risedek', 'rikala', 'dugase', 'dugas',
        'daweg', 'ritatkala', 'olih', 'antuk', 'maring', 'sareng',
        'teken', 'ajak', 'ngajak', 'bareng', 'ngiring', 'sameton', 'nyama',
        'braya', 'kulawarga', 'kadang', 'wargi', 'arsa', 'sumeken', 
        'sajeroning', 'tengahing', 'ngawit', 'kayang', 'rauh'
    ],
    'Pronoun': [
        'tiang', 'cang', 'iragane', 'ci', 'ia', 'ida', 'nyane', 'kami', 'iraga',
        'idane', 'dane', 'nenten', 'nikanne', 'ikane', 'sapa', 
        'puniki', 'punapi', 'titiang', 'icang', 'kai', 'jerone', 'ragane', 'gusi',
        'cai', 'iba', 'ipun',
        'gelah', 'dewek', 'awakne', 'ida-dane', 'sira', 'ipun-ipun', 'rerama',
        'okane', 'putrane', 'okan-okane', 'putran-putrane', 'ragan-ragane',
        'sami', 'samian', 'samiyan', 'sinamian', 'parasida', 'parasami',
        'parajana', 'parajanma', 'parajero', 'parasane', 'paranirane',
        'parasapasira', 'parasapasami', 'puniku', 
        'punikune', 'niki', 'nika', 'niku',
        'sira-sira', 'sapasira', 'sapasami', 'sapunapi-sapunapi',
        'manira', 'gelah', 'nira', 'ira', 'ratu', 'cokor', 'palungguh',
        'dane', 'rerama', 'meme', 'bapa', 'biang', 'aji', 'bibi',
        'uwa', 'pekak', 'dadong', 'kakiang', 'niang', 'embok', 'beli',
        'misan', 'mindon', 'kumpi', 'buyut', 'canggah', 'wareng', 'kelab',
        'uduh', 'klabang', 'gantung', 'siwer', 'ratu', 'dewa', 'betara',
        'widhi', 'hyang', 'ida', 'dané', 'ragané', 'titiang',
        'iragang', 'gelahé', 'awakné', 'dewekné', 'ragané', 'idané'
    ],
    'Det': [
        'niki', 'nika', 'puniki', 'punika', 'ene', 'ento', 'ne', 'to',
        'anu', 'ane', 'punikine', 'punikane', 'punikune', 'nikine', 'nikane',
        'nikune', 'niki-nika', 'puniki-punika'
    ],
    'Num': [
        # Cardinal numbers
        'besik', 'kalih', 'tiga', 'papat', 'lima', 'nem', 'pitu', 'kutus', 'sia', 'dasa',
        # Ordinal numbers
        'kapertama', 'kaping kalih', 'kaping tiga', 'kaping papat', 'kaping lima',
        # Collective numbers
        'aketi', 'asiu', 'ayu', 'atus', 'adasa',
        # Fractional numbers
        'aparo', 'duang paro', 'telung paro'
    ],
    'intransitiveVerb': [
        'mejalan', 'melaib', 'negak', 'teka', 'ulung', 'medem', 'matangi', 
        'nongos', 'luas', 'makecos', 'makecog', 'makeber', 'nglayang', 'nglangi', 
        'ngeling', 'makarya', 'magae', 'megae', 'masare', 'mesuryak', 'makejer', 
        'mekekeh', 'meluah', 'ngendih', 'majemuh', 'masisigan', 'ngoyong', 'mabanten', 
        'muspa', 'masemadi', 'mayoga', 'masekar', 'megending', 'makekawin', 'ngigel', 
        'magebur', 'merebah', 'mebikas', 'megedi', 'makuuk', 'masemu', 'mekipe', 
        'mekedek', 'melali', 'mengkeb', 'menjit', 'mentik', 'mesiat', 'metimpuh', 
        'mesuryak', 'dados', 'makelimat', 'maplisahan', 'mekumpul', 'mepaluing', 
        'merengin', 'mesangih', 'mesaut', 'meturut', 'mawangsit', 'masayuban', 
        'masemayan', 'masesangi', 'masesapan', 'matektekan', 'matirtayan', 'mayasakala', 
        'malajah', 'tinggal'
    ],
    'transitiveVerb': [
        'meli', 'numbas', 'meliang', 'ngajeng', 'madaar', 'ngamah', 'minum', 'nginem', 
        'nyemak', 'ngejang', 'ngaba', 'nyuun', 'ngisinin', 'ngutang', 'nyangih', 
        'ngorahang', 'nuturang', 'ngaukin', 'nulungin', 'nguruk', 'ngajahin', 'nunden', 
        'mapitulung', 'nyagjagin', 'ngortain', 'ngae', 'ngaenang', 'nulis', 'nyurat', 
        'ngukir', 'metanding', 'ngocek', 'ngadukang', 'ningalin', 'ngerasang', 'ningeh', 
        'ngadek', 'ngecap', 'malajah', 'memaca', 'ngaturang', 'ngisidang', 'nyangkepang', 
        'ngubadin', 'ngupayang', 'nguratiang', 'ngidih', 'nyilih', 'ngadep', 'negul', 
        'nguberin', 'ngebah', 'nyangkol', 'ngateh', 'nyarup', 'ngecum', 'nyiksik', 
        'nyangket', 'ngebug', 'nyiup', 'negakin', 'nyampat', 'ngumbah', 'ngetep', 
        'nulad', 'nyangkil', 'nengok', 'ningting', 'ngetok', 'ngibukang', 'nyarmin', 
        'ngangget', 'ngutgut', 'ngesges', 'ngebut', 'ngepung', 'nyemuh', 'nguyak', 
        'ngungkab', 'ngebet', 'nguncab', 'ngebang', 'nyedut', 'ngampik', 'ngejer', 
        'ngengap', 'ngukud', 'ngenahang', 'ngorahin', 'nyemakang', 'ngadanin', 'nyelepin', 
        'ngelengin', 'ngamaang', 'nampedang', 'nampenin', 'nampiang', 'nandesang', 
        'nandiang', 'nandingang', 'nandurin', 'nanenayang', 'nanggapin', 'nangkenang', 
        'nangkidang', 'nangkilin', 'ngamenekang', 'ngedengang', 'ngedilang', 'ngejotin', 
        'ngekadang', 'ngematiang', 'ngemasin', 'ngempelin', 'ngempetin', 'ngencakang', 
        'ngendahang', 'ngenjuhin', 'ngentenang', 'ngentikang', 'ngenyudang', 'ngerehang', 
        'ngerusuhin', 'ngesenggang', 'ngetakang', 'ngetelang', 'ngetuhang', 'ngewangang', 
        'ngicenin', 'ngidupang', 'ngilehin', 'ngilingin', 'ngimpasin', 'ngindayang', 
        'ngintipang', 'ngisiang', 'ngitungang', 'ngiwasin', 'nglanturang', 'nglemesin', 
        'nglepasang', 'nglinggihang', 'ngojarang', 'ngomong', 'ngonemin', 'ngortain', 
        'ngosong', 'ngubadin', 'ngubuhin', 'nguduhin', 'ngulapin', 'ngulatin', 'nguliang', 
        'ngulurin', 'ngumpulang', 'ngumpulin', 'ngundebang', 'ngundigang', 'nguntulang', 
        'ngupayang', 'ngurukang', 'ngutangag', 'ngutsahayang', 'nguwuhin', 'nyelapang', 
        'nyelempang', 'merasa', 'bangun', 'maem'
    ],
    'contextDependentVerb': [
        'malajah',      # can study (intransitive) or study something (transitive)
        'megending',    # can sing (intransitive) or sing something (transitive)
        'maplalian',    # can play (intransitive) or play with something (transitive)
        'memaca',       # can read (intransitive) or read something (transitive)
        'ngomong',      # can talk (intransitive) or tell something (transitive)
        'ngraos',       # can speak (intransitive) or speak about something (transitive)
        'matutur',      # can converse (intransitive) or tell something (transitive)
        'metelik',      # can peek (intransitive) or peek at something (transitive)
        'metakon',      # can ask (intransitive) or ask something (transitive)
        'nongos',       # can stay (intransitive) or occupy something (transitive)
        'masare',       # can sleep (intransitive) or sleep on something (transitive)
        'mesuryak',     # can shout (intransitive) or shout something (transitive)
        'ngeling',      # can cry (intransitive) or cry for something (transitive)
        'ngigel',       # can dance (intransitive) or dance something (transitive)
        'makekawin',    # can sing poetry (intransitive) or sing specific poetry (transitive)
        'mabanten',     # can make offerings (intransitive) or offer something specific (transitive)
        'ngayah',       # can serve (intransitive) or serve something (transitive)
        'metanding',    # can arrange (intransitive) or arrange something (transitive)
        'nganteb',      # can hit (intransitive) or hit something (transitive)
        'malayang'      # can fly (intransitive) or fly something (transitive)
    ],
}

nounCategories = {
    'food': ['jaja', 'jukut', 'sate', 'lawar', 'betutu', 'pepesan', 'timbungan', 'urutan', 
             'komoh', 'rujak', 'sambal', 'urab', 'serombotan', 'plecing', 'sambel', 
             'dodol', 'begina', 'satuh', 'bendu', 'lempog', 'klepon', 'nagasari', 
             'apem', 'bubuh', 'tepeng', 'timpan', 'laklak', 'panggang', 'pepes', 
             'blayag', 'temisi', 'besisit', 'timbung', 'ketipat', 'pesan', 'gecok',
             'sumping', 'saur', 'gedang', 'belimbing', 'ceroring', 'delima', 'durén', 
             'jambu', 'juét', 'manggis', 'nangka', 'nyambu', 'paya', 'sotong', 'tibah', 
             'wani', 'bengkuang', 'boni', 'buluan', 'bunut', 'kepundung', 'kuweni', 
             'sentul', 'silik', 'srikaya', 'sukun', 'tin', 'tingkih', 'timbul', 'rambutan', 'nasi'],

    'drink': ['arak', 'tuak', 'tirta', 'yeh'],

    'items': ['baju', 'sepatu', 'gelang', 'kalung', 'subeng', 'udeng', 'kamben', 
              'saput', 'bebed', 'kebaya', 'wastra', 'umpal', 'layangan', 'kober', 
              'umbul-umbul', 'kajang', 'dulang', 'sokasi', 'tamiang', 'sampian',
              'bebungkilan', 'tetaring', 'kelir', 'langse', 'aling-aling', 'klatkat',
              'liat', 'laib', 'adeg', 'ater', 'ider', 'ayah', 'uruk', 'arep', 'ibing', 
              'tegul', 'tebus', 'beli', 'iket', 'tampi', 'uber', 'gebug', 'bantang', 
              'tulang', 'kulit', 'getih', 'lengen', 'lima', 'jeroan', 'kelapa', 'base'],

    'tools': ['tiuk', 'gergaji', 'cedok', 'cekalan', 'sinduk', 'caratan', 'sembe',
              'kuskusan', 'dangdang', 'paso', 'jun', 'gentong', 'pane', 'kekeb', 
              'kau', 'penarak', 'bokor', 'wadah', 'pabuan', 'cecepan', 'coblong',
              'lumur', 'jalikan', 'payuk', 'panci', 'semprong', 'kompor', 'kulkul',
              'arit'],

    'offerings': ['canang', 'banten', 'sesajen', 'gebogan', 'canangsari', 'pecaruan', 
                  'bebanten', 'yadnya', 'daksina', 'sibuh', 'pedupaan', 'plangkiran',
                  'dapetan', 'penuntun'],

    'places': ['sekolah', 'pasar', 'setra', 'jaba', 'kaja', 'kelod', 'kangin', 'kauh', 
               'teben', 'badung', 'sanglah'],

    'property': ['umah', 'tanah', 'merajan', 'bale', 'sanggah', 'pelinggih', 'natah', 
                 'gedong', 'paon', 'tembok', 'tegal', 'uma', 'sema', 'pura', 'mrajan',
                 'warung', 'kakus', 'ampik', 'undagan', 'pekarangan', 'pemesuan', 
                 'pemrajan', 'piasan', 'penyengker', 'angkul-angkul', 'candi', 'kori',
                 'tapakan', 'kemulan', 'rong', 'tugu', 'palih', 'undag', 'pengubengan',
                 'pangapit', 'pamedal', 'jogan', 'saka', 'sunduk', 'sineb', 'tetekeh',
                 'tiang', 'tugeh', 'lelangit', 'jineng', 'carik'],

    'people': ['guru', 'pandita', 'raja', 'balian', 'pecalang', 'pemangku', 'klian',
               'meme', 'adi', 'dewa', 'raksasa', 'kusir', 'dalang', 'dedari', 
               'penunggu', 'leak', 'pekaseh', 'alit-alite'],

    'arts': ['gamelan', 'gender', 'rindik', 'kendang', 'suling', 'gong', 'kempur',
             'kempli', 'gangsa', 'kantil', 'jegog', 'klentung', 'kekawin', 'kidung',
             'geguritan', 'peparikan', 'kecer', 'cengceng', 'reong', 'trompong',
             'kajar', 'kempul', 'kemong', 'jegogan', 'jublag', 'penyacah', 'kantilan',
             'pemade', 'kenong', 'kelentang', 'kelentung', 'rebab', 'seruling',
             'sendor', 'sunari', 'sesapi', 'cendekan', 'rangda', 'barong', 'jauk',
             'telek', 'topeng', 'legong', 'pendet', 'rejang', 'baris', 'sanghyang',
             'kecak', 'gambuh', 'arja', 'wayang', 'geguntangan', 'tapel', 'ukir'],

    'documents': ['lontar', 'prasi', 'keropak'],

    'abstract': ['keneh', 'atma', 'dharma', 'taksu', 'sukerta', 'suarga', 'neraka', 
                 'alas', 'bhuana', 'tenget', 'bunyi'],

    'vehicles': ['motor', 'jukung'],

    'furniture': ['kursi', 'meja'],

    'nature': ['gunung', 'angin', 'tukad', 'segara', 'bunga', 'don', 'woh', 'padang', 
               'abing', 'bias', 'endut', 'telabah', 'punyan', 'entik', 'biu', 'poh',
               'bingin', 'kepuh', 'jagung', 'padi', 'kacang', 'ketela', 'kesela', 
               'tabia', 'bawang', 'jahe', 'kunyit', 'lengkuas', 'cengkeh', 'pala', 
               'kemiri', 'celagih', 'gadung', 'kesuna', 'jepun'],

    'materials': ['kayu', 'emas', 'tiing', 'bulaan', 'batu', 'plastik', 'besi', 'mas', 
                 'selaka', 'tembaga', 'jaring', 'uyah'],

    'animals': ['kucit', 'siap', 'sampi', 'celeng', 'bangkung', 'bikul', 'lelipi', 
                'katak', 'kedis', 'bebek', 'meong', 'cicing'],

    'ceremonial': ['galungan', 'kuningan', 'saraswati', 'penjor', 'tumpek', 'upacara', 
                  'odalan', 'pawiwahan', 'ngaben', 'potong_gigi', 'genta', 'pelawa', 
                  'tedung']
}

verbCategoryPairs = {
    # Eating/Drinking verbs
    'ngajeng': ['food'],
    'maem': ['food'],
    'madaar': ['food'],
    'nginem': ['drink'],
    'minum': ['drink'],
    
    # Carrying/Movement verbs
    'ngaba': ['items', 'offerings', 'tools', 'food', 'documents'],
    'nyuun': ['offerings', 'items', 'food'],
    'nyemak': ['items', 'tools', 'food', 'documents'],
    'ngisidang': ['items', 'tools', 'furniture'],
    'ngungsi': ['places', 'property'],
    'ngatehang': ['people', 'animals'],
    
    # Perception verbs
    'ningalin': ['people', 'arts', 'nature', 'animals', 'ceremonial'],
    'ningeh': ['arts', 'abstract'],
    'ngadek': ['food', 'nature', 'offerings'],
    'metelik': ['people', 'animals', 'ceremonial'],
    
    # Communication verbs
    'ngorahang': ['abstract'],
    'nuturang': ['abstract'],
    'ngaukin': ['people'],
    'ngomong': ['abstract'],
    'nyapa': ['people'],
    'nuturin': ['people'],
    'nyatuang': ['people'],
    
    # Creation/Work verbs
    'ngae': ['food', 'offerings', 'items', 'arts'],
    'nulis': ['documents', 'abstract'],
    'ngukir': ['materials', 'arts'],
    
    # Learning/Teaching verbs
    'melajah': ['arts', 'abstract', 'documents'],
    'nguruk': ['people'],
    'nurturang': ['abstract'],
    'ngajain': ['people'],
    
    # Religious/Ceremonial verbs
    'ngaturang': ['offerings'],
    'mabanten': ['offerings'],
    'ngayah': ['ceremonial'],
    
    # Activity verbs
    'megending': ['arts'],
    'maplalian': ['items', 'tools'],
    'memaca': ['documents', 'abstract'],
    'masare': ['property'],
    'ngigel': ['arts'],
    
    # Cleaning/Maintenance verbs
    'nyampat': ['property', 'places'],
    'ngumbah': ['items', 'vehicles'],
    'ngisinin': ['items', 'tools'],
    
    # Commerce verbs
    'meli': ['items', 'food', 'drink', 'vehicles', 'property', 'materials'],
    'ngadep': ['items', 'food', 'drink', 'vehicles', 'property', 'materials'],
    'numbas': ['items', 'food', 'drink', 'vehicles', 'property', 'materials'],

    # Social interaction verbs
    'ngajak': ['people'],
    'nekain': ['people'],
    'nyagjagin': ['people'],
    'ngalemesin': ['people'],
    'nulungin': ['people'],
    'marengin': ['people'],
    'ngantosang': ['people'],
    'ngalih': ['people', 'items'],
    'mapag': ['people'],
    'ngajakin': ['people'],
    'ngempi': ['people'],
    'ngencanin': ['people']
}