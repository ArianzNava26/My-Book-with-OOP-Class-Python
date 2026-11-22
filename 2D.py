print('Kita Coba Lagi')
print()
print()

## KITA BUAT CLASS NYA DAHULU
class DaftarBukuku:
    def __init__(self,judul,stok):
        self.judulnya = judul
        self.stoknya = stok


## INISIASI YUK
bukupertamaku = DaftarBukuku('Ternyata Aku Berharga',20)
bukukeduaku = DaftarBukuku('Aku Cepirit Gak Ya',25)
bukuketigaku = DaftarBukuku('Cebok itu Penting',22)


## KITA BERIKAN INFORMASI, SEKALIGUS UJICOBA DATA
print(f'Jadi Judul Buku pertama: {bukupertamaku.judulnya} ')
print(f'Stok buku {bukupertamaku.judulnya} adalah {bukupertamaku.stoknya} ')
print(f'Sementara buku Keduaku adalah: {bukukeduaku.judulnya} ')
print(f'dan Stok {bukukeduaku.judulnya} adalah {bukukeduaku.stoknya} ')
print(f'Satu buku yang Saya yang bernama: {bukuketigaku.judulnya} , menurutmu Judulnya Kurang Kerjaan Gak? ')
print()
print()

## KITA MASUKAN KE VARIABEL BARU UNTUK MEMPERMUDAH KEDEPANNYA!
stok1 = bukupertamaku.stoknya
stok2 = bukukeduaku.stoknya
stok3 = bukuketigaku.stoknya

## KITA UJICOBA VARIABEL YANG BARU KITA BUAT
print(f'Saat ini stok nya adalah buku pertama : {stok1}, buku kedua: {stok2} dan buku ketiga: {stok3} ')


## DISINI KITA BUTUH LOOPING
cobayuk = True

while cobayuk:

    ## KITA TANYA TAMBAH ATAU KURANG KEPADA USER
    #
    tanya = str(input('Mau Nambah apa kurang? '))

    ## SETELAHNYA KITA BUAT LOGIKA NYA
    if tanya == 'nambah':
        judulnya = str(input('Buku yang mana? '))
        berapa = int(input('Berapa? '))
        if judulnya == '1':
            stok1 = stok1 + berapa
        elif judulnya == '2':
            stok2 = stok2 + berapa
        elif judulnya == '3':
            stok3 = stok3 + berapa

    elif tanya == 'kurang':
        judulnya = str(input('Buku yang mana? '))
        berapa = int(input('Berapa? '))
        if judulnya == '1':
            stok1 = stok1 - berapa
        elif judulnya == '2':
            stok2 = stok2 - berapa
        elif judulnya == '3':
            stok3 = stok3 - berapa

    ## KITA GUNAKAN VARIABEL BARU UNTUK MENAMPUNG HASIL AKHIRNYA
    relek = 'stok' + judulnya

    ## SETELAH ITU KITA COBA JELASKAN KEPADA PYTHON ARTINYA!
    if relek == 'stok1':
        relek = stok1
    elif relek == 'stok2':
        relek = stok2
    elif relek == 'stok3':
        relek = stok3

    ## SETELAH SELESAI, KITA HASILKAN HASIL AKHIRNYA!
    print(f'Maka Stok buku {judulnya} menjadi {relek} ')

    lanjut = str(input('Lanjut gak? ').lower())
    if lanjut == 'y':
        print('oke')
    else:
        cobayuk = False
