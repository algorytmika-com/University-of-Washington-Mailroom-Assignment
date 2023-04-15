from utils import facades as f

def main():
    while True:
        response = input(f.prompt)  
        if response == "1":
            f.send_thanks()
        elif response == "2":
            f.create_report()
        elif response == "3":
            f.exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()