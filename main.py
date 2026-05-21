from app.cli import interface
from app.cli import utils

def main():
    
    utils.welcome()

    interface.menu()

    utils.bye()

if __name__ == "__main__":
    main()