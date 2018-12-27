import random
##### PROBLEMS ASAP FIXXXX ####



##### To do list #####

#Function for all fight sequences?
###Double .format input? (x,y)

#List for funny player names, randint index?
###['Herbert', ' ']



##### UNI VARS #####
weapon = {"sword": 1}
fist = {"fists": 1}

##### ACTIONS #####
def you_died(why):
    print("{}. Good job!".format(why))
    play_again()
    

def play_again():
    print("Play again? [Y/N]")
    choice = input("> ").lower()
    print(' ')
    if choice in ["y", "yes"]:
        start_adventure()
    # This exits the program entirely.
    else:
        return
    
##### CHARACTERS #####
def guard():
    attack = weapon["sword"]
    in_fight = False
    guard1_hp = 5
    your_hp = 10
    crit = False
    print("You approach the guard, he's still sleeping.")
    print("Suddenly you knocked a wooden cask with a mug on it... CRASSH!")
    print("\n'Oi, what you doing 'ere?' The Guard says.")

    # Guard is not moving initially
    guard_moved = False
    hit = False
    while True:
        guard1_att = fist["fists"]
        if your_hp <= 0:
            you_died("HP reduced to {}.").format(your_hp)
        if guard1_hp <= 0:
            print("You beat the guard, and walk out the door. You're home free! Huzzah!")
            return
        #If they are in fight already, dont re-ask
        if in_fight == False:
            next_action = input("\nDo you try fighting the guard(in progress), running, or lunging for the exit? > ").lower()
        #Fight sequence
        if next_action in ["fight", "fighting"]:
            in_fight = True
            print("\nGuard's hp: {}".format(guard1_hp))
            #Enraged guard no good.
            if guard1_hp <= 2:
                print("The guard is enraged, and deals double damage")
                fist["fists"] *= 2
            print("The Guard's weapon is a {}.".format(fist))
            print("\nYour hp: {}".format(your_hp))
            print("Your weapon is a {}.".format(weapon))
            att_dir = input("\nThe guard runs at you. Do you attack his left or right side? >").lower()
            print(' ')
            #Guard_dir 1 is left, 2 is right
            guard_dir = random.randint(1,3)
            #If crit then one hit kill
            chance = random.randint(1,11)
            c = 5
            if chance == c:
                crit = True
            if crit == True:
                attack *= 10
            if guard_dir == 3: #dodge
                hit == False
                print("The guard dodges under your swing and hits you")
            elif att_dir in ["left", "left side", "l"] and guard_dir == 1: #hit
                hit = True
            elif att_dir in ["left", "left side", "l"] and guard_dir == 2: #miss
                hit = False
            elif att_dir in ["right", "right side", "r"] and guard_dir == 1: #miss
                hit = False
            elif att_dir in ["right", "right side", "r"] and guard_dir == 2: #hit
                hit = True
            else:
                print("You don't know how to swing that way, try left or right next time.")
            #Test if hit
            if hit == True:
                guard1_hp -= attack
                hit == False
                if crit == True:
                    attack /= 10
                    print("HEADSHOT! 10x damage, you dealt {} damage!".format(int(attack)))
                else:
                    print("Nice hit. You dealt {} damage.".format(attack))
            else:
                your_hp -= guard1_att
                print("Nice miss. You were hit for {} damage.".format(guard1_att))    
        else:
            if next_action in ["run", "run from guard", "flee"] and guard_moved:
                you_died("Guard was faster than he looks and your world goes dark...")
            elif next_action in ["run", "run from guard", "flee"] and not guard_moved:
                print("\nGuard jumps up and looks the other way, leaving the door unprotected")
                guard_moved = True
            elif next_action in ["door", "reach for door", "go for door"] and guard_moved:
                print("\nYou just slipped through the door before the guard realised it.")
                print("You are now outside, home free! Huzzah!")
                return 
            elif next_action == "door" and not guard_moved:
                you_died("Guard was faster than he looks and your world goes dark...")
            else:
                print("\nNot sure what you meant there... try again.")

##### ROOMS #####
def blissful_ignorance_of_illusion_room():
    treasure_chest = ["diamonds", "gold", "silver", "sword"]
    print("\nYou see a room with a wooden treasure chest on the left, and a sleeping guard on the right in front of the exit.")
    
    # Ask player what to do.
    action = input("What do you do? > ").lower()
    print(' ')

    # This is a way to see if the text typed by player is in the list
    if action in ["treasure", "chest", "treasure chest", "left", "go left", "l"]:
        print("Oooh, treasure!") 

        print("Open it? [Y/N]")
        choice = input("> ").lower()
        print(' ')
        if choice in ["y", "yes"]:
            print("Let's see what's in here...")
            print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
            print("You find some")

            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_chest list, print the treasure.
            for treasure in treasure_chest:
                print(treasure)

            # So much treasure, what to do? Take it or leave it.
            print(' ')
            print("What do you want to do?")
            print("To take all {} treasure(s), type '1'".format(len(treasure_chest)))
            print("To leave it, type '2'")

            treasure_choice = input("> ")
            print(' ')
            if treasure_choice == "1":
                print("Woohoo! Bounty and a shiny new sword.")
                weapon["sword"] += 1
                print("You drop your crappy sword in the empty treasure chest.")
                print("You just received [{}]".format(", ".join(treasure_chest)))
            elif treasure_choice == "2":
                print("It will still be here (I hope), right after I get past this guard")
            # Picked up treasure or left it, you will now encounter the guard.
            guard()
        else:
              print("What a shame. Even without opening it you caused the guard to wake up. Good Luck dealing with him.")
              guard()
    elif action in ["guard", "go for guard", "g", "right"]:
        guard()
    else:
        print("I'll take that as 'lets go for the guard!'")
        guard()


def painful_truth_of_reality_room():
    print("\nThere you see the great evil Cthulhu.")
    print("He, it, whatever stares into your soul and you go insane.")
    print("Do you flee for your life or eat your head?")

    next_move = input("> ").lower()
    print(' ')
    # Flee or die
    if next_move in ["flee", "run"]:
        print("Congrats, you lost your mind, aimlessly wandering until you find your way back to the beginning.")
        main()
    else:
        you_died("You died. Well, that was tasty!")
        
### Preliminaries ###
def get_player_name():
    # The player enters their name and gets assigned to a variable called "name"
    name = input("What's your name? > ")
    alt_name = "Rainbow Fluffy Unicorn"
    answer = input("Your name is {}, is that correct? [Y|N] > ".format(alt_name.upper()))
    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print("You are fun, {}! Let's begin our adventure!".format(name.upper()))
    elif answer.lower() in ["n", "no"]:
        print("Ok, picky. {} it is. Let's get started on our adventure.".format(name.upper()))
    else:
        print("Trying to be funny? Well, you will now be called {} anyway.".format(alt_name.upper()))
        name = alt_name
    return name

def start_adventure():
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you pick the red door or blue door? > ").lower()
    
    # Pick a door and we go to a room and something else happens
    if door_picked in ["red", "red door", "r", "left", "left door"]:
        painful_truth_of_reality_room()
    elif door_picked in ["blue", "blue door", "b", "right", "right door"]:
        blissful_ignorance_of_illusion_room()
    else:
        print("Its a simple choice. Just pick a door...")
        start_adventure()

def main():
    player_name =  get_player_name()
    print(' ')
    start_adventure()
    
    print("\nThe end\n")
    print("Thanks for playing, {}!".format(player_name.upper()))

### STARTS THE PROGRAM ###
main()
