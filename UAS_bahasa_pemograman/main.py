import texttable as tt
import getpass
from perhitungan.penil import nilai_mahasiswa
from perhitungan.pembay import pembayaran
from perhitungan.calcul import pilihan

def menu():
    print("==========================================")
    print("\n\t----pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")
    print("\t3. calculator")
    
    pilih=input("\n\tsilakan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2":
        pembayaran()
    elif pilih == "3":
        pilihan()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y\n)?")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input................!!!")
username=input("\nUsername : ")
password=getpass.getpass()
print("======================================================")
if username == "Rifki tbj" and password == "bissmillah":
    menu()

else:
    print("maaf password salah...!!!")

    
          
