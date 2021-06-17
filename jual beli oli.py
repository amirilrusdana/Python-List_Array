"""
Nama    : Amiril Rusdana
NIM     : 20083000077
Kelas   : 2C
"""
oli = ["Duration SW20 1L","Castrol Magnetec 1L","Federal Supreme XX 1L","Yamalube 1L","Shell 1L"]
harga = [53000,50000,54000,45000,46000]
jwb = "Y"
while jwb=="Y":
    u='A'
    while u>='A' and u<='E':
        print("\n======================================================")
        print("|                  Ganti Oli Sejahtera               |")
        print("======================================================")
        print("| A. Duration SW20 1L                   @ Rp. 53.000 |")
        print("| B. Castrol Magnatec 1L                @ Rp. 50.000 |")
        print("| C. Federal Supreme XX 1L              @ Rp. 54.000 |")
        print("| D. Yamalube 1L                        @ Rp. 45.000 |")
        print("| E. Shell 1L                           @ Rp. 46.000 |")
        print("======================================================")
        u = input(" Masukkan oli Pilihan anda \t= ")
        u = u.upper()
        if u>='A' and u<='E':
            if u=='A':      
                java = 0
            elif u=='B':
                java = 1
            elif u=='C':      
                java = 2
            elif u=='D':
                java = 3
            elif u=='E':
                java = 4
            
            print("------------------------------------------------------")
            print(" Anda memilih Oli \t\t=",oli[java])
            print(" Harga \t\t\t\t= Rp.", harga[java],"@ Buah")
            jum = int(input(" Jumlah pembelian \t\t= "))
            jumhar = jum * harga[java]
            print(" Harga Awal \t\t\t= Rp.",jumhar)
            if jumhar>=200000 :
                disk = jumhar * 0.05
                print(" Anda Mendapat Diskon \t\t= Rp.", disk)
            else:
                disk = 0

            javascript = jumhar - disk
            ppn = javascript * 0.01
            totharga = javascript + ppn
            print(" PPN \t\t\t\t= Rp.",ppn)
            print(" Total Harga \t\t\t= Rp.",totharga)
            while jwb!='Y' or jwb!='T':
                jwb = input("\n Ulang program? y/t \t\t= ")
                jwb = jwb.upper()
                if jwb=="T":
                    print("------------------ Program Berhenti ------------------")
                    exit()
                elif jwb=='Y':
                    break
                else :
                    print("---------------- Masukan Y atau T saja ----------------")
        else:
            pesan=" Masukkan angka usia A-E saja"
            print(pesan)
            break
        