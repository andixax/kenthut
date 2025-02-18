import random
import time
from colorama import init, Fore, Style, Back
import os

# Inisialisasi colorama
init(autoreset=True)

def bau_kentut(bau):
    # Daftar acak
    bau_kentut = [
        "Martabak Cokelat",
        "Oli Motor",
        "Ikan Lele",
        "Gosong",
        "Ikan Gosong",
        "Gak Bau/Wangi (makan apa bang)",
        "Bensin Pertamax",
        "Kotoran Kucing",
        "Kari Ayam",
        "Kari Ayam"
    ]
    
    # Memilih secara acak
    kenthut = random.choice(bau_kentut)
    return kenthut

def main_menu():
    os.system('clear')
    header = """
    
    __    ___  __  _      ____    ____  __ __      __  _    ___  ____   ______  __ __  ______ 
   /  ]  /  _]|  l/ ]    |    \  /    T|  T  T    |  l/ ]  /  _]|    \ |      T|  T  T|      T
  /  /  /  [_ |  ' /     |  o  )Y  o  ||  |  |    |  ' /  /  [_ |  _  Y|      ||  |  ||      |
 /  /  Y    _]|    \     |     T|     ||  |  |    |    \ Y    _]|  |  |l_j  l_j|  |  |l_j  l_j
/   \_ |   [_ |     Y    |  O  ||  _  ||  :  |    |     Y|   [_ |  |  |  |  |  |  :  |  |  |  
\     ||     T|  .  |    |     ||  |  |l     |    |  .  ||     T|  |  |  |  |  l     |  |  |  
 \____jl_____jl__j\_j    l_____jl__j__j \__,_j    l__j\_jl_____jl__j__j  l__j   \__,_j  l__j  
                                                                                              
                                                                                              
"""
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{header}")
    print(f"{Back.CYAN}{Fore.BLACK}Cek Bau Kentut | {Fore.BLUE}{Style.BRIGHT}{Back.RED}Created By {Back.BLUE}{Fore.RED}&DIXA")
    bau = input(f"{Fore.CYAN}{Style.BRIGHT}Masukkan nama kamu: ")
    kentut_user = bau_kentut(bau)
    print(f"{Fore.CYAN}{Style.BRIGHT}Kentut mu Bau {Fore.GREEN}{Style.BRIGHT}{kentut_user}")
    
    # Menambahkan jeda 2 detik
    time.sleep(2)
    
    while True:
        print(f"\n{Fore.CYAN}Pilihan:")
        print(f"{Fore.YELLOW}1. {Style.BRIGHT}Ulang")
        print(f"{Fore.YELLOW}2. {Style.BRIGHT}Keluar")
        
        pilihan = input(f"{Fore.CYAN}Masukkan pilihan kamu (1/2): ")
        
        if pilihan == "1":
            kentut_user = bau_kentut(bau)
            print(f"{Fore.CYAN}{Style.BRIGHT}Kentut mu Bau {Fore.GREEN}{Style.BRIGHT}{kentut_user}")
            time.sleep(2)
        elif pilihan == "2":
            print(f"{Fore.CYAN}Terima kasih Bang Udah Pake Script Ini!(⁠づ⁠￣⁠ ⁠³⁠￣)⁠づ")
            break
        else:
            print(f"{Fore.RED}Pilihan tidak valid. Silakan coba lagi.")

# Menampilkan menu utama
main_menu()