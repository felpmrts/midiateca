import os
import time

def welcome():
    clear_screen()
    print(f"\n==================================")
    print("            MidiaTeca            ")
    print("==================================")

    time.sleep(3)

def bye():
    clear_screen()
    print(f"==================================")
    print(f"    Encerrando o programa...     ")
    print(f"==================================")
    time.sleep(3)
    clear_screen()


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')