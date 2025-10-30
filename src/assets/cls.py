import os

def clear_console(bool):
    # Windows の場合は "cls"
    # macOS / Linux の場合は "clear"
    if bool == True:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        pass