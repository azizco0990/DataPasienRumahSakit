# Inisialisasi daftar pasien
daftar_pasien = [{"ID Pasien": 101, "Nama": "Aziz", "Umur": 22, "Jenis Kelamin": "Pria" ,"Alamat": "Jl Kalijudan", "Penyakit": "Demam" },
                 {"ID Pasien": 102, "Nama": "Yani", "Umur": 24, "Jenis Kelamin": "Pria" ,"Alamat": "Jl Mulyorejo", "Penyakit": "Flu" },
                 {"ID Pasien": 103, "Nama": "Umam", "Umur": 23, "Jenis Kelamin": "Pria" ,"Alamat": "Jl Kalidami", "Penyakit": "Panas" },
                 {"ID Pasien": 104, "Nama": "Azizah", "Umur": 20, "Jenis Kelamin": "Perempuan" ,"Alamat": "Jl Sutorejo", "Penyakit": "Panas" },
                 {"ID Pasien": 105, "Nama": "Ayu", "Umur": 21, "Jenis Kelamin": "Perempuan" ,"Alamat": "Jl Mulyosari", "Penyakit": "Flu" }]

# Fungsi untuk menambahkan pasien baru
def tambah_pasien():
    while True:
        id = input("Masukkan ID pasien (integer): ")
        if id.isdigit():
            id = int(id)
            break
        else:
            print("Masukkan hanya angka untuk ID.")
    nama = input("Masukkan Nama pasien: ")
    while True:
        umur = input("Masukkan umur pasien (integer): ")
        if umur.isdigit():
            umur = int(umur)
            break
        else:
            print("Masukkan hanya angka untuk umur.")
    jenis_kelamin = input("Masukkan Jenis Kelamin Pasien: ")
    alamat = input("Masukkan Alamat pasien: ")
    penyakit = input("Masukkan Penyakit pasien: ")
    pasien = {"ID Pasien": id, "Nama": nama, "Umur": umur, "Jenis Kelamin": jenis_kelamin ,"Alamat": alamat, "Penyakit": penyakit }
    daftar_pasien.append(pasien)
    print("Data Pasien berhasil ditambahkan.")

# Fungsi untuk menampilkan semua pasien
def tampilkan_pasien():
    if not daftar_pasien:
        print("Belum ada pasien terdaftar.")
    else:
        print("Daftar Pasien:")
        for idx, pasien in enumerate(daftar_pasien, 1):
            print(f"{idx}. ID Pasien: {pasien['ID Pasien']}, Nama: {pasien['Nama']}, Umur: {pasien['Umur']}, Jenis Kelamin: {pasien['Jenis Kelamin']}, Alamat: {pasien['Alamat']}, Penyakit: {pasien['Penyakit']}")

# Fungsi untuk menampilkan data pasien berdasarkan kriteria
def tampilkan_data_kriteria(kriteria):
    if not daftar_pasien:
        print("Belum ada pasien terdaftar.")
        return

    if kriteria == 'id':
        id = input("Masukkan ID Pasien yang ingin dicari: ")
        hasil_pencarian = [pasien for pasien in daftar_pasien if pasien['ID Pasien'] == int(id)]
    elif kriteria == 'nama':
        nama = input("Masukkan Nama yang ingin dicari: ")
        hasil_pencarian = [pasien for pasien in daftar_pasien if pasien['Nama'].lower() == nama.lower()]
    elif kriteria == 'jenis kelamin':
        jenis_kelamin = input("Masukkan Jenis Kelamin yang ingin dicari: ")
        hasil_pencarian = [pasien for pasien in daftar_pasien if pasien['Jenis Kelamin'].lower() == jenis_kelamin.lower()]
    elif kriteria == 'penyakit':
        penyakit = input("Masukkan Penyakit yang ingin dicari: ")
        hasil_pencarian = [pasien for pasien in daftar_pasien if pasien['Penyakit'].lower() == penyakit.lower()]
    else:
        print("Kriteria tidak valid.")
        return

    if not hasil_pencarian:
        print(f"Tidak ditemukan data pasien dengan {kriteria} tersebut.")
    else:
        print(f"Hasil Pencarian berdasarkan {kriteria}:")
        for idx, pasien in enumerate(hasil_pencarian, 1):
            print(f"{idx}. ID Pasien: {pasien['ID Pasien']}, Nama: {pasien['Nama']}, Umur: {pasien['Umur']}, Jenis Kelamin: {pasien['Jenis Kelamin']}, Alamat: {pasien['Alamat']}, Penyakit: {pasien['Penyakit']}")

# Fungsi untuk menampilkan Data berdasarkan urutan Nama
def tampilkan_pasien_by_nama():
    new_daftar_pasien = daftar_pasien.copy()
    n = len(new_daftar_pasien)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if new_daftar_pasien[j]["Nama"] > new_daftar_pasien[j + 1]["Nama"]:
                new_daftar_pasien[j], new_daftar_pasien[j + 1] = new_daftar_pasien[j + 1], new_daftar_pasien[j]
    for idx, pasien in enumerate(new_daftar_pasien, 1):
        print(f"{idx}. ID Pasien: {pasien['ID Pasien']}, Nama: {pasien['Nama']}, Umur: {pasien['Umur']}, Jenis Kelamin: {pasien['Jenis Kelamin']}, Alamat: {pasien['Alamat']}, Penyakit: {pasien['Penyakit']}")

# Fungsi untuk menampilkan Data berdasarkan urutan Umur
def tampilkan_pasien_by_umur():
    new_daftar_pasien = daftar_pasien.copy()
    n = len(new_daftar_pasien)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if new_daftar_pasien[j]["Umur"] > new_daftar_pasien[j + 1]["Umur"]:
                new_daftar_pasien[j], new_daftar_pasien[j + 1] = new_daftar_pasien[j + 1], new_daftar_pasien[j]
    for idx, pasien in enumerate(new_daftar_pasien, 1):
        print(f"{idx}. ID Pasien: {pasien['ID Pasien']}, Nama: {pasien['Nama']}, Umur: {pasien['Umur']}, Jenis Kelamin: {pasien['Jenis Kelamin']}, Alamat: {pasien['Alamat']}, Penyakit: {pasien['Penyakit']}")

# Fungsi untuk mengupdate data pasien
def update_pasien():
    tampilkan_pasien()
    if not daftar_pasien:
        return
    nomor_pasien = int(input("Masukkan nomor pasien yang ingin diupdate: ")) - 1
    if 0 <= nomor_pasien < len(daftar_pasien):
        pasien = daftar_pasien[nomor_pasien]
        print("Data Pasien yang akan diupdate:")
        print(f"ID Pasien: {pasien['ID Pasien']}, Nama: {pasien['Nama']}, Umur: {pasien['Umur']}, Jenis Kelamin: {pasien['Jenis Kelamin']} ,Alamat: {pasien['Alamat']}, Penyakit: {pasien['Penyakit']}")
        id = int(input("Masukkan ID baru(Wajib angka, kosongkan jika tidak ingin mengubah): "))
        nama = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
        umur = int(input("Masukkan umur baru (Wajib angka, kosongkan jika tidak ingin mengubah): "))
        jenis_kelamin = input("Masukkan jenis kelamin baru (kosongkan jika tidak ingin mengubah): ")
        alamat = input("Masukkan alamat baru (kosongkan jika tidak ingin mengubah): ")
        penyakit = input("Masukkan penyakit baru (kosongkan jika tidak ingin mengubah): ")
        if id:
            pasien["ID Pasien"] = id
        if nama:
            pasien['Nama'] = nama
        if umur:
            pasien['Umur'] = umur
        if jenis_kelamin:
            pasien['Jenis Kelamin'] = jenis_kelamin
        if alamat:
            pasien['Alamat'] = alamat
        if penyakit:
            pasien['Penyakit'] = penyakit
        print("Data pasien berhasil diupdate.")
    else:
        print("Nomor pasien tidak valid.")

# Fungsi untuk menghapus data pasien
def hapus_pasien():
    tampilkan_pasien()
    if not daftar_pasien:
        return
    nomor_pasien = int(input("Masukkan nomor pasien yang ingin dihapus: ")) - 1
    if 0 <= nomor_pasien < len(daftar_pasien):
        pasien = daftar_pasien[nomor_pasien]
        print("Data Pasien yang akan dihapus:")
        print(f"Nama: {pasien['Nama']}, Umur: {pasien['Umur']}, Alamat: {pasien['Alamat']}")
        konfirmasi = input("Apakah Anda yakin ingin menghapus data pasien ini? (y/n): ")
        if konfirmasi.lower() == 'y':
            daftar_pasien.pop(nomor_pasien)
            print("Data pasien berhasil dihapus.")
    else:
        print("Nomor pasien tidak valid.")

# Fungsi utama untuk menjalankan program
def main():
    while True:
        print("\nAplikasi Manajemen Data Pasien Rumah Sakit")
        print("1. Tambah Pasien")
        print("2. Tampilkan Pasien")
        print("3. Update Pasien")
        print("4. Hapus Pasien")
        print("5. Keluar")
        
        pilihan = input("Pilih operasi (1/2/3/4/5): ")
        
        if pilihan == '1':
            tambah_pasien()
        elif pilihan == '2':
            print("1. Tampilkan Seluruh Data")
            print("2. Tampilkan Data Berdasarkan ID Pasien")
            print("3. Tampilkan Data Berdasarkan Nama")
            print("4. Tampilkan Data Berdasarkan Jenis Kelamin")
            print("5. Tampilkan Data Berdasarkan Penyakit")
            sub_pilihan = input("Pilih sub-operasi (1/2/3/4/5): ")
            if sub_pilihan == '1':
                print("1. Tampilkan Semua Data Tanpa Urutan")
                print("2. Tampilkan Semua Data dengan Urutan Nama")
                print("3. Tampilkan Semua Data dengan Urutan Umur")
                sub_pilihan2 = input("Pilih sub-operasi (1/2/3): ")
                if sub_pilihan2 == "1":
                    tampilkan_pasien()
                elif sub_pilihan2 == "2":
                    tampilkan_pasien_by_nama()
                elif sub_pilihan2 == "3":
                    tampilkan_pasien_by_umur()
                
            elif sub_pilihan == '2':
                tampilkan_data_kriteria('id')
            elif sub_pilihan == '3':
                tampilkan_data_kriteria('nama')
            elif sub_pilihan == '4':
                tampilkan_data_kriteria('jenis kelamin')
            elif sub_pilihan == '5':
                tampilkan_data_kriteria('penyakit')
            else:
                print("Pilihan tidak valid.")
        elif pilihan == '3':
            update_pasien()
        elif pilihan == '4':
            hapus_pasien()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")

main()