import os
listprogram = []

def fungsi(waktu_selesai,jatah,programlist):
    start = 0
    while start < waktu_selesai:
        for i,data in enumerate(programlist):
            proses = data[0]
            waktu_proses = data[1]
            waktu_sisa = waktu_proses - jatah
            
            if(waktu_proses >= jatah):
                print(proses,'-> Detik Ke -',start, ' s.d. - Detik Ke -', start + jatah )
            else:
                print(proses,'-> Detik Ke -',start, ' s.d. - Detik Ke -', start + waktu_proses )
            
            if(waktu_proses >= jatah):
                start += jatah
            else:
                start += waktu_proses
                
            if( waktu_sisa > 0):
                listprogram.append([proses,waktu_sisa])

os.system("cls")
total_proses = int(input('Total Proses : '))

for i in range(total_proses):
    proses = input('Nama Proses : ')
    print("")
    waktu = int(input('Waktu Proses : '))
    print("")
    data_list = [proses,waktu]
    listprogram.append(data_list)

jatah = int(input('Jatah Waktu : '))

time_complete = 0
for i in listprogram:
    time_complete += i[1]

print("")
fungsi(time_complete,jatah,listprogram)