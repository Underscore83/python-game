try:
    
    Characters={}

    def show():
        print(Characters)
    
    def ask():
        print("This is the character dictionary")
        print("Choose one of the options below")
        print("1. Add characters")
        print("2. See your characters")
        print("3. Exit the dictionary")


    running=True

    while running:
    
        ask()
    
        ask1=int(input("Please choose an option "))
    
        if ask1==1:
        
            ask2=str(input("What is the name "))
            ask3=str(input("How many points are there "))
        
            Characters[ask2]=ask3
    
        elif ask1==2:
            show()
    
        elif ask1==3:
            running=False
    
        else :
            print("Invalid choice!")

except ValueError:
    print("Oops! Invalid choice!")
