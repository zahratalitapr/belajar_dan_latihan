#membuat list kosong untuk menampung nama buah
buah=[]
stop=false
i=0
#mengisi nama buah
while(not stop):
  nama_buah=raw_input("Masukan nama buah dari yang paling kamu suka ke-{}:".format(i))
  nama.append(nama_buah)
  
  #increment i
  i+=1
  lagi=raw+input("Ada buah kesukaanmu yang lain ? (y/n):")
  if(lagi=="y"):
    stop=True
#Cetak semua nama buah
print "=" *10
print"Kamu memiliki {} buah kesukaan".format(len(buah))
for bh in buah:
  print"-{}".format(bh)
