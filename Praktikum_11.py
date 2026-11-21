import datetime
import os
import random
import string

print("===Program 11.1 Multi keys & Nesting Dictionary===")

mahasiswa1 = {
    "nama": "Ucup Surucup",
    "nim": "19022001",
    "sks_lulus": 130,
    "beasiswa": False,
    "lahir": datetime.datetime(2001, 4, 10),
}
mahasiswa2 = {
    "nama": "Azan Magrib",
    "nim": "19022002",
    "sks_lulus": 140,
    "beasiswa": True,
    "lahir": datetime.datetime(2002, 10, 10),
}
mahasiswa3 = {
    "nama": "Slamet Dunia Akhirat",
    "nim": "19022003",
    "sks_lulus": 100,
    "beasiswa": True,
    "lahir": datetime.datetime(1977, 5, 10),
}

data_mahasiswa = {
    "MAH001": mahasiswa1,
    "MAH002": mahasiswa2,
    "MAH003": mahasiswa3,
}

print(f"{"KEY":<6} {"Nama":<17} {"SKS":<3} {"Beasiswa":<9} {"Lahir":<10}")
print("-" * 50)

for mahasiswa in data_mahasiswa:
    key = mahasiswa
    nama = data_mahasiswa[key]["nama"]
    nim = data_mahasiswa[key]["nim"]
    sks = data_mahasiswa[key]["sks_lulus"]
    beasiswa = data_mahasiswa[key]["beasiswa"]
    lahir = data_mahasiswa[key]["lahir"].strftime("%x")
    print(f"{key:<6} {nama:<17} {sks:<3} {beasiswa:<9} {lahir:<10}")

print("===Program 11.2 Latihan Dictionary Bagian 1===")

mahasiswa_template = {
    "nama": "nama",
    "nim": 00000000,
    "sks_lulus": 0,
    "lahir": datetime.datetime(1111,1,11),
}

data_mahasiswa = {}

print(f"{"SELAMAT DATANG":^20}")
print(f"{"DATA MAHASISWA":^20}")
print("-" * 20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa["nama"] = input("Nama Mahasiswa: ")
mahasiswa["nim"] = input("NIM Mahasiswa: ")
mahasiswa["sks_lulus"] = int(input("SKS Lulus: "))
tahun_lahir = int(input("Tahun lahir (YYYY): "))
bulan_lahir = int(input("Bulan lahir (1-12): "))
tanggal_lahir = int(input("Tanggal lahir (1-31): "))
mahasiswa["lahir"] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

print(mahasiswa)

print("===Program 11.3 Latihan Dictionary Bagian 2===")

mahasiswa_template = {
    "nama": "nama",
    "nim": "00000000",
    "sks_lulus": 0,
    "lahir": datetime.datetime(1111, 1, 11),
}

data_mahasiswa = {}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{"SELAMAT DATANG":^20}")
    print(f"{"DATA MAHASISWA":^20}")
    print("-" * 20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa["nama"] = input("Nama Mahasiswa: ")
    mahasiswa["nim"] = input("NIM Mahasiswa: ")
    mahasiswa["sks_lulus"] = int(input("SKS Lulus: "))
    tahun_lahir = int(input("Tahun lahir (YYYY): "))
    bulan_lahir = int(input("Bulan lahir (1-12): "))
    tanggal_lahir = int(input("Tanggal lahir (1-31): "))
    mahasiswa["lahir"] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

    key = "".join(random.choice(string.ascii_uppercase) for _ in range(6))
    data_mahasiswa[key] = mahasiswa

    print(f"{"KEY":<6} {"Nama":<17} {"NIM":<8} {"SKS Lulus":<10} {"Tanggal Lahir":<10}")
    print("-" * 60)

    for mahasiswa_key in data_mahasiswa:
        nama = data_mahasiswa[mahasiswa_key]["nama"]
        nim = data_mahasiswa[mahasiswa_key]["nim"]
        sks = data_mahasiswa[mahasiswa_key]["sks_lulus"]
        lahir = data_mahasiswa[mahasiswa_key]["lahir"].strftime("%x")
        print(f"{mahasiswa_key:<6} {nama:<17} {nim:<8} {sks:^10} {lahir:^10}")

    print()
    is_done = input("Mau tambah lagi bro (y/n)? ")
    if is_done.lower() == "n":
        break

print("\nAkhir dari program, terima kasih")