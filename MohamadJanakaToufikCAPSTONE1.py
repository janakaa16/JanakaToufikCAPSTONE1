data = {
    "00001":{
        "nama" : "Arthur Morgan",
        "kelamin": "laki-laki",
        "divisi" : "HR",
        "jabatan": "Supervisor"
    },
    "00002":{
        "nama" : "Dutch Van Der Linde",
        "kelamin" : "Laki-laki",
        "divisi" : "Finance",
        "jabatan" :"Manager"
    },
    "00003":{
        "nama" : "Saddie Adler ",
        "kelamin": "Perempuan",
        "divisi": "Marketing",
        "jabatan": "Staff"
    }
}

def Menampilkan():
    print(f"ID\t\tNama\t\t Kelamin\t Divisi \t Jabatan")
    for i in data:
        print(f'{i}|{data[i]["nama"]:15}    \t|{data[i]["kelamin"]}\t|{data[i]["divisi"]}     \t|{data[i]["jabatan"]}')

def submenampilkan():
    print("1.Tampilkan semua data\n2.Cari Karyawan\n3.Kembali")
    subpilih = int(input("Masukan pilihan anda= "))
    if subpilih == 1:
        Menampilkan()
        submenampilkan()
    elif subpilih == 3:
        main()
    elif subpilih == 2:
        xkaryawan = (input("Masukan ID karyawan= "))
        if xkaryawan in data:
            print(data[xkaryawan])
            submenampilkan()
        else:
            print("Data tidak ditemukan")
            submenampilkan()
    else:
        print("Input salah")
        submenampilkan()

def hapus():
    print("1.Hapus data karyawan\n2.Kembali")
    subhapus = input("Masukan pilihan anda= ")
    if subhapus == "1":
        subsubhapus = input("Masukan ID karyawan: ")
        if subsubhapus in data:
            print("Apakah ingin menghapus data \n1.Iya\n2.Tidak")
            yakinhapus = input("Masukan pilihan anda: ")
            if yakinhapus == "1":
                data.pop(subsubhapus)
                print("Data telah terhapus")
                hapus()
            elif yakinhapus == "2":
                hapus()
            else:
                print("Input anda salah")
                hapus()
        else:
            print("Data tidak ditemukan")
            hapus()

    else:
        main()
def Menambahkan():
    print("1.Tambah data\n2.Kembali")
    subtambah = input("Masukan pilihan anda: ")
    if subtambah == "1":
        kode_baru = input("Masukkan ID karyawan: ")
        if kode_baru in data.keys():
            print("Karyawan sudah ada")
            Menambahkan()
        else:
            nama_baru = input("Masukkan nama karyawan\t:")
            kelaminbaru = input("Masukkan jenis kelamin\t:")
            divisibaru = input("Masukkan divisi\t:")
            jabatanbaru = input("Masukan jabatan\t:")
            data.update(
           {kode_baru : {
                "nama" : nama_baru,
                "kelamin" : kelaminbaru,
                "divisi" : divisibaru,
                "jabatan" : jabatanbaru
            }
           }
        )
        print("Apakah ingin menyimpan data ? \n1.Iya\n2.Tidak")
        subsubtambah = input("Masukan pilihan anda: ")
        if subsubtambah == "1":
            print("Data telah tersimpan")
            Menambahkan()
        elif subsubtambah =="2":
            data.pop(kode_baru)
            Menambahkan()
    elif subtambah == "2":
        main()
    else:
        print("Input anda salah")
        Menambahkan()

def update():
    print("1.Update data karyawan \n2.Kembali")
    subupdate = input("Masukan pilihan anda: ")
    if subupdate == "1":
        subsubupdate= input("Masukan ID karyawan: ")
        if subsubupdate in data:
            subsubsubupdate = input("Masukan kolom yang ingin diupdate: ")
            z = subsubsubupdate.lower()
            databaru = input(f"Masukan {subsubsubupdate} baru: ")
            print("Apakah ingin update data \n1.Iya\n2.Tidak")
            yakinupdate = input("Masukan pilihan anda: ")
            if yakinupdate == "1":
                data[subsubupdate][z] = databaru
                print("Data telah terupdate")
                update()
            elif yakinupdate == "2":
                update()
            else:
                print("Input anda salah")
                update()
        else:
            print("Data tidak ditemukan")
            update()
            
    elif subupdate == "2":
        main()
    else:
        print("Input anda salah")
        update()




def main(): 
    print(''' SELAMAT DATANG DI DATABASE KARYAWAN PT G-CORP
    1. Tampilkan data karyawan.
    2. Menambah data karyawan.
    3. Update data karyawan.
    4. Hapus data karyawan.
    5. Keluar
    ''')
    x = input("Masukan pilihan anda= ")
    if x == "5":
        exit = input("Apakah anda yakin ingin keluar? \n1.Iya\n2.Tidak\nMasukan pilihan =   ")
        if exit == "1":
            print("Terimakasih")
        elif exit =="2":
            main()
        else:
            print("Input yang anda masukan salah")
            main()
    elif x =="1":
        submenampilkan()
    elif x == "4":
        hapus()
    elif  x == "2":
        Menambahkan()
    elif x == "3":
        update()
    else:
        print("Input anda salah")
        main()
        

main()