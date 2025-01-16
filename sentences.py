# Valid Sentences:
test_valid_sentences = [
    # "titiang sampun meblanja",
    # "i putu dangin punika sesai melajah megambal",
    # "adik tiange kapah melali ka umah timpalne",
    # "sepedane wayan darta sesai anggone ngatehin bapane ka carik",
    # "ketua pasar punika sampun rauh saking tuni semeng",
    # "bapakne i putu gede punika pinaka guru olahraga di sekolah tiange",
    # "adin tiange sampun dados mahasiswa baru ring kampus udayana jimbaran",
    # "ragane sampun mekarya saking semeng pisan",
    # "dane setata manting baju akeh pisan ka tukad unda",
    # "bapan ipune sampun dados balian sakti saking sue pisan"
]

# Invalid Sentences:
test_invalid_sentences = [
    "ibu guru tiange galak pisan ngajahin matematika",
    "anake luh jegeg punika dueg pisan mekarya wewantenan",
    "pianakne pak guru ento seleg pisan melajah komputer di sekolah",
    "bapakne i putu gede guru olahraga di sekolah tiange",
    "ibu puspa punika dosen matematika sane jegeg ring kampus timpal tiange",
    "nasi goreng punika ajengan sane paling demenin tiang",
    "sepeda baru adin tiange telung pasang lakar abane ka kota surabaya",
    "sepeda motorne dadue luung pati",
    "bapan tiange ka carik nanem padi uli tuning semengan",
    "memene ketut bagus ka yogyakarta ngatehin adine"
]

# Valid Sentences:
# (S) titiang  (P) sampun meblanja  (Done)
# (S) "i putu dangin" punika  (P) sesai melajah  (O) megambal (Done)
# (S) adik tiange (P) kapah melali (Ket) ka umah timpalne   (Done)
# (S) sepedane wayan darta (P) sesai anggone (Pel) ngatehin bapane (Ket) ka carik   (Done)
# (S) ketua pasar punika (P) sampun rauh (Ket) saking tuni semeng
# (S) bapakne i putu gede punika (P) pinaka (Pel) guru olahraga (Ket) di sekolah tiange
# (S) adin tiange (P) sampun dados (Pel) mahasiswa baru (Ket) ring kampus udayana jimbaran
# (S) ragane (P) sampun mekarya (Ket) saking semeng pisan
# (S) dane (P) setata manting (O) baju akeh pisan (Ket) ka tukad unda
# (S) bapan ipune (P) sampun dados (Pel) balian sakti (Ket) saking sue pisan

# Invalid Sentences:
# (S) ibu guru tiange (P) galak pisan (Pel) ngajahin matematika
# (S) anake "luh jegeg" punika (P) dueg pisan (Pel) mekarya wewantenan
# (S) pianakne pak guru ento (P) seleg pisan (Pel) melajah komputer (Ket) di sekolah
# (S) bapakne "i putu gede" (P) guru olahraga (Ket) di sekolah tiange
# (S) ibu puspa punika (P) dosen matematika (Pel) sane jegeg (Ket) ring kampus timpal tiange
# (S) nasi goreng punika (P) ajengan (Pel) sane paling demenin tiang
# (S) sepeda baru adin tiange (P) telung pasang (Pel) lakar abane (Ket) ka kota surabaya
# (S) sepeda motorne (P) dadue (Pel) luung pati
# (S) bapan tiange (P) ka carik (Pel) nanem padi (Ket) uli tuning semengan
# (S) memene "ketut bagus" (P) ka yogyakarta (Pel) ngatehin adine