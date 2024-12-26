# Class 
class Buku:
    # Instance
    def __init__(self, pd):
        self.pd = pd
        self.Judul = ""
        self.Pengarang = ""
        self.Tahunterbit = ""

    # Method 1
    def printBuku(self):
        print("Judul Buku : ", self.Judul)
        print("Pengarang Buku : ", self.Pengarang)
        print("Tahun Terbit Buku : ", self.Tahunterbit)
    
    # Method 2
    def Her(self, kondisi):
        print("Cek Buku")
        print(kondisi)

# Objek
buku1 = Buku("Romance")
buku2 = Buku("Fantasy")

# Value
buku1.Judul = "Winter In Tokyo"
buku1.Pengarang = "Ilana Tan"
buku1.Tahunterbit = "24 Oktober 2014"
buku2.Judul  = "Harry Potter and The Cursed Child"
buku2.Pengarang = "J. K. Rowling"
buku2.Tahunterbit = "31 Juli 2016"
# Pemanggilan Method
buku1.printBuku()
buku1.Her("Buku Tersedia")
buku2.printBuku()
buku2.Her("Buku Tersedia")