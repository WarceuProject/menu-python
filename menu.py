# Oke ,disini saya membuat list menu dengan opsi menggunakan python 2.7
# mari kita mulai membuat kerangka nya :v

import os,sys

def banner():
  os.system('clear')
  #ini untuk banner atau logo nya
  print "   "
  print "                Hallo gan"
  print " Ini adalah program list opsi menu python2.7"
  print "_____________________________________________"
  print ""
  # Untuk banner agan2 bisa sesuaikan 
def menu():
  # Nah ini untuk menu nya
  print "[MENU]:"
  print ""
  print "(1). Ospsi ke 1"
  print "(2). Opsi ke 2 "
  print "(0) Opsi keluar"
  
#setelah itu kita sebut keduanya di bawah
banner()
menu()
pil = input("pilih:")
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
  