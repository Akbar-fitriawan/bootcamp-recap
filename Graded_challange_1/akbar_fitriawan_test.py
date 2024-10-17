'''
=================================================
Graded Challenge 1

Nama  : Akbar Fitriawan
Batch : HCK-14

Ini adalah program untuk menguji apakah fungsi dari ShoppingCart berjalan dengan baik
yang mana menguji tambah barang, hapus barang dan hitung total harga dari keranjang
=================================================
'''



import sys
import os

os.system("akbar_fitriawan_app.py") # membaca file .py
from akbar_fitriawan_app import ShoppingCart

import unittest # library unit test

class TestShoppingCart(unittest.TestCase):
    """ Kelas untuk test fungsi dari kelas ShoppingCart yang mana menguji tambah barang, hapus barang dan perhitungan total belanja """

    def test_add_item(self):
        '''' test fungsi tambah barang ke keranjang '''
        cart = ShoppingCart() # inisialisasi objek cart
        cart.add_item('Jeruk',1000) # method input barang sebagai percoabaan
        self.assertEqual(len(cart.items),1) # menghitung input yang masuk dan panggia method assertEqual untuk cek 
        self.assertEqual(cart.items[0].nama, 'Jeruk') # cek input nama apakah yang masuk sama dengan index
        self.assertEqual(cart.items[0].harga, 1000) # cek input harga
        
    def test_remove(self):
        ''' test fungsi hapus barang yang di keranjang '''
        cart = ShoppingCart() # inisialisasi objek cart
        cart.add_item("Apel", 1000) 
        cart.add_item("MANGGA", 20000) # method input barang sebagai percoabaan
        cart.remove_item("MANGGA") # method hapus barang 
        self.assertEqual(len(cart.items),1)
        self.assertEqual(cart.items[0].nama, 'Apel')

    def test_total(self):
        cart = ShoppingCart() # inisialisasi objek cart
        cart.add_item('APEL', 2000)# method input barang sebagai percoabaan
        cart.add_item('APEL', 2000)
        self.assertEqual(cart.total(), 4000) # Method cek total
        self.assertEqual(len(cart.items), 2)


if __name__ == "__main__": # Idiom 
    unittest.main() # gate main