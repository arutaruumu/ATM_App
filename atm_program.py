import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
  id = int(input("Masukan pin anda: "))
  trial = 0
  
  while (id != int(atm.checkPin()) amd trial < 3):
    id = int(input("Pin anda salah. Silakan masukan lagi: "))
    trial += 1
    if trial == 3:
      print("Error. Silakan ambil kartu dan coba lagi..")
      exit()
    while True:
      print("Selamat datang di ATM Progate..")
      print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
      selectmenu = int(input("\nSilakan pilih menu: ")
    if selectmenu == 1:
      print("\nSaldo anda sekarang: Rp. " + str(atm.checkBalance()) + "\n")
    elif selectmenu == 2:
      nominal = float(input("Masukan nominal saldo: "))
      verify_withdraw = input("Konfirmasi: Anda akan melakukan debit dengan nominal berikut ? y/n " + str(nominal) + " ")
      if verify_withdraw == "y":
        print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + "")
      else:
        break
      if nominal < atm.checkBalance():
        atm.withdrawBalance(nominal)
        print("Transaksi debet berhasil!")
        print("Saldo sisa sekarang: Rp. " + str(atm.checkBalance()) + "")
      else:
        print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
        print("Silakan lakukan penambahan nominal saldo")
                       
