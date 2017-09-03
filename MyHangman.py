def hangman(word):
    slots=["__"]*len(word)
    parts=["________", "|      |", "|      0", "|     /|\ ", "|     / \ " ]
    wrong=0
    won=False
    letters=list(word)
    print("\tSLOTS:")
    print(" ".join(slots))
    while wrong<len(parts):
        print("---*---"*6)
        guess=input("guess a letter:")
        print("\n\n\n\n")
        if guess in letters:
            index=word.index(guess)
            slots[index]=guess
            letters[index]="#"
        else:
            wrong+=1
        print(" ".join(slots))
        print("\n".join(parts[0:wrong]))
        print("\n\n\n\n")
        if "__" not in slots:
            print("You won!")
            print("The word was {}".format(" ".join(slot)))
            won=true
            break
    if not won:
        print("You lose!")
        print("The word was {}".format(word))
        

hangman("mango")


            
    


