import random
def main():
    """Guess The Elemen"""
    print("*-*Guess The Elemen!*-*")
    print("“Winning takes talent; to repeat takes character.”")
    print("<><><><><><><><><><><><>")
    print("1.Oxygen")
    print("2.Hydrogen")
    print("3.Copper")
    print("4.Silver")
    print("5.Iridium")
    print("6.Coblat")
    q=["oxygen","hydrogen","copper","silver","iridum","coblat"]
    x=random.choice(q)
    guess = None
    
    while x!=guess:
        guess =str(input("Guess the Elemen number from 1-6 : " ))
        print("Don`t despair! Sooner or later good luck will find you!")
        print("_________________<>_________________")
        if x == guess:
            print("Congrats!")
        elif x != guess:
            print("Try a again.")
                    
main()
