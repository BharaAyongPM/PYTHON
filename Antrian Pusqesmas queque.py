#program antrian Puskesmas
import os
import queue


class antrian:
    def __init__(self):
        self.items = queue.Queue()

    # periksa kosong
    def isEmpty(self):
        return self.items.empty()

    # Menambah data pasien
    def qPut(self, item):
        self.items.put(item)

    # Mengeluarkan data pasien
    def qGet(self):
        if not self.items.empty():
            return self.items.get()
        else:
            return "empty"
            # Menghitung jumlah pasien

    def size(self):
        return self.items.qsize()

    # Main menu aplikasi
    def menu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("cls")
            print("=============================================")
            print("                PROGRAM ANTRIAN              ")
            print("           PUSKESMAS DESA BAKTI MULYA        ")
            print("=============================================")
            print("1. Masukan Nama Pasien ")
            print("2. Panggil Pasien")
            print("3. Cek Jumlah Total Antrian")
            print("=========================")
            pilihan = str(input(("Silakan masukan pilihan anda [1-3] : ")))
            if pilihan == "1" :
                os.system("cls")
                obj = str(input("Masukan Nama Pasien: "))
                self.qPut(obj)
                print("Pasien  " + obj + " telah ditambahkan")
                x = input("")

            elif pilihan == "2":
                os.system("cls")
                temp = self.qGet()
                if temp != "empty":
                    print("Pasien  " + temp + " Dipanggil")
                else:
                    print("Antrian Kosong")
                x = input("")

            elif pilihan == "3":
                os.system("cls")
                print("Total antrian Pasien Adalah: " + str(self.size()))
                x = input("")
            else:
                print("Anda Salah memasukan Angka")


if __name__ == "__main__":
    q = antrian()
    q.menu()
