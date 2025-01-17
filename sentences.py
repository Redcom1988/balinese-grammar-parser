# Valid Sentences:
test_valid_sentences = [
    "Titiang sampun meblanja",
    "I putu dangin punika sesai melajah megambal",
    "Adik tiange kapah melali ka umah timpalne",
    "Sepedane wayan darta sesai anggone ngatehin bapane ka carik",
    "Ketua pasar punika sampun rauh saking tuni semeng",
    "Bapakne i putu gede punika pinaka guru olahraga di sekolah tiange",
    "Adin tiange sampun dados mahasiswa baru ring kampus udayana jimbaran",
    "Ragane sampun mekarya saking semeng pisan",
    "Dane setata manting baju akeh pisan ka tukad unda",
    "Bapan ipune sampun dados balian sakti saking sue pisan"
]

# Invalid Sentences:
test_invalid_sentences = [
    "Ibu guru tiange galak pisan ngajahin matematika",
    "Anake luh jegeg punika dueg pisan mekarya wewantenan",
    "Pianakne pak guru ento seleg pisan melajah komputer di sekolah",
    "Bapakne i putu gede guru olahraga di sekolah tiange",
    "Ibu puspa punika dosen matematika sane jegeg ring kampus timpal tiange",
    "Nasi goreng punika ajengan sane paling demenin tiang",
    "Sepeda baru adin tiange telung pasang lakar abane ka kota surabaya",
    "Sepeda motorne dadue luung pati",
    "Bapan tiange ka carik nanem padi uli tuning semengan",
    "Memene ketut bagus ka yogyakarta ngatehin adine"
]

# Valid Sentences:
# (S) titiang  (P) sampun meblanja 
# (S) i putu dangin punika  (P) sesai melajah  (O) megambal    
# (S) adik tiange (P) kapah melali (Ket) ka umah timpalne      
# (S) sepedane wayan darta (P) sesai anggone (Pel) ngatehin bapane (Ket) ka carik
# (S) ketua pasar punika (P) sampun rauh (Ket) saking tuni semeng  
# (S) bapakne i putu gede punika (P) pinaka (Pel) guru olahraga (Ket) di sekolah tiange 
# (S) adin tiange (P) sampun dados (Pel) mahasiswa baru (Ket) ring kampus udayana jimbaran
# (S) ragane (P) sampun mekarya (Ket) saking semeng pisan  
# (S) dane (P) setata manting (O) baju akeh pisan (Ket) ka tukad unda 
# (S) bapan ipune (P) sampun dados (Pel) balian sakti (Ket) saking sue pisan   

# Invalid Sentences:
# (S) ibu guru tiange (P) galak pisan (Pel) ngajahin matematika  
# (S) anake luh jegeg punika (P) dueg pisan (Pel) mekarya wewantenan  
# (S) pianakne pak guru ento (P) seleg pisan (Pel) melajah komputer (Ket) di sekolah  
# (S) bapakne i putu gede (P) guru olahraga (Ket) di sekolah tiange  
# (S) ibu puspa punika (P) dosen matematika (Pel) sane jegeg (Ket) ring kampus timpal tiange  
# (S) nasi goreng punika (P) ajengan (Pel) sane paling demenin tiang  
# (S) sepeda baru adin tiange (P) telung pasang (Pel) lakar abane (Ket) ka kota surabaya  
# (S) sepeda motorne (P) dadue (Pel) luung pati 
# (S) bapan tiange (P) ka carik (Pel) nanem padi (Ket) uli tuning semengan 
# (S) memene ketut bagus (P) ka yogyakarta (Pel) ngatehin adine 