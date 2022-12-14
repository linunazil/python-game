import random
import time

from welcome import welcome_message
from login import user_login


# Save game state at any point in play to be recovered 
class Game:
    def __init__(self, username):
        self.user = username
        self.level = 1
        self.health = 100
        self.sebacc_health = 100
        self.sebacc_last_move = 0
        self.weapons = []

def print_congrats(hero_action):
    r = random.random()
    if r < 0.25:
        print("Great Hit!!")
    elif r < 0.5:
        print("Nice Move!!")
    elif r < 0.75:
        print("You " + hero_action + " well!")
    else:
        print("Sebbac got Damage!")

def print_sorry(sebbac_action):
    r = random.random()
    if r < 0.25:
        print("Damn! You got Hit!!")
    elif r < 0.5:
        print("Bad.... Move!! Absorb the damage")
    elif r < 0.75:
        print("Sebbac " + hero_action + " you!")
    else:
        print("You got some Damage! Get up & fight!!")


def levelOne(game_state):
    print("""
       +-+-+-+-+-+ +-+-+-+          
       |L|E|V|E|L| |O|N|E|          
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |H|A|C|K|M|A|N| |V|S| |S|E|B|B|A|C|
    +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+

    """)
    game_state.level = 1
    print("You have the powers of S-Shu (increased stamina) & H-Horus (increased speed)")
    print("Do you want to avail 'S-H' powers of SHAZAM? (you will have lesser time to fight though)")
    option1 = input("1. Yes Get me Shu & Horus powers! 2. No. I am good: ")
    if option1 == '1':
        print("\nCongrats! You got Shu & Horus powers! Now you have extended health & better Speed")
        hero_health = 120
        allowed_time = 100 # 100 seconds
    else:
        hero_health = 100
        allowed_time = 120 # 2 minutes
    
    # Sebbac starts with a health of 100
    sebbac_health = 100

    # weapons accuracy & power
    hero_accuray = [0.7, 0.5, 0.3, 0.8]
    hero_power = [10, 20, 30]
    # the accuracy & power of sebbac & hero are the same in level 1
    sebbac_accuray = [0.7, 0.5, 0.3, 0.8]
    sebbac_power = [10, 20, 30]

    print("\n Fasten your trousers! Fighting Begins!!!!! ")

    # start level one timer
    start_time = time.time()
    elapsed_time = 0

    # list of weapons or actions
    actions = ["punched", "kicked", "stabbed", "blocked"]
    # Sebbac makes the first move!
    hero_action = "blocked" # just a start
    hero_action_index = 3
    # flag to indicate who won the game
    hero_won = False
    while True:
        # randomly sample an action for sebbac
        sebbac_action = random.sample(actions, 1)[0]
        print("Sebbac %s" % sebbac_action)
        sebbac_action_index = actions.index(sebbac_action)
        # check all possibilities of attacks on Sebbac
        sebbac_got_hit = False
        if hero_action != "blocked":
            if random.random() < hero_accuray[hero_action_index]:
                # the action of the hero is accurate
                if sebbac_action != "blocked":
                    # sebbac will take a hit
                    sebbac_got_hit = True
                elif random.random() > sebbac_accuray[3]:
                    # if sebbacc failed to block
                    print("Block failed!!")
                    sebbac_got_hit = True
        
        # print a congratulatory message if sebbac got a hit
        if sebbac_got_hit:
            print_congrats(hero_action)
            sebbac_health -= hero_power[hero_action_index]
            if sebbac_health <= 0:
                # stop
                hero_won = True
                break

        # decide hero action
        action = int(input("Press 1 to punch, press 2 to kick, press 3 to stab, press 4 to block: "))
        if action in [1, 2, 3]:
            hero_action = actions[action-1]
        else:
            hero_action = "blocked"
        
        # convert action to a number
        hero_action_index = actions.index(hero_action)

        print("You " + hero_action)

        hero_got_hit = False
        if sebbac_action != "blocked":
            if random.random() < sebbac_accuray[sebbac_action_index]:
                # the action of sebbac is accurate
                if hero_action != "blocked":
                    # hero will take a hit
                    hero_got_hit = True
                elif random.random() > hero_accuray[3]:
                    # if sebbacc failed to block
                    print("Block failed!!")
                    hero_got_hit = True
        
        # print a sorry message if the hero got a hit
        if hero_got_hit:
            print_sorry(sebbac_action)
            hero_health -= sebbac_power[sebbac_action_index]
            if hero_health <= 0:
                # stop
                hero_won = False
                break
        
        print(f"Hero_health is {hero_health}")
        print(f"Sebbac_health is {sebbac_health}")

        # update elapsed time
        elapsed_time = int(time.time() - start_time)
        if elapsed_time < allowed_time:
            print("Remaining Time: %d seconds" %(allowed_time - elapsed_time))
        else:
            print("Time over!")
            hero_won = False
            break
    
    # end of while loop
    if hero_won:
        print("Congratulations. Hawkman defeated Sebbac in Level 1 itslef! ")
        print(f"Your score is {hero_health}")
        print("You get a bonus of 200 points!")
        hero_health += 200
        if elapsed_time < (allowed_time - 20):
            print("You finished Sebbac in %d seconds" %(elapsed_time))
            print("You get a bonus of 50 points!")
            hero_health += 50

        print("Your total score is %d"%(hero_health))
    
    else:
        print("Hawkman got killed! Dr. Fate will fight Sebbac in Level 2")
        print("Good luck! See you Level Two")   



# Main section; display welcome message
welcome_message()
# Ask user to login/signup
user_name = user_login()
# create a game state for the current user
game_state = Game(user_name)

# Ask user to choose the level
print("\nChoose your Level\n----------------------")
print("Level 1: Hawkman will fight Sebbac")
print("Level 2: Dr. Fate will fight Sebbac")
print("Level 3: Black Adam will fight Sebbac")
print("Protip! Choose level 3 to kill Sebbac faster but Choose level 1 for more points")
level = input("1. Level One  2. Level Two  3. Level Three: ")

if level == '1':
    levelOne(game_state)
elif level == '2':
    levelTwo(game_state)
else:
    levelThree(game_state)


