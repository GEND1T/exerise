#input nama karyawan
nama = str(input("nama karyawan : "))


#input jam kerja per hari
jam = int(input("jumlah jam kerja : "))


#input tarif perjam
tarif = float(input("tarif per jam : "))



#hitung jam kerja perbulan
jam_kerja_perbulan = jam*20

#hitung gaji perbulan 
gaji = tarif*jam_kerja_perbulan 


#end
print()
print (f'\nnama karyawan : {nama}')
print (f'jam kerja : {jam}')
print (f'tarif perjam : {tarif}')
print(f'jumlah jam kerja perbulan : {jam_kerja_perbulan}')
print(f'gaji sebulan : {gaji:,.2f}')