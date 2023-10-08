import os
import glob
import shutil
from pystyle import *
import colorama
from colorama import *
from PIL import Image
import webbrowser
import sys

def open_discord_server_invite():
    # Remplacez 'YOUR_SERVER_INVITE_LINK' par votre lien d'invitation au serveur
    invite_link = 'https://discord.gg/2eqYYCFf'
    webbrowser.open_new_tab(invite_link)

if __name__ == "__main__":
    open_discord_server_invite()

def print_banner():
    banner = f"""

 █████╗ ██╗     ███████╗ █████╗ ███╗  ██╗██╗  ██╗  ██╗   ██╗  ███╗  
██╔══██╗██║     ██╔════╝██╔══██╗████╗ ██║╚██╗██╔╝  ██║   ██║ ████║  
██║  ╚═╝██║     █████╗  ███████║██╔██╗██║ ╚███╔╝   ╚██╗ ██╔╝██╔██║  ʙʏ ᴄᴇʟᴇsᴛɪᴀʟ
██║  ██╗██║     ██╔══╝  ██╔══██║██║╚████║ ██╔██╗    ╚████╔╝ ╚═╝██║  
╚█████╔╝███████╗███████╗██║  ██║██║ ╚███║██╔╝╚██╗    ╚██╔╝  ███████╗
 ╚════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝     ╚═╝   ╚══════╝        
    """
    print(Colorate.Vertical(Colors.red_to_black, str(banner), 1))
    Write.Print(("""
                \n\n  ==============================================================
                https://github.com/Hichioo"""), Colors.red_to_yellow, interval=0.0025)

def clear_dns_cache():
    try:
        if os.name == 'nt':
            os.system('ipconfig /flushdns')
            print("DNS cache cleared successfully.")
        else:
            print("DNS cache flushing is not supported on this system.")
    except Exception as e:
        print(f"Unable to clear DNS cache: {str(e)}")

def clear_user_temp():
    user_temp_directory = os.path.join(os.environ["USERPROFILE"], 'AppData', 'Local', 'Temp', '*')
    files = glob.glob(user_temp_directory)
    for file in files:
        try:
            if os.path.isfile(file):
                os.remove(file)
        except Exception as e:
            print(f"Unable to delete {file}: {str(e)}")

def clear_temp():
    temp_directory = os.path.join(os.environ["TEMP"], '*')
    files = glob.glob(temp_directory)
    for file in files:
        try:
            if os.path.isfile(file):
                os.remove(file)
        except Exception as e:
            print(f"Unable to delete {file}: {str(e)}")

def clear_recycle_bin():
    try:
        if os.name == 'nt':
            os.system('rd /s /q C:\\$Recycle.Bin')
        else:
            os.system('rm -rf ~/.local/share/Trash/*')
    except Exception as e:
        print(f"Unable to clear recycle bin: {str(e)}")

def clear_prefetch():
    prefetch_directory = 'C:\\Windows\\Prefetch'
    files = os.listdir(prefetch_directory)
    for file in files:
        try:
            file_path = os.path.join(prefetch_directory, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Unable to delete {file}: {str(e)}")

if __name__ == "__main__":
    while True:
        print_banner()

        print(Fore.YELLOW + """
                 ――――――――――――――――――――――――
                 | 1. Clear Temp        |
                 | 2. Clear Recycle Bin |
                 | 3. Clear Prefetch    |
                 | 4. Clear DNS Cache   |
                 | 5. Clear User Temp   |
                 | 6. Exit              |
                 ――――――――――――――――――――――――
          """)                

        option = input("                       >  ")

        if option == '1':
            clear_temp()
            print("Temp folder cleared successfully.")
        elif option == '2':
            clear_recycle_bin()
            print("Trash emptied successfully.")
        elif option == '3':
            clear_prefetch()
            print("Prefetch folder cleared successfully.")
        elif option == '4':
            clear_dns_cache()
        elif option == '5':
            clear_user_temp()
        elif option == '6':
            break
        else:
            print("Invalid option. Please select a valid option.")
