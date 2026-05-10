import time
import os

def type_out(text, speed):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)

def clear():
    os.system("cls")

clear()
type_out("Welcome to MyFileManager\n", .05)

while True:
    type_out("\nContinue?\n", .03)
    input_main = input("Yes/No: ").lower()
    
    if input_main == "yes":
        clear()
        type_out("loading..", .2)
        clear()
        
        for char in "...":
            print(char, flush=True)
            time.sleep(.4)
        clear()

        def menu():
            print("======================================================================")
            time.sleep(.1)
            print(" >>                        MY FILE MANAGER                         << ")
            time.sleep(.1)
            print("======================================================================")
            time.sleep(.1)
            print(" [1] Read Inspiring Messages")
            time.sleep(.1)
            print(" [2] Add New Inspiring Messages")
            time.sleep(.1)
            print(" [3] Rewrite Entire File")
            time.sleep(.1)
            print(" [4] Exit")
            time.sleep(.1)
            print("======================================================================")
            time.sleep(.3)

        while True:
            menu()
            input_selection = int(input("Select: "))
            
            if input_selection == 1:
                while True:
                    clear()
                    type_out("Your File\n", .02)
                    with open("dreams.txt", "r") as file:
                        type_out(file.read(), .02)
                    
                    input_back_read = input("\n\nBack to menu(y/n)? ").lower()
                    if input_back_read == "y":
                        clear()
                        break
                    clear()

            elif input_selection == 2:
                while True:
                    clear()
                    type_out("Add new inspiring messages\n\n", .02)
                    input_message = input("Put message: ")
                    with open("dreams.txt", "a") as file1:
                        file1.write(f"\n{input_message}")
                    
                    type_out("\nadding..", 0.2)
                    clear()
                    for char in "...":
                        print(char, flush=True)
                        time.sleep(0.5)
                    clear()
                    type_out("Message Added", 0.1)
                    
                    input_back_add = input("\n\nBack to menu(y/n)? ").lower()
                    if input_back_add == "y":
                        clear()
                        break
                    clear()

            elif input_selection == 3:
                while True:
                    clear()
                    type_out("Rewriting the File\n\n", .02)
                    input_rewrite_content = input("Put message: ")
                    time.sleep(.2)
                    clear()
                    type_out("Are you sure?\nThis will overwrite your text file(y/n):\n", .02)
                    input_confirm = input("Typing... ").lower()
                    
                    if input_confirm == "y":
                        with open("dreams.txt", "w") as file2:
                            file2.write(f"\n{input_rewrite_content}")
                        type_out("\nCreating..", 0.2)
                        clear()
                        for char in "...":
                            print(char, flush=True)
                            time.sleep(0.5)
                        clear()
                        type_out("New file created", 0.1)
                        
                        if input("\n\nBack to menu(y/n)? ").lower() == "y":
                            clear()
                            break
                    elif input_confirm == "n":
                        break

            elif input_selection == 4:
                clear()
                if input("Exit(y/n): ").lower() == "y":
                    clear()
                    print("Thank you for using my system")
                    exit()
                clear()

    elif input_main == "no":
        clear()
        print("Thank you for using my system")
        break
    else:
        clear()
        type_out("Invalid Input\n", .02)
        time.sleep(.5)
