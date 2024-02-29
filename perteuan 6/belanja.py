product = {
    "beras": 10000,
    "gula": 12500,
    "telur": 35000,
    "susu": 19000,
}

def belanja():
    print("selamat datang, selamat belanja")
    print("berikut adalah daftar barang yg tersedia")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per kg")

    total_belanja = 0 
    while True:
        barang_dipilih = input("masukkan nama barang yg ingin anda beli(atau 'selesai' untuk selesai)")
        if barang_dipilih.lower() == 'selesai':
            break

        if barang_dipilih not in product:
            print("maaf, barang tersebut tdk tersedia")
        jumlah = float(input(f"berapa kg {barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total belanja anda adalah: rp{total_belanja}")

belanja()