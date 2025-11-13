# Inventaris awal toko Anda
inventaris_toko = {
    "Laptop": {"stok": 15, "harga": 8500000.0},
    "Mouse Wireless": {"stok": 50, "harga": 150000.0},
    "Keyboard Mekanik": {"stok": 20, "harga": 700000.0}
}

def cek_ketersediaan(nama_barang, jumlah_beli, inventaris):
    # cek dulu apakah nama_barang ada di inventaris
    # kalau tidak ada, return False
    barang = inventaris.get(nama_barang)
    print(barang)
    if(barang == None):
        print(barang +" tidak tersedia")
        return False

    # kalau ada, cek dan return jumlah_beli < stok
    return jumlah_beli <= barang.get("stok")

print("Ada yang mau beli mouse 3 pcs, apakah tersedia?")
print(cek_ketersediaan("Mouse Wireless", 300, inventaris_toko))