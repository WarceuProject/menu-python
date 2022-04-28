# Oke ,disini saya membuat list menu dengan opsi menggunakan python 2.7
# mari kita mulai membuat kerangka nya :v

import os,sys
# Oke,ini di part 2 nya ya ,kita tambahin sedikit warna biar cuantik :v
class col:
  red ="\033[1;31m"
  grn ="\033[1;32m"
  end ="\033[0m"
  #Untuk warna agan bisa tambahin sesuka agan 
def banner():
  os.system('clear')
  #ini untuk banner atau logo nya
  print  "   "
  print col.red + "                Hallo gan"
  print col.grn + " Ini adalah program list opsi menu python2.7"
  print col.end + "_____________________________________________"
  print ""
  # Untuk banner agan2 bisa sesuaikan 
def menu():
  # Nah ini untuk menu nya
  print col.end + "[" + col.grn + "MENU" + col.end + "]:"
  print ""
  print col.end + "(1)." + col.grn + "Ospsi ke 1"
  print col.end + "(2)." + col.grn + "Opsi ke 2 "
  print col.end + "(0)." + col.grn + "Opsi keluar"
  
#setelah itu kita sebut keduanya di bawah
banner()
menu()
pil = input(col.end + "pilih:" + col.grn)
if pil == 1:
  print "Ini adalah opsi pertama"
elif pil == 2:
  print "Ini adalah opsi ke 2"
elif pil == 0:
  print "Ini opsi keluar"
  sys.exit()
else:
  print "kesalahan inputan"
  #di gunakan untuk ketika penginputan number nya salah atau tak sama
  # sekarang mari kita jalan kan
  
  
  
  #NAH GAMPANG KAN :v
  #Oke segini dulu aja ya :v nanti lanjut di part 2 nya
  
  
  
  #Nah sesudah itu agan bisa sesuai kan warna2 nya sesuka agan :v
  # oke dah kita tinggal buat project nya aja deh terserah agan mo bikin apa juga :v
