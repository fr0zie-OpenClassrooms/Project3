from app.application import Application

def main():
    choice = {"1": "cli", "2": "pygame"}
    output = input("How do you want to play the game?\n1: Terminal\n2: PyGame\nChoice: ")

    if output not in choice:
        main()
    else:
        app = Application(choice[output])
        app.run()

if __name__ == "__main__":
    main()