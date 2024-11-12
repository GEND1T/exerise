nama = str(input('Masukan Nama :  '))
umur = int(input('Masukan Umur : '))
pekerjaan_orangtua = str(input('Pekerjaan Orangtua : '))
gaji_orangtua = int(input('Gaji Orangtua : '))
ipk = float(input('IPK : '))


cek = ["dokter",'pns','tni']



if (gaji_orangtua <= 1000000) and (ipk > 2.7) and (umur < 25) and (pekerjaan_orangtua not in cek):
    hasil = 'memenuhi syarat untuk mendapatkan beasiswa'
else:
    hasil = 'tidak memenuhi syarat untuk mendapatkan beasiswa'

print()
print()
print()
print(f'NAMA :', nama)
print(f'UMUR :', umur)
print(f'PEKERJAAN ORANG TUA', pekerjaan_orangtua)
print(f'GAJI RANG TUA :', gaji_orangtua)
print(f'IPK :', ipk)    
print(f'HASIL :',hasil)
print()
print()
print(pekerjaan_orangtua not in cek)