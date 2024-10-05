class DaftarMenu:
    def __init__(self):
        # dictionary untuk menyimpan menu dan harga
        self.menu_makanan = {} 
        self.menu_minuman = {}   
    
    # Menambahkan makanan ke daftar menu
    def tambah_makanan(self, makanan, harga):
        self.menu_makanan[makanan] = harga
        print(f"{makanan} telah ditambahkan ke daftar menu makanan dengan harga Rp {harga}.")
  
    def tambah_minuman(self, minuman, harga):
        self.menu_minuman[minuman] = harga
        print(f"{minuman} telah ditambahkan ke daftar menu minuman dengan harga Rp {harga}.")
    
    def tampilkan_menu_makanan(self):
        if self.menu_makanan:
            print("\nDaftar Menu Makanan:")
            for makanan, harga in self.menu_makanan.items():
                print(f"- {makanan} ==> Rp {harga}")
        else:
            print("Belum ada makanan di daftar menu.")
    
    # Menampilkan daftar menu minuman
    def tampilkan_menu_minuman(self):
        if self.menu_minuman:
            print("\nDaftar Menu Minuman:")
            for minuman, harga in self.menu_minuman.items():
                print(f"- {minuman} ==> Rp {harga}")
        else:
            print("Belum ada minuman di daftar menu.")
    
    # Menampilkan semua menu (makanan dan minuman)
    def tampilkan_semua_menu(self):
        print("\n--- Daftar Menu ---")
        self.tampilkan_menu_makanan()
        self.tampilkan_menu_minuman()


def main():
    menu = DaftarMenu()
    
    while True:
        print("\nMenu Pilihan:")
        print("1. Tambah Makanan ==> ")
        print("2. Tambah Minuman ==> ")
        print("3. Tampilkan Daftar Menu Makanan ==> ")
        print("4. Tampilkan Daftar Menu Minuman ==> ")
        print("5. Tampilkan Semua Menu ==> ")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6) ==> ")

        if pilihan == '1':
            makanan = input("Masukkan nama makanan ==> ")
            harga = input("Masukkan harga makanan (tanpa Rp)==> ")
            try:
                harga = int(harga)
                menu.tambah_makanan(makanan, harga)
            except ValueError:
                print("Harga harus berupa angka.")
        elif pilihan == '2':
            minuman = input("Masukkan nama minuman ==> ")
            harga = input("Masukkan harga minuman (tanpa Rp) ==> ")
            try:
                harga = int(harga)
                menu.tambah_minuman(minuman, harga)
            except ValueError:
                print("Harga harus berupa angka.")
        elif pilihan == '3':
            menu.tampilkan_menu_makanan()
        elif pilihan == '4':
            menu.tampilkan_menu_minuman()
        elif pilihan == '5':
            menu.tampilkan_semua_menu()
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
