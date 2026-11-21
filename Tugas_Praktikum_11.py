import datetime
import os
import random
import string

# 1. Template dictionary (Multi-keys)
template_buku = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun': 0000,
    'terakhir_pinjam': datetime.datetime(1111, 1, 1),
    'status': 'TERSEDIA',
}

# Dictionary utama untuk menampung semua data (Nesting dictionary)
data_perpustakaan = {}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^75}")
    print('=' * 75)

    # 2. Input data buku baru berdasarkan template
    buku = dict.fromkeys(template_buku.keys())

    buku['judul'] = input('Judul Buku\t\t: ')
    buku['penulis'] = input('Penulis\t\t\t: ')
    buku['tahun'] = int(input('Tahun Terbit\t\t: '))

    tahun_pinjam = int(input('Tahun Terakhir Pinjam\t: '))
    bulan_pinjam = int(input('Bulan Terakhir Pinjam\t: '))
    tanggal_pinjam = int(input('Tanggal Terakhir Pinjam\t: '))
    buku['terakhir_pinjam'] = datetime.datetime(
        tahun_pinjam, bulan_pinjam, tanggal_pinjam)

    buku['status'] = input('Status (TERSEDIA/TIDAK)\t: ').upper()

    # 3. Membuat KEY acak unik (6 huruf kapital) dan menyimpannya ke Nesting Dictionary
    while True:
        KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
        if KEY not in data_perpustakaan:
            break
    data_perpustakaan.update({KEY: buku})

    # 4. Menampilkan seluruh data buku dalam bentuk tabel
    print(
        f"\n{'KEY':<8} {'JUDUL BUKU':<20} {'PENULIS':<15} {'TAHUN':<6} "
        f"{'TERAKHIR PINJAM':<16} {'STATUS':<10}"
    )
    print('-' * 80)

    for key in data_perpustakaan:
        KEY_BUKU = key
        JUDUL = data_perpustakaan[key]['judul']
        PENULIS = data_perpustakaan[key]['penulis']
        TAHUN = data_perpustakaan[key]['tahun']
        TANGGAL = data_perpustakaan[key]['terakhir_pinjam'].strftime('%x')
        STATUS = data_perpustakaan[key]['status']

        print(
            f'{KEY_BUKU:<8} {JUDUL:<20} {PENULIS:<15} {TAHUN:<6} {TANGGAL:<16}'
            f' {STATUS:<10}'
        )

    print('\n')
    lanjut = input('Apakah ingin menambah buku lagi? (y/n): ')
    if lanjut.lower() == 'n':
        break

print('\nProgram selesai. Terima kasih!')
