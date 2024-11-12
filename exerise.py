jumlah_siswa = int(input("masukan jumlah siswa : "))

total_nilai = 0
for x in  range(1,jumlah_siswa+1):
    nilai = int(input(f'masukan nilai siswa {x} : '))
    nilai = int(input(f'masukan nilai siswa {x} : '))
    total_nilai+=nilai
    
print()
print(f'jumlah nilai siswa : {total_nilai}')
print()
print(f'rata - rata nilai siswa : {total_nilai/jumlah_siswa}')

    

    
    
