'''
=================================================
Graded Challenge 1

Nama  : Akbar Fitriawan
Batch : HCK-14

Ini adalah program sederhana Shopping cart yang mana user dapat melakukan 
menambahkan barang ke keranjang, menghapus barang yang ada di keranjang, menampilkan 
jumalah barang yang ada di keranjang dan menjumlahkan total harga yang ada di keranjang.


=================================================
'''
import os # library os python



class CartItem:
  """
  Kelas Ini untuk menampung variable nama dan harga,
  serta sebagai induk kelas
  """
  def __init__(self, nama,harga):
    ''' Method inisialisasi attribut variable nama dan harga'''
    self.nama = nama
    self.harga = harga

  def __str__(self):
    ''' Method string induk kelas '''
    return f'Nama : {self.nama}, Harga : {self.harga}'

class ShoppingCart(CartItem):
  ''' Kelas ini untuk menampung items cart berisi method yang mana dapat menambah, menghapus , menammpilkan dan menjumlah'''
  def __init__(self):
    ''' Inisialisasi attribut dari induk kelas '''
    super().__init__(nama=None,harga=None)
    self.items = [] # mambuat list untuk manampug nama barang dan harga


  def add_item(self,nama,harga):
    """ Fungsi untuk menambah barang """ 
    item = CartItem(nama,harga) # menampung parameter kedalam item dan memasukan ke kelas induk sebagai objek
    self.items.append(item)

  def remove_item(self, nama_barang):
    """ Fungsi untuk menghapus barang di keranjang"""
    for item in self.items:
      if item.nama == nama_barang: # jika item nama sama dengan nama barang dari parameter 
        self.items.remove(item) # maka Items list di remove dari index awal yang nama nya sama
        break

  def total(self):
    """ Fungsi untuk menjumlahkan Items"""
    total = 0 # memasukan 0 untuk penjumlahan list item
    for item in self.items: # iterasi untuk mencari item
      total += item.harga
    return total # mengembalikan nilai penajumlahan harga

  def display(self):
    """ Fungsi untuk menampilkan barang di keranjang """
    print("Total barang di keranjang:")

    for item in self.items:
      print(item.nama, "-","Rp",item.harga)


def val_add():
  """ Fungsi untuk validasi nama barang adalah string dan harga adalah integer,
  Dengan ketentuan jika nama barang memiliki karakter atau nomor maka raise ValueError, serta jika harga bukan integer
  akan raise eror
  """
  try:
    nama_barang = input("Masukan nama barang: ")
    harga = int(input("Masukan harga : "))
    if nama_barang.isalpha() == False:
     raise ValueError('Silahakan Masukan lagi'+'\n')
  except ValueError:
    print('Tolong masukan dengan benar'+'\n')

  else:
    cart.add_item(nama_barang,harga)
    print(f'Barang "{nama_barang}" berhasil dimasukan ke keranjang')


def val_del():
  """ Fungsi validasi remove """
  print('input sesuai dengan nama !')
  for item in cart.items:
      print(f" - {item.nama} Rp {item.harga}")

  nama_hapus = input('Masukan barang yang igin di hapus: ')
  for item in cart.items:
    if nama_hapus == item.nama:
      cart.remove_item(nama_hapus)
      print('Berhasil di hapus\n')
      break
    else:
      print('Silahkan coba lagi\n')
      break






def main():
  ''' Fungsi ini user interface'''

  print("=================================================")

  print('\nSelamat Datang di Keranjang Belanja Toko UCUP\n')

  print("=================================================" + '\n')
  while True:
    
    print('\nMenu :')
    print('1. Menambah Barang')
    print('2. Hapus Barang')
    print('3. Tampilkan Barang di Keranjang')
    print('4. Lihat Total Belanja')
    print('5. Exit\n')
    
    try:
      '''Jika diluar pilihan yang tertera maka raise error'''
      pilih = int(input('Pilihan: '))
      
      if pilih > 5 or pilih < 1:
        print("Silahkan pilih dengan benar!!")

      else:
        
        if pilih == 1:
          val_add() # panggil fungsi validasi add
        elif pilih == 2:
          if cart.items == []: # jika keranjang kosong
            print('Maaf barang di keranjang tidak ada.')
          else:
            val_del() # panggil fungsi validasi del

        elif pilih == 3:
          if cart.items == []: # jika keranjang kosong
            print('Barang di keranjang tidak ada.')
          else:
            cart.display() # panggil fungsi kelas menampilkan detail item

        elif pilih == 4:
          print(f'Total belanja: Rp {cart.total():.2f}') # panggil fungsi penjumlahan item
        else:
           (pilih == 5)
           print('\n')
           print('Terimakasih Telah Belanja di toko UCUP')
           break

    except ValueError: # jika ketentuan tidak terpenuhi
      print('silahkan input dengan benar!!')



if __name__ == "__main__": # fungsi idiom
  cart = ShoppingCart() # inisialisasi objek 'cart'
  main() # panggil fungsi main interface user
  sistem_operasi = os.name # cek sistem os
  match sistem_operasi: 
      case "posix": os.system("clear") # fungsi clear terminal linux
      case "nt": os.system("cls") # fungsi clear terminal windows dan mac