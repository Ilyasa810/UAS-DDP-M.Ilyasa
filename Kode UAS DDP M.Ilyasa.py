from prettytable import PrettyTable
from datetime import datetime
import os
import pwinput
os.system("cls")

users = {
    "Member": {"pass": "1234", "type": "Biasa", "Gems": 200, "voucher_used": False},
    "VIP": {"pass": "9999", "type": "VIP", "Gems": 500, "voucher_used": False}
}

items_pagi = {"Smart Lamp": 50, "Smart Vaccum Cleaner": 200, "Earbuds": 250}
items_siang = {"HP": 300, "Laptop Gaming": 350, "PS 5": 500}
items_malam = {"LCD Projector": 200, "Headphone": 130, "Board game": 99}

def login():
    percobaan = 0
    while percobaan < 3:
        username = input("Masukkan Username: ")
        password = pwinput.pwinput("Masukkan Password: ")
        if username in users and users[username]["pass"] == password:
            print(f"Login Berhasil, Selamat Datang {username} ({users[username]['type']})")
            return username
        else:
            print("Username atau password salah, silahkan coba lagi.")
            percobaan += 1
            if percobaan == 3:
                print("Akun Anda terkunci setelah gagal dalam 3 kali percobaan login.")
                return None
    return None

def tampilkan_barang(waktu_hari):
    table = PrettyTable()
    table.field_names = ["Nama Barang", "Harga"]

    for item, harga in barang(waktu_hari).items():
        table.add_row([item, harga])
    print(table)

def barang(waktu_hari):
    if waktu_hari == "pagi":
        return items_pagi
    elif waktu_hari == "siang":
        return items_siang
    elif waktu_hari == "malam":
        return items_malam

def top_up(username):
    MAX_TOP_UP = 1000  # Batas maksimum top up
    print("=" * 20)
    print(f"Saldo Gems Anda saat ini: {users[username]['Gems']}")
    amount = int(input("Masukkan jumlah Gems yang ingin ditambahkan: "))

    if amount > MAX_TOP_UP:
        print(f"Jumlah yang ingin ditambahkan melebihi batas maksimum {MAX_TOP_UP} Gems. Silakan coba lagi.")
        return

    users[username]['Gems'] += amount
    print("=" * 20)
    print(f"Top up berhasil! Saldo Gems Anda sekarang: {users[username]['Gems']}")


def beli(username):
    waktu_hari = waktu_sekarang()
    print(f"Saldo Gems anda sisa: {users[username]['Gems']}")
    print("=" * 20)
    print(f"Barang yang tersedia di {waktu_hari}:")
    print("=" * 20)
    tampilkan_barang(waktu_hari)

    item = input("Masukkan nama barang yang ingin dibeli (dengan sesuai): ")
    if item in barang(waktu_hari):
        harga = barang(waktu_hari)[item]
        print("=" * 20)
        print(f"Harga {item}: {harga}")
        print("=" * 20)
        print(f"Saldo Gems anda sisa: {users[username]['Gems']}")

        if users[username]["Gems"] >= harga:
            users[username]["Gems"] -= harga
            print("=" * 20)
            print(f"Pembelian {item} berhasil !! Harga akhir: {harga}")
        else:
            print("Saldo tidak cukup untuk transaksi ini.")
            return

        if not users[username]["voucher_used"]:
            pakai_voucher = input("Apakah Anda ingin menggunakan voucher Anda? (y/n): ")
            if pakai_voucher.lower() == "y":
                # Tentukan diskon berdasarkan tipe member
                if users[username]["type"] == "Biasa":
                    diskon = harga * 0.2  # 20% untuk member biasa
                elif users[username]["type"] == "VIP":
                    diskon = harga * 0.5  # 50% untuk member VIP

                harga -= diskon
                users[username]["voucher_used"] = True
                print("=" * 20)
                print(f"Selamat, voucher Anda telah terpakai. Harga setelah diskon: {harga}")
                print("=" * 20)
                print(f"Pembelian {item} berhasil !! Harga akhir setelah diskon: {harga}")
                print("=" * 20)
    else:
        print("Barang tidak tersedia :( ")

def waktu_sekarang():
    jam = datetime.now().hour
    if 1 <= jam < 12:
        return "pagi"
    elif 12 <= jam < 18:
        return "siang"
    else:
        return "malam"

def main():
    print("<< SELAMAT DATANG DI M.Ilyasa810 store >> ")
    username = login()
    if username:
        table = PrettyTable()
        table.field_names = ["No", "Menu"]
        pilihan_menu = [
            ["1", "Lihat Barang dan Belanja"],
            ["2", "Top Up Saldo Gems"],
            ["3", "Keluar"]
        ]
        for option in pilihan_menu:
            table.add_row(option)

        while True:
            print(table)
            pilihan = int(input("Silahkan memilih menu yang diinginkan (1/2/3) = "))
            if pilihan == 1:
                beli(username)
            elif pilihan == 2:
                top_up(username)
            elif pilihan == 3:
                print("TerimaKasih dan Selamat Tinggal")
                break
            else:
                print("Pilihan tidak valid.")
    else:
        print("Login gagal, keluar dari aplikasi.")

main()
