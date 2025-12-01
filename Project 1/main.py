from auto_mode import run_auto_mode
from manual_mode import run_manual_mode

def main():
    while True:
        print("Choose mode:")
        print("1 = Automatic mode")
        print("2 = Manual mode")
        print("Q = Quit")

        choice = input("Enter choice: ").lower()

        if choice == "1":
            run_auto_mode()
        elif choice == "2":
            run_manual_mode()
        elif choice == "q":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
