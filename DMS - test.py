
#----------------------------#
# IMPORTS AND TIME VARIABLES #
#----------------------------#
import pickle
import time
import keyboard

quickdialog = .01
a = .05
b = .075
dialog = .08
d = 1.25
e = 1.88
f = 3
g = 4
test = .5
GAMEOVER = .70


x = 0
x_save= open("diamond.pickle", "wb")
pickle.dump(x, x_save)
x_save.close()




'''
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
'''


#==============================================================================================#
# print save chapter 1
#==============================================================================================#

def savechapter1():

    print()
    print()
    Line = "OPENING SAVED CHECKPOINT "
    for character in Line:
        print(end=character, flush = True)
        time.sleep(dialog)
    time.sleep(2.5)
    print()
    print()
    print()
    print('BOSS: "YOU\'RE FIRED"')
    print()
    print("Your boss has had it with your tardiness!")
    print("He didn’t know your car was in the shop- he didn’t seem to care either.")
    print("Good thing you took the bus all the way across town for THIS!")
    print("You walk down the street with nowhere to go.")
    print("Your newfound joblessness has made the city feel big and scary.")
    print("Maybe if you beg, your landlord will let you pay your rent, late... again.")
    print("As you silently beg for a guardian angel to help you-- it happens:")
    print("A Ferrari speeds down the street and after performing a donut, parks next to you.")
    print("The windows roll down to see a rich, drunk man.")
    print("He throws you an expensive looking box.")
    print()
    print('RICH MAN: "Happy Birthday, Kid!')
    print('          "Ciao!"')
    print()
    print("He drives off just as quickly as he came.")
    print("You didn’t expect your guardian angel to smell like booze.")
    print("Regardless, you wonder what the hell is in this box!")
    print("You know it’s dangerous to open a present from a total stranger...")
    print("But, what the hell? You’ve got nothing to lose!")
    print("You look inside the box, and see a pink diamond the size of your fist!")
    print("You panic, you have no idea where this came from or how that stranger got it.")
    print("But you also wonder how much it’s worth...")
    print()
    print("What should you do?")
    print()
    print()
    optionch1()
    


#==============================================================================================#
# print save chapter A
#==============================================================================================#


def savechapterA():
    chapterVALUE = 2
    print()
    print()
    Line = "OPENING SAVED CHECKPOINT "
    for character in Line:
        print(end=character, flush = True)
        time.sleep(dialog)
    time.sleep(2.5)
    print()
    print()
    print()
    print("You get off the bus.")
    print("The appraiser’s office is only a few blocks away.")
    print("You think nothing can go wrong, until it happens... again!")
    print("A large van screeches its breaks and parks next to you.")
    print("The sliding door opens...")
    print("Inside are three well-dressed men who look like they bench Maseratis!")
    print("You also see the man from that night.")
    print("He looks like he’s been beaten by them.")
    print()
    print('MOBSTER: "Is this them?"')
    print()
    print('RICH MAN [IN PAIN]: "Y-yes..."')
    print()
    print("The mobster is looking at you, menacingly!")
    print()
    print('MOBSTER: "Don’t make this harder than it needs to be!"')
    print('         "Give us the diamond!"')
    print()
    print('DRIVER: "Yeah!"')
    print('        "We stole that fair and square!"')
    print()
    print("The mobster turns back quickly at the driver.")
    print()
    print('MOBSTER: "Shut the fuck up! This fucker can’t know that!"')
    print()
    print("One of the men hops out and greets you with a threatening stance.")
    print("Wow... You thought goons this stupid only existed in cartoons...")
    print("The rich man must’ve stolen a stolen diamond and given it to you.")
    print("Does that mean you stole it too?!")
    print("Who’d it belong to originally?!")
    print()
    optionchA()
    




#==============================================================================================#
# print save chapter B1
#==============================================================================================#

def savechapterB1():
    print()
    print()
    Line = "OPENING SAVED CHECKPOINT "
    for character in Line:
        print(end=character, flush = True)
        time.sleep(dialog)
    time.sleep(2.5)
    print()
    print()
    print()
    print("Without any other options you hide in a poorly built dog house nearby.")
    print("The growling Schnauzer sitting next to you would be a lot scarier on any other day.")
    print("As they land, the Schnauzer switches attention to them and runs out barking.")
    print("The Mobsters scream like children and run away from the dog.")
    print("You’re starting to question why you were even scared of them in the first place.")
    print("You know it’s not yours, and it almost got you buried in the Mojave Desert.")
    print("...And yet, you went through a hell of a lot of trouble to protect it...")
    print()
    print("Time for a serious decision! What do you do?")
    print()
    optionchB1()




#==============================================================================================#
#==============================================================================================#



#==============================================================================================#
#==============================================================================================#


#==============================================================================================#
                                  # INTRO SCRIPT #
#==============================================================================================#


def print_intro():
    

    print()
    print()
    print()
    print()
    print("##################################################################")
    print("##################################################################")
    print("###                                                            ###")
    print("###               _______________________________              ###")
    print("###           /@@@#............@@@@@............@@@.\          ###")
    print("###          /@@(/@@........#@@.   @@@........@@@..@.\         ###")
    print("###         /@@(/)%@@....@@@..       @@@....@@.  ..@@:\        ###")
    print("###        /@@(//////@@/@@*....         @@@@@@.    ..@:\       ###")
    print("###       |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:.|      ###")
    print("###        \@@@(///////#@@..............@@%:       .@@:/       ###")
    print("###         \@@@(//////&@@..............@@%:      .@@./        ###")
    print("###            \#@@(////@@@.............@@%:     @@/           ###")
    print("###             \@@(/////@@(...........@@%:    .@@/            ###")
    print("###                \@@(///@@,.........@@%: .&@@/               ###")
    print("###                  \@@(//@@........@@%:..@@@/                ###")
    print("###                     \@@(/@@.....@@#  @@/                   ###")
    print("###                      \@@@@@..@@@@@%../                     ###")
    print("###                         \,%@@@@%.../                       ###")
    print("###                           \%@@%../                         ###")
    print("###                                                            ###")
    print("##################################################################")
    print("##################################################################")
    print()
    print()
    time.sleep(2)
    print("                DIAMOND, MOBSTERS, AND SCHNAUZERS                 ")
    print()
    time.sleep(2)
    print("                 Programmed by:   Jimmy Slaughter                 ") 
    time.sleep(2)
    print("                  Written by:      Robert Colyar                  ") 
    time.sleep(2)
    print()
    print()
    print()
    print("Welcome to DIAMOND, MOBSTERS, AND SCHNAUZERS.")
    print()
    time.sleep(2)

#==============================================================================================#
                                  # CHAPTER 1 SCRIPT #
#==============================================================================================#


def printch1():

    
    print()
    print()
    input("PRESS ENTER TO START ")
    print()
    print()
    print()
    line1 = 'BOSS: '
    print(line1, end = "")
    time.sleep(1)
    line2 = '"YOU\'RE FIRED!"'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
    print("                                                                >>>", end = "")
    input()
    


    print()
    print("Your boss has had it with your tardiness!                                            >>>", end = "")
    input()
    print("He didn’t know your car was in the shop- he didn’t seem to care either.              >>>", end = "")
    input()
    print("Good thing you took the bus all the way across town for THIS!                        >>>", end = "")
    input()
    print("You walk down the street with nowhere to go.                                         >>>", end = "")
    input()
    print("Your newfound joblessness has made the city feel big and scary.                      >>>", end = "")
    input()
    print("Maybe if you beg, your landlord will let you pay your rent, ", end = "")
    print("late", end = "")
    line3 = '...'
    for character in line3:
        print(end=character, flush=True)
        time.sleep(.75)
    print(" again.", end = "")
    input("           >>>")
    print("As you silently beg for a guardian angel to help you-- it happens:                   >>>", end = "")
    input()
    print("A Ferrari speeds down the street and after performing a donut, parks next to you.    >>>", end = "")
    input()
    print("The windows roll down to see a rich, drunk man.                                      >>>", end = "")
    input()
    print("He throws you an expensive looking box.                                              >>>", end = "")
    input()
    print()
    line4 = 'RICH MAN: '
    print(line4, end = "")
    time.sleep(1)
    line5 = '"Happy Birthday, Kid!"'
    for character in line5:
        print(end=character, flush=True)
        time.sleep(.025)
    input("                                                     >>>")
    line5 = '          "Ciao!"'
    for character in line5:
        print(end=character, flush=True)
        time.sleep(.025)
    input("                                                                    >>>")
    print()
    print("He drives off just as quickly as he came.                                            >>>", end = "")
    input()
    print("You didn’t expect your guardian angel to smell like booze.                           >>>", end = "")
    input()
    print("Regardless, you wonder what the hell is in this box!                                 >>>", end = "")
    input()
    print("You know it’s dangerous to open a present from a total stranger...                   >>>", end = "")
    input()
    print("But, what the hell? You’ve got nothing to lose!                                      >>>", end = "")
    input()
    print("You look inside the box, and see a pink diamond the size of your fist!               >>>", end = "")
    input()
    print("You panic, you have no idea where this came from or how that stranger got it...      >>>", end = "")
    input()
    print("But you also wonder how much it’s worth...                                           >>>", end = "")
    input()
    print()
    print("What should you do?                                                                  >>>", end = "")
    input()
    print()
    optionch1()
    


#==============================================================================================#
                                  # CHAPTER A SCRIPT #
#==============================================================================================#


def printchA():
    chapterVALUE = 2
    print()
    print()
    input("PRESS ENTER TO START ")
    print()
    print()
    print()
    print("Tie, or no tie?                                                                      >>>", end = "")
    input()
    print("You’re a little out of your element here.                                            >>>", end = "")
    input()
    print("It’s been a few days since that night.                                               >>>", end = "")
    input()
    print("But you finally decided to appraise the diamond.                                     >>>", end ="")
    input()
    print("You’ve never done this before and don’t know how nicely you should dress.            >>>", end ="")
    input()
    print("Hopefully this process will be more routine when you’re rich!                        >>>", end = "")
    input()
    print("For now, you’ve got a bus to catch!                                                  >>>", end = "")
    input()
    print("You check yourself in the mirror before you go.                                      >>>", end = "")
    input()
    print()
    print()
    print("Which tie did you put on?")
    print()
    print("[A] Blue toned stripes\n[B] Solid red\n[C] Definitely a black bowtie")
    tieanswer = input("Select an option:   ")
    
    if tieanswer == "A" or tieanswer == "a":
        print()
        tiequestion = "Good choice!\nMaybe the blue pattern will hide your nervous sweat!"
        for character in tiequestion:
            print(end=character, flush=True)
            time.sleep(quickdialog)
        input("                                  >>>")
        print()
    elif tieanswer == "B" or tieanswer == "b":
        print()
        tiequestion = "Good choice!\nThe red tie matches your nervously flushed face!"
        for character in tiequestion:
            print(end=character, flush=True)
            time.sleep(quickdialog)
        input("                                     >>>")
        print()
    elif tieanswer == "C" or tieanswer == "c":
        print()
        tiequestion = "Good choice!\nNo one will question your eccentrically off-putting style!"
        for character in tiequestion:
            print(end=character, flush=True)
            time.sleep(quickdialog)
        input("                           >>>")
        print()
    else:
        print()
        tiequestion = "Who are you kidding?\nWith your inability to make a proper desicion, you left without a tie."
        for character in tiequestion:
            print(end=character, flush=True)
            time.sleep(quickdialog)
        input("               >>>")
        print()
    

    print("You get off the bus.                                                                 >>>", end = "")
    input()
    print("The appraiser’s office is only a few blocks away.                                    >>>", end = "")
    input()
    print("You think nothing can go wrong, until it happens... again!                           >>>", end = "")
    input()
    print("A large van screeches its breaks and parks next to you.                              >>>", end = "")
    input()
    print("The sliding door opens...                                                            >>>", end = "")
    input()
    print("Inside are three well-dressed men who look like they bench Maseratis!                >>>", end = "")
    input()
    print("You also see the man from that night.                                                >>>", end = "")
    input()
    print("He looks like he’s been beaten by them.                                              >>>", end = "")
    input()
    print()

    chb0 = 'MOBSTER: '
    print(chb0, end = "")
    time.sleep(1)
    chb1 = '"Is this them?"'
    for character in chb1:
        print(end=character, flush=True)
        time.sleep(dialog)
    input("                                                             >>>")
    print()
    chb2 = 'RICH MAN [IN PAIN]: '
    print(chb2, end = "")
    time.sleep(1)
    chb4 = 'Y-yes..."'
    for character in chb4:
        print(end=character, flush=True)
        time.sleep(dialog)
    input("                                                        >>>")
    print()
    print("The mobster is looking at you, menacingly!                                           >>>", end ="")
    input()
    print()
    chb5 = 'MOBSTER: '
    print(chb5, end = "")
    time.sleep(1)
    chb6 = '"Don’t make this harder than it needs to be!"'
    for character in chb6:
        print(end=character, flush=True)
        time.sleep(.05)
    input("                               >>>")
    chb6 = '         "Give us the diamond!"'
    for character in chb6:
        print(end=character, flush=True)
        time.sleep(.03)
    input("                                                      >>>")
    print()
    chb5 = 'DRIVER: '
    print(chb5, end = "")
    time.sleep(1)
    chb7 = '"Yeah! '
    print(chb7, end ="")
    time.sleep(1)
    chb8 = '"We stole that fair and square!"'
    for character in chb8:
        print(end=character, flush=True)
        time.sleep(dialog)
    input("                                      >>>")
    print()
    print("The mobster turns back quickly at the driver.                                        >>>", end ="")
    input()
    print()
    chb5 = 'MOBSTER: '
    print(chb5, end = "")
    time.sleep(1)
    chb6 = '"Shut the fuck up! This fucker can’t know that!"'
    for character in chb6:
        print(end=character, flush=True)
        time.sleep(quickdialog)
    input("                            >>>")
    print()
    print("One of the men hops out and greets you with a threatening stance.                    >>>", end = "")
    input()
    chb6 = 'Wow... '
    for character in chb6:
        print(end=character, flush=True)
        time.sleep(.33)
    time.sleep(1.5)
    print("You thought goons this stupid only existed in cartoons...                     >>>", end ="")
    input()
    
    print("The rich man must’ve stolen a stolen diamond and given it to you.                    >>>", end ="")
    input()
    print("Does that mean you stole it too?!                                                    >>>", end ="")
    input()
    print("Who’d it belong to originally?!                                                      >>>", end ="")
    input()
    print()
    optionchA()
    


#==============================================================================================#
                                  # CHAPTER B SCRIPT #
#==============================================================================================#

def printchB():
    print()
    print()
    input("PRESS ENTER TO START ")
    print()
    print()
    print()
    line1 = 'MECHANIC: '
    print(line1, end = "")
    time.sleep(1)
    line2 = '"YOU\'RE HIRED!"'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
        
    input("                                                            >>>")
    print()
    print("Ironic you got hired by the mechanic that fixed your car.                            >>>", end = "")
    input()
    print("Sure it wasn’t your first choice in jobs, but what does it matter?                   >>>", end = "")
    input()
    print("This is your life now. Dead-end-job to dead-end-job...                               >>>", end = "")
    input()
    print("As you change Karen’s oil for the fiftieth time you think about that night.          >>>", end = "")
    input()
    print("Leaving the diamond was the right thing to do... but at what cost?                   >>>", end = "")
    input()
    print("It’s almost like you made a “logical” decision out of fear of uncertainty.           >>>", end = "")
    input()
    print("Clearly someone doesn’t like adventures...                                           >>>", end = "")
    input()
    print("Too bad life isn’t a video-game that you can reset.                                  >>>", end = "")
    input()
    print("Now get back to work!                                                                >>>", end = "")
    
    input()
    print()
    print()
    line0 = 'GAME OVER'
    for character in line0:
        print(end=character, flush=True)
        time.sleep(GAMEOVER)
    print("\n")
    line1 = 'CONGRATULATIONS!'
    for character in line1:
        print(end=character, flush=True)
        time.sleep(dialog)
    print("\n")
    line2 = 'You got the QUICKEST ENDING!'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
    print()
    print()
    input("PRESS ENTER TO RETURN TO MAIN MENU ")
    time.sleep(1.5)
    gameStart()
    
    

#==============================================================================================#
                                  # CHAPTER A1 SCRIPT #
#==============================================================================================#

def printchA1():
    print()
    print()
    input("PRESS ENTER TO START ")
    print()
    print()
    print()
    print("Just keep screaming!                                                                 >>>", end = "")
    input()
    print("No one heard you the first 52 times, so maybe 53 times’ the charm!                   >>>", end = "")
    input()
    print("Apparently The Mob really doesn’t like loose ends.                                   >>>", end = "")
    input()
    print("When you gave back the Diamond, they decided you knew too much.                      >>>", end = "")
    input()
    print("No amount of desperate pleading is going to change a Mob Boss’s mind!                >>>", end = "")
    input()
    print("Now you're tied up in a shitty coffin that smells like your own B.O.                 >>>", end = "")
    input()
    print("They buried you in what you can only imagine is the Mojave Desert.                   >>>", end = "")
    input()
    print("To think of what could’ve happened if you had thought your decision through.         >>>", end = "")
    input()
    print("Don’t worry, though, someone will come for you! ", end = "")
    print("Maybe", end = "")
    line3 = '...'
    for character in line3:
        print(end=character, flush=True)
        time.sleep(.15)
    print("                             >>>", end = "")
    input()
    print()
    print()


    badendminus = 'GAME OVER'
    for character in badendminus:
        print(end=character, flush=True)
        time.sleep(GAMEOVER)
    print("\n")
    line1 = 'CONGRATULATIONS!'
    for character in line1:
        print(end=character, flush=True)
        time.sleep(dialog)
    print("\n")
    line2 = 'You got the WORST ENDING!'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
    print()
    print()
    input("PRESS ENTER TO RETURN TO MAIN MENU ")
    time.sleep(1.5)
    gameStart()

#==============================================================================================#
                                  # CHAPTER B1 SCRIPT #
#==============================================================================================#

def printchB1():
    print()
    print()
    input("PRESS ENTER TO START ")
    print()
    print()
    print()
    print("You book-it as fast as you can - which is hard with the diamond box in your arms!    >>>", end = "")
    input()
    print("You don’t look behind you, but you can hear the Mobsters chasing you on foot!        >>>", end = "")
    input()
    print("Up ahead is a tall, wooden fence leading to some dude’s backyard.                    >>>", end = "")
    input()
    print("You throw the Diamond over the fence then try to climb the fence yourself.           >>>", end = "")
    input()
    print("This looks so much easier in the movies!                                             >>>", end = "")
    input()
    print("Behind you, you hear the loud cursings of one of the Mobsters closing in on you!     >>>", end = "")
    input()
    print("You feel a strong hand grip your heel.                                               >>>", end = "")
    input()
    print()
    text0 = "MOBSTER: "
    print(text0, end = "")
    text = "GOTCHA!!!"
    time.sleep(1)
    for character in text:
        print(end=character, flush = True)
        time.sleep(quickdialog)
    print("                                                                   >>>", end = "")
    input()
    print()
    print("[A] KICK MOBSTER!\n[B] Do nothing.")
    fightanswer = input("Select an option:   ")

    if fightanswer == "A" or fightanswer == "a":
        print()
        print("You kick him in the nose with your other foot.                                       >>>", end = "")
        input()
        print("Why didn’t he grab both of your feet?                                                >>>", end = "")
        input()
        print("You barely make it over the fence.                                                   >>>", end = "")
        input()
    elif fightanswer == "B" or fightanswer == "b":
        print()
        print("You're done fighting. The dream of being rich was fun while it lasted.               >>>", end = "")
        input()
        print("The moment you go limp the fence flips over.                                         >>>", end = "")
        input()
        print("The fence flips back and hits the mobster on their face.                             >>>", end = "")
        input()
        print("You end up on the other side of the fence.                                           >>>", end = "")
        input()
    else:
        print()
        print("JIMMY: ", end = "")
        tiequestion = '"I\'m going to pretend you selected A."'
        for character in tiequestion:
            print(end=character, flush = True)
            time.sleep(dialog)
        print("                                        >>>", end = "")
        input()
        print()
        print("You kick him in the nose with your other foot.                                       >>>", end = "")
        input()
        print("Why didn’t he grab both of your feet?                                                >>>", end = "")
        input()
        print("You barely make it over the fence.                                                   >>>", end = "")
        input()
    print("Without any other options you hide in a poorly built dog house nearby.               >>>", end = "")
    input()
    print("The growling Schnauzer sitting next to you would be a lot scarier on any other day.  >>>", end = "")
    input()
    print("As they land, the Schnauzer switches attention to them and runs out barking.         >>>", end = "")
    input()
    print("The Mobsters scream like children and run away from the dog.                         >>>", end = "")
    input()
    print("You’re starting to question why you were even scared of them in the first place.     >>>", end = "")
    input()
    print("You know it’s not yours, and it almost got you buried in the Mojave Desert.          >>>\n", end = "")
    print("...And yet, you went through a hell of a lot of trouble to protect it...             >>>\n", end = "")
    print()
    print("Time for a serious decision! What do you do?                                         >>>", end = "")
    
    input()
    print()
    optionchB1()


#==============================================================================================#
                                  # CHAPTER A2 SCRIPT #
#==============================================================================================#

def printchA2():

    print()
    print()
    input("PRESS ENTER TO START ")
    print()
    print()
    print()
    print("You only got half as much for the diamond than you would’ve at auction.              >>>", end = "")
    input()
    print("You also sold it illegally so beggars can’t be choosers.                             >>>", end = "")
    input()
    print("Given the circumstances, you couldn’t stay in the country.                           >>>", end = "")
    input()
    print("The Mob is looking for you, and the IRS will wonder how you got all that cash.       >>>", end = "")
    input()
    print("You used your money to get a new identity, and a small beach house in Belize.        >>>", end = "")
    input()
    print("The house itself isn’t much to brag about, but the shoreline is beautiful!           >>>", end = "")
    input()
    print("Your diamond money won’t last forever, though, and the Mob may still find you.       >>>", end = "")
    input()
    print("In the end, you managed to become resourceful.                                       >>>", end = "")
    input()
    print("And now make passive income from the stock market.                                   >>>", end = "")
    input()
    print("So far, things don't look too bad. You take time to enjoy the little things in life. >>>", end="")
    input()
    print("You sit on your porch and watch the sunset over the sea.                             >>>", end = "")
    input()
    print("Your future may be uncertain, but at this moment you’re content.                     >>>", end = "")
    input()
    print()
    print()
    line0 = 'GAME OVER'
    for character in line0:
        print(end=character, flush=True)
        time.sleep(GAMEOVER)
    print("\n")
    line1 = 'CONGRATULATIONS!'
    for character in line1:
        print(end=character, flush=True)
        time.sleep(dialog)
    print("\n")
    line2 = 'You got the GOOD ENDING!'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
    print()
    print()
    input("PRESS ENTER TO RETURN TO MAIN MENU ")
    time.sleep(1.5)
    gameStart()

#==============================================================================================#
                                  # CHAPTER B2 SCRIPT #
#==============================================================================================#

def printchB2():

    print()
    print()
    input("PRESS ENTER TO START ")
    print()
    print()
    print()
    line1 = 'PHILANTHROPIST: '
    print(line1, end = "")
    time.sleep(1)
    line2 = '"Thanks for returning my stone, ole’ chap!'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
    input("                           >>>")
    print()
    print("All things considered, things turned out okay!                                       >>>", end = "")
    input()
    print("The police found your story hard to swallow - because frankly, it’s absurd!          >>>", end = "")
    input()
    print("Fortunately the philanthropic owner of the diamond isn’t pressing charges.           >>>", end = "")
    input()
    print("He’s just happy to put it back in his museum.                                        >>>", end = "")
    input()
    print("You tell your sad, dangerous, and bonkers story to the philanthropist.               >>>", end = "")
    input()
    print("He smiles through his thick mustache.                                                >>>", end = "")
    input()
    print()
    line1 = 'PHILANTHROPIST: '
    print(line1, end = "")
    time.sleep(1)
    line2 = '"That sounds like the plot to a ludicrous video-game!'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
    input("                >>>")
    line2 = '                "You must be completely mad to have endured that!'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
    input("                    >>>")
    print()
    line2 = '"...'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(.65)
    print(" Is that a compliment?\"                                                          >>>", end = "")
    input()
    print()
    print("The philanthropist takes a moment to process your story.                             >>>", end = "")
    input()
    print("As he strokes his mustache in thought, his eyes suddenly light up.                   >>>", end = "")
    input()
    print()
    line1 = 'PHILANTHROPIST: '
    print(line1, end = "")
    time.sleep(1)
    line2 = '"Say... are you looking for work?'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
    input("                                    >>>")
    print()
    print("Turns out, he’s the leader of a foreign expedition team.                             >>>", end = "")
    input()
    print("What’s more, he wants you to join said team!                                         >>>", end = "")
    input()
    print("It will involve adventuring the globe and seeking out priceless treasures.           >>>", end = "")
    input()
    print("You will be guarded by well-trained, anti-mob Schnauzers.                            >>>", end = "")
    input()
    print("And the pay doesn’t suck!                                                            >>>", end = "")
    input()
    print()
    line2 = 'So... what do you say?'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
    input("                                                               >>>")
    print()
    print()
    line0 = 'GAME OVER'
    for character in line0:
        print(end=character, flush=True)
        time.sleep(GAMEOVER)
    print("\n")
    line1 = 'CONGRATULATIONS!'
    for character in line1:
        print(end=character, flush=True)
        time.sleep(dialog)
    print("\n")
    line2 = 'You got the BEST ENDING!'
    for character in line2:
        print(end=character, flush=True)
        time.sleep(dialog)
    print()
    print()
    input("PRESS ENTER TO RETURN TO MAIN MENU ")
    time.sleep(1.5)
    gameStart()






#==============================================================================================#

#################################################################################
## CHAPTER 1 MENU                                                              ##
#################################################################################

#==============================================================================================#


def optionch1():
    print("[A] Take the Diamond!")
    print("[B] Put it down, leave, forget you ever saw it!")
    print("[1] Mark as checkpoint")
    print("[2] Return to main menu")
    print("[3] Exit game")
    c1input = input("Select an option:   ")

    if c1input == "A" or c1input == "a":
        print()
        printchA()

    if c1input == "B" or c1input == "b":
        print()
        printchB()
    
    if c1input == "1":
        chapterVALUE = 1
        saveChapter = open("diamond.pickle", "wb")
        pickle.dump(chapterVALUE, saveChapter)
        saveChapter.close()
        print()
        loading = "Marking as checkpoint..."
        for character in loading:
            print(end=character, flush=True)
            time.sleep(dialog)
        print()
        print("Checkpoint saved!")
        time.sleep(2.5)
        print()
        print()
        optionch1()

    if c1input == "2":
        print()
        print()
        print("Are you sure you want to return to the main menu?")
        print("Any unsaved progress will not be saved.")
        print("[1] No\n[2] Yes")
        areyousure = input("Select an option:   ")
        if areyousure == "1":
            print()
            print()
            print("Please choose an option.")
            print()
            optionch1()

        if areyousure == "2":
            print()
            print()
            print("RETURNING TO MAIN MENU")
            print()
            print()
            time.sleep(2.5)
            gameStart()

        else:
            print()
            print()
            print("Sorry, that is not an option.")
            print("Please try again.\n")
            print()
            optionch1()


    if c1input == "3":
        print()
        print()
        print("Are you sure you want to quit?")
        print("[1] No\n[2] Yes")
        areyousure = input("Select an option:   ")
        if areyousure == "1":
            print()
            print()
            print("Please choose an option.")
            print()
            optionch1()
        if areyousure == "2":
            print()
            print()
            quitgreeting = "Thank you for playing!\n\n"
            for character in quitgreeting:
                print(end=character, flush = True)
                time.sleep(.075)
            input("Press ENTER to quit, or close window. ")

        else:
            print()
            print()
            print("Sorry, that is not an option.")
            print("Please try again.\n")
            print()
            optionch1()


        quit()
    
    else:
        print()
        print("Please choose an option.")
        print()
        optionch1()


#################################################################################
## CHAPTER A MENU                                                              ##
#################################################################################

def optionchA():

    print("[A] Give it back - you don’t want any trouble!")
    print('[B] “RUN!!!”')
    print("[1] Mark as checkpoint")
    print("[2] Return to main menu")
    print("[3] Exit game")
    c1input = input("Select an option:   ")

    if c1input == "A" or c1input == "a":
        print()
        printchA1()

    if c1input == "B" or c1input == "b":
        print()
        printchB1()

    if c1input == "1":
        chapterVALUE = 2
        saveChapter = open("diamond.pickle", "wb")
        pickle.dump(chapterVALUE, saveChapter)
        saveChapter.close()
        print()
        loading = "Marking as checkpoint..."
        for character in loading:
            print(end=character, flush=True)
            time.sleep(dialog)
        print()
        print("Checkpoint saved!")
        time.sleep(2.5)
        print()
        print()
        optionchA()

    if c1input == "2":
        print()
        print()
        print("Are you sure you want to return to the main menu?")
        print("Any unsaved progress will not be saved.")
        print("[1] No\n[2] Yes")
        areyousure = input("Select an option:   ")
        if areyousure == "1":
            print()
            print()
            print("Please choose an option.")
            print()
            optionchA()

        if areyousure == "2":
            print()
            print()
            print("RETURNING TO MAIN MENU")
            print()
            print()
            time.sleep(2.5)
            gameStart()

        else:
            print()
            print()
            print("Sorry, that is not an option.")
            print("Please try again.\n")
            print()
            optionchA()

    if c1input == "3":
        print()
        print()
        print("Are you sure you want to quit?")
        print("[1] No\n[2] Yes")
        areyousure = input("Select an option:   ")
        if areyousure == "1":
            print()
            print()
            print("Please choose an option.")
            print()
            optionchA()
        if areyousure == "2":
            print()
            print()
            quitgreeting = "Thank you for playing!\n\n"
            for character in quitgreeting:
                print(end=character, flush = True)
                time.sleep(.075)
            input("Press ENTER to quit, or close window. ")
        else:
            print()
            print()
            print("Sorry, that is not an option.")
            print("Please try again.\n")
            print()
            optionchA()


        quit()
    
    else:
        print()
        print("Please choose an option.")
        print()
        optionchA()



#------------------------------------------------
# CHAPTER B HAS NO MENU




# CHAPTER A1 HAS NO MENU

#################################################################################
## CHAPTER B1 MENU                                                             ##
#################################################################################


def optionchB1():
    print("[A] I've had enough! I'll turn it in to the police...")
    print('[B] “MY PRECIOUS!!!”')
    print("[1] Mark as checkpoint")
    print("[2] Return to main menu")
    print("[3] Exit game")
    c1input = input("Select an option:   ")

    if c1input == "A" or c1input == "a":
        print()
        printchB2()
        

    if c1input == "B" or c1input == "b":
        print()
        printchA2()
        

    if c1input == "1":
        chapterVALUE = 3
        saveChapter = open("diamond.pickle", "wb")
        pickle.dump(chapterVALUE, saveChapter)
        saveChapter.close()
        print()
        loading = "Marking as checkpoint..."
        for character in loading:
            print(end=character, flush=True)
            time.sleep(dialog)
        print()
        print("Checkpoint saved!")
        time.sleep(2.5)
        print()
        print()
        optionchB1()

    if c1input == "2":
        print()
        print()
        print("Are you sure you want to return to the main menu?")
        print("Any unsaved progress will not be saved.")
        print("[1] No\n[2] Yes")
        areyousure = input("Select an option:   ")
        if areyousure == "1":
            print()
            print()
            print("Please choose an option.")
            print()
            optionchB1()

        if areyousure == "2":
            print()
            print()
            print("RETURNING TO MAIN MENU")
            print()
            print()
            time.sleep(2.5)
            gameStart()

        else:
            print()
            print()
            print("Sorry, that is not an option.")
            print("Please try again.\n")
            print()
            optionchB1()

    if c1input == "3":
        print()
        print()
        print("Are you sure you want to quit?")
        print("[1] No\n[2] Yes")
        areyousure = input("Select an option:   ")
        if areyousure == "1":
            print()
            print()
            print("Please choose an option.")
            print()
            optionchB1()
        if areyousure == "2":
            print()
            print()
            quitgreeting = "Thank you for playing!\n\n"
            for character in quitgreeting:
                print(end=character, flush = True)
                time.sleep(.075)
            input("Press ENTER to quit, or close window. ")
        else:
            print()
            print()
            print("Sorry, that is not an option.")
            print("Please try again.\n")
            print()
            optionchB1()


        quit()
    
    else:
        print()
        print("Please choose an option.")
        print()
        optionchB1()

    


#----------------------------------------------------------------------------#    
#     START UP MENU                                                          #
#----------------------------------------------------------------------------#
class Path:
    def __init__(self, path, value):
        self.path = path
        self.value = value


def Tutorial():
    print('Press ENTER when you see ">>>" to generate the next part of the story.')
    print("When prompted, type in the option you would like to perform.\nHit ENTER to submit responses.\n")
    input("Press ENTER to continue. ")
    print()
    
    

def start_up_menu_prints():
    print("[0] How to play")
    print("[1] Start a new game")
    print("[2] Continue from checkpoint")
    print("[3] Exit game")


    menu_prompt = input("Select an option:   ")


    if menu_prompt == "0":
        print("\n")
        Tutorial()
        print("\n")
        start_up_menu_prints()


    elif menu_prompt == "1":
        print()
        print()
        printch1()

    
    elif menu_prompt == "2":
        chapterVALUE = 0
        load = open("diamond.pickle", "rb")
        loadChapter = pickle.load(load)        

        if chapterVALUE+loadChapter == 0:
            print()
            sorry = "Sorry, there is no checkpoint saved."
            for character in sorry:
                print(end=character, flush=True)
                time.sleep(dialog)
            time.sleep(1.5)
            print()
            print()
            start_up_menu_prints()
            
        if chapterVALUE+loadChapter == 1:
            print()
            loading = "Loading checkpoint..."
            for character in loading:
                print(end=character, flush=True)
                time.sleep(dialog)
            savechapter1()
        if chapterVALUE+loadChapter == 2:
            print()
            loading = "Loading checkpoint..."
            for character in loading:
                print(end=character, flush=True)
                time.sleep(dialog)
            savechapterA()
        if chapterVALUE+loadChapter == 3:
            print()
            loading = "Loading checkpoint..."
            for character in loading:
                print(end=character, flush=True)
                time.sleep(dialog)
            savechapterB1()
        
    
    elif menu_prompt == "3":
        print()
        print()
        print("Are you sure you want to quit?")
        print("[1] No\n[2] Yes")
        areyousure = input("Select an option:   ")
        if areyousure == "1":
            print()
            print()
            print("Please choose an option.")
            print()
            start_up_menu_prints()
        if areyousure == "2":
            print()
            print()
            quitgreeting = "Thank you for playing!\n\n"
            for character in quitgreeting:
                print(end=character, flush = True)
                time.sleep(.075)
            input("Press ENTER to quit, or close window. ")
        else:
            print()
            print()
            print("Sorry, that is not an option.")
            print("Please try again.\n")
            print()
            start_up_menu_prints()


        quit()


    else:
        print("\n")
        print("Sorry, that is not an option.")
        print("Please try again.\n")
        start_up_menu_prints()

# CHAPTER SHORTCUTS FOR PICKLE PROGRAMMING #
# printch1() chapterVALUE = 1
# printchA() chapterVALUE = 2
# printchB() BAD END
# printchA1() WORST END
# printchB1() chapterVALUE = 3

#==============================================================================================#
# GAME START / Loop
#==============================================================================================#


#----------------------------#
#DELETE THIS AFTER TESTING!!!!!!!!!!!!!!

#savechapter1()
#savechapterA()
#savechapterB1()

#printch1()
#printchA()
#printchB()
#printchB1()
#printchA1()
#printchB2()
#printchA2()

#----------------------------#

def gameStart():
    print_intro()
    start_up_menu_prints()

#Loop
gameStart()


 









#diamond icon file
#c:\users\jimmy\pictures\projects\dms_icon.ico


#python file
#C:\Users\jimmy\Documents\CYOA_PROGRAMMING\DMS.py

#pyinstaller -F -i <iconfile> <pythonfile>


#pyinstaller -F -i c:\users\jimmy\pictures\projects\dms_icon.ico C:\Users\jimmy\Documents\CYOA_PROGRAMMING\DMS.py


#pyinstaller -F -i C:\Users\jimmy\Pictures\Projects\dms_icon.ico C:\Users\jimmy\Documents\CYOA_PROGRAMMING\DMS.py

#pyinstaller -F -i C:\Users\jimmy\Pictures\Projects\dms_icon.ico C:\Users\jimmy\Documents\CYOA_PROGRAMMING\DMS.py
