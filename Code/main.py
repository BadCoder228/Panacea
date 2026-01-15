from os import system
from art import tprint
from Core.FreePanacea.main import Main as FreeMain
from Core.PremiumPanacea.main import Main as PremiumMain

def Main() -> None:
    system("cls")
    
    tprint("Booting mode")
    action : str = input("Please, select your account's type:\n1. Premium\n2. Free\n\n>>> ")
    
    system("cls")

    match(action):
        case "1":
            PremiumMain()
        case "2":
            FreeMain()
        case _:
            Main()

if __name__ == '__main__':
    Main()