"""
Nama    : Amiril Rusdana
NIM     : 20083000077
Kelas   : 2C
"""

kota = ['Surabaya','Bandung']
jarak =[169,452]
ongkirperkm = [2500,4000]
jwbulangprog = "y"

jwb = "y"
while jwb=="y" or jwb=="Y":
    u='a'
    while u=='a' or u=='b' or u=='A' or u=='B':
        print("\n======================================================")
        print("|                    Biaya Ekspedisi                 |")
        print("======================================================")
        print("| A. Surabaya, Batas Jarak 169 Km, Ongkir 2500/Km    |")
        print("| B. Bandung, Batas Jarak 452 Km, Ongkir 4000/Km     |")
        print("======================================================")
        u = input(" Masukkan tujuan anda \t= ")
        if u=='a' or u=='b' or u=='A' or u=='B':
            if u=='a' or u=='A':      
                java = 0
            elif u=='b' or u=='B':               
                java = 1

            print("------------------------------------------------------")
            print(" Tujuan\t\t\t=", kota[java])
            print(" Batas Jarak\t\t=", jarak[java],"Km")
            print(" Ongkir Per KM\t\t= Rp.", ongkirperkm[java])
            javascript =1
            totongkir = 1
            while javascript>=1 and javascript<=jarak[java]:
                javascript = int(input(" Masukkan Jarak Tujuan\t= "))
                if int(javascript)>0 and int(javascript)<=jarak[java]:
                    if int(javascript)>0 and int(javascript)<=jarak[java]:
                        totongkir = int(javascript) * int(ongkirperkm[java])
                        print(" Total Ongkir \t\t= Rp.", totongkir)
                        break
                else:
                    print(" Batas jarak", jarak[java],"Km")

            jwb = str(input("\n Ulang program? y/t \t= "))
            if jwb=="t" or jwb=="T":
                break
            elif jwb!="y" and jwb!="Y":
                print("Masukan y atau t saja")
                break

        else:
            print(" Masukkan angka usia A dan B saja")
            break
        