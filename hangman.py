import random
name=input("Enter Your Name")
print("Welcome to Hangman game",name)
print("RULES:\n 1)DO NOT ENTER THE ENTERED LETTER AGAIN \n 2)YOU ONLY HAVE 6 LIFELINE AND FOR EACH WRONG GUESS YOU WILL LOSE 1 \n 3)YOU CAN USE IDEA  IT COST 25 POINTS FOR EACH\n 4)IDEA_SCORE:\n       IDEA_SCORE=100-->GOLD PLAYER\n       IDEA_SCORE=75-->SILVER PLAYER\n       IDEA_SCORE=50-->BRONZE PLAYER")

fruits=['apple','orange','dates','grapes']
IDEA_SCORE=100
lifeline=6
stages=['''
        +--------+
        |        |
        |        O
        |       /|\ 
        |       / \ 
        ============
        ''',
        '''
        +--------+
        |        |
        |        O
        |       /|\ 
        |       / 
        ============
        ''','''
        +--------+
        |        |
        |        O
        |       /|\ 
        |       
        ============
        ''','''
        +--------+
        |        |
        |        O
        |       /|
        | 
        ============
        ''','''
        +--------+
        |        |
        |        O
        |        |
        |
        ============
        ''','''
        +--------+
        |        |
        |        O
        |
        |
        ============
        ''','''
        +--------+
        |        |
        |
        |
        |
        ============
        ''']
rand_word=random.choice(fruits)
if(rand_word=="apple"):
    c=1
    clue1=list(set("apple"))
elif(rand_word=="orange"):
    c=2
    clue2=list(set("orange"))
elif(rand_word=="dates"):
    c=3
    clue3=list(set("dates"))
else:
    c=4
    clue4=list(set("grapes"))
#print(clue)
#print(rand_word)
blank=[]
for i in  range(len(rand_word)):
    blank+="_"
print (blank) 
end=True
idea=100
gl=[]
while(lifeline!=0 and end!= False):
    guess_ltr=input("Guess a letter").lower()
    if guess_ltr in gl:
        print("You Have Already guessed This Letter try anything else")
        guess_ltr=input("Guess a letter").lower()
    else:
        gl.append(guess_ltr)
        print("Guessed letter",gl)
    
    if guess_ltr in rand_word:
        for i in range(len(rand_word)):
            if(guess_ltr==rand_word[i]):
                blank[i]=guess_ltr
        print(blank)
        print("TOTAL LIFE LINE=",lifeline)
        print("IDEA_POINTS:",idea)
    else:
        lifeline-=1
        print("TOTAL LIFE LINE=",lifeline)
        print("IDEA_POINTS:",idea)
        if(lifeline!=0):
            ideachoice=input("you want to use IDEA YES/NO?").lower()
            if(ideachoice=="yes"):
                idea-=25
                if(c==1):
                    c_elem=list(set(gl)&set(clue1))
                    clue1=[elem for elem in clue1 if elem not in c_elem]
                    random.shuffle(clue1)
                    if clue1:
                        print("HINT:",clue1[0])
                        clue1.pop(0)
                    else:
                         print("Out of choice")
                        
                elif(c==2):
                        c_elem=list(set(gl)&set(clue2))
                        clue2=[elem for elem in clue2 if elem not in c_elem]
                        random.shuffle(clue2)
                        if clue2:
                            print("HINT:",clue2[0])
                            clue2.pop(0)
                        else:
                             print("Out of choice")
                elif(c==3):
                        c_elem=list(set(gl)&set(clue3))
                        clue3=[elem for elem in clue3 if elem not in c_elem]
                        random.shuffle(clue3)
                        if clue3:
                            print("HINT:",clue3[0])
                            clue3.pop(0)
                        else:
                             print("out of choice")
                else:
                        c_elem=list(set(gl)&set(clue4))
                        clue4=[elem for elem in clue4 if elem not in c_elem]
                        random.shuffle(clue4)
                        if clue4:
                            print("HINT :",clue4[0])
                            clue4.pop(0)
                        else:
                             print("Out of choice")
            else:
                pass            
    if(lifeline==0):
            print("Game over! you've lost.better luck next time!")
    if "_" not in blank:
        end=False
        print(" Congratulations! you've  won the game!")
        if(idea==100):
            print("you have won Gold medal!")
        elif(idea==75):
            print("you have won Silver medal!")
        elif(idea==50):
            print("you have won Bronze medal!")
        else:
            print("Great effort! keep trying,you'll get a medal next time")
    print(stages[lifeline])