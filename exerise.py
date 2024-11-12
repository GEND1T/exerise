nama = str(input('NAMA KARYAWAN : ')).upper()
jabatan = str(input ('JABATAN KARYAWAN : ')).upper()
status = str(input('STATUS PERKAWINAN : ')).upper()
print()
print()
print()
print()


# if jabatan == "DESIGN":
#     gaji =5000000
#     if status == "SUDAH MENIKAH":
#         gaji_kotor = gaji + gaji*(20/100)
#         pajak = gaji_kotor*(10/100)
#         total_pendapatan = gaji_kotor - pajak
#         print(f'NAMA KARYAWAN:{nama}')
#         print(f'JABATAN KARYAWAN:{jabatan}')
#         print(f'STATUS PERNIKAHAN :{status}')
#         print()
#         print()
#         print()

        
        
        


#         print(f'GAJI KOTOR :{gaji_kotor}')
#         print(f'PAJAK :{pajak}')
#         print(f'TOTAL PENDAPATAN :{total_pendapatan}')
#     else:
#         print(f'NAMA KARYAWAN:{nama}')
#         print(f'JABATAN KARYAWAN:{jabatan}')
#         print(f'STATUS PERNIKAHAN :{status}')

#         pajak = gaji*(10/100)
#         total_pendapatan = gaji - pajak
#         print(f'PAJAK :{pajak}')
#         print(f'TOTAL PENDAPATAN :{total_pendapatan}')

# elif jabatan == "PROGRAMMER":
#     gaji =10000000
#     if status == "SUDAH MENIKAH":
#         gaji_kotor = gaji + gaji*(20/100)
#         pajak = gaji_kotor*(10/100)
#         total_pendapatan = gaji_kotor - pajak
#         print(f'NAMA KARYAWAN:{nama}')
#         print(f'JABATAN KARYAWAN:{jabatan}')
#         print(f'STATUS PERNIKAHAN :{status}')

#         print(f'GAJI KOTOR :{gaji_kotor}')
#         print((f'PAJAK :{pajak}'))
#         print(f'TOTAL PENDAPATAN :{total_pendapatan}')
#     else :
#         print(f'NAMA KARYAWAN:{nama}')
#         print(f'JABATAN KARYAWAN:{jabatan}')
#         print(f'STATUS PERNIKAHAN :{status}')
    
        
#         pajak = gaji*(10/100)
#         total_pendapatan = gaji - pajak
#         print((f'PAJAK :{pajak}'))
#         print(f'TOTAL PENDAPATAN :{total_pendapatan}')
        



# elif jabatan == "RESOURCE":
#     gaji = 5000000
#     if status == "SUDAH MENIKAH":
#          gaji_kotor = gaji + gaji*(20/100)
#          pajak = gaji_kotor*(10/100)
#          total_pendapatan = gaji_kotor - pajak
#          print(f'NAMA KARYAWAN:{nama}')
#          print(f'JABATAN KARYAWAN:{jabatan}')
#          print(f'STATUS PERNIKAHAN :{status}')

#          print(f'GAJI KOTOR :{gaji_kotor}')
#          print((f'PAJAK :{pajak}'))
#          print(f'TOTAL PENDAPATAN :{total_pendapatan}')
#     else:
#           pajak = gaji*(10/100)
#           total_pendapatan = gaji - pajak
#           print(f'NAMA KARYAWAN:{nama}')
#           print(f'JABATAN KARYAWAN:{jabatan}')
#           print(f'STATUS PERNIKAHAN :{status}')

#           print((f'PAJAK :{pajak}'))
#           print(f'TOTAL PENDAPATAN :{total_pendapatan}')
          
import locale

# Set locale ke Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

angka = 10000
rupiah = locale.currency(angka, grouping=True, symbol="Rp ")
# print(rupiah)  # Output: Rp 10.000,00

if (jabatan == "RESOURCE"or jabatan== "DESIGN"):
    gaji = 5000000
elif jabatan == "PROGRAMER" :
    gaji = 10000000
else:
    print("DITOLAK")
# print (jabatan=="RESOURCE"or jabatan=="DESIGN" or jabatan== "PROGRAMER")



if  status == "SUDAH MENIKAH":
    tunjangan = gaji*(20/100)
    gaji_kotor = gaji + gaji*(20/100)
    pajak = gaji_kotor*(10/100)
    total_pendapatan = gaji_kotor - pajak
    
elif (jabatan=="RESOURCE"or jabatan=="DESIGN" or jabatan== "PROGRAMER") : 
    gaji_kotor = gaji
    pajak = gaji_kotor*(10/100)
    total_pendapatan = gaji_kotor - pajak
    

print(f'NAMA KARYAWAN : {nama}')
print(f'JABATAN KARYAWAN : {jabatan}')
print(f'STATUS PERNIKAHAN : {status}')

# print(f'GAJI KOTOR : {locale.currency(gaji_kotor, grouping=True, symbol="Rp. ")}')
# print((f'PAJAK : {pajak:,.0F}'))
# print(f'TOTAL PENDAPATAN : {locale.currency(total_pendapatan, grouping=True, symbol="Rp. ")}')

if  status == "SUDAH MENIKAH":
    print(f'TUNJANGAN KELUARGA : {locale.currency(tunjangan, grouping=True, symbol="Rp. ")}')

if (jabatan=="RESOURCE"or jabatan=="DESIGN" or jabatan== "PROGRAMER"):
    print(f'GAJI KOTOR : {locale.currency(gaji_kotor, grouping=True, symbol="Rp. ")}')
    print((f'PAJAK : {locale.currency(pajak, grouping=True, symbol="Rp. ")}'))
    print(f'TOTAL PENDAPATAN : {locale.currency(total_pendapatan, grouping=True, symbol="Rp. ")}')












        
       
        


