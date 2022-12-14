import random
import time
import pickle
import os

from welcome import welcome_message
from login import user_login


# Save game state at any point in play to be recovered 
class Game:
    def __init__(self, username):
        self.user = username
        self.level = 1
        self.hero_health = 100
        self.sebbac_health = 100
        self.sebbac_last_move = 0

def print_congrats(hero_action):
    r = random.random()
    if r < 0.25:
        print("Congrats. That was a Great Hit!!")
    elif r < 0.5:
        print("Nice Move!! Hit Sebacc harder!")
    elif r < 0.75:
        print("You " + hero_action + " well! Finish him off")
    else:
        print("Well done! Sebbac got Damage!")

def print_sorry(sebbac_action):
    r = random.random()
    if r < 0.25:
        print("Damn! You got Hit!!")
    elif r < 0.5:
        print("Bad.... Move!! Absorb the damage")
    elif r < 0.75:
        print("Sebbac " + sebbac_action + " you! Get back on your feet!")
    else:
        print("You got some Damage! Get up & fight!!")

def print_health(hero_health, sebbac_health):
    print("---------------------------------")
    print(f"Hero_health is {hero_health}")
    print(f"Sebbac_health is {sebbac_health}")
    print("---------------------------------")


def check_leaderboard(username, score):
    users, scores = [], []
    with open('resources/leaderboard.txt', 'r') as lbf:
        for line in lbf:
            if len(line.strip()) > 0:
                a = line.split(",")
                if len(a) == 2:
                    users.append(a[0].strip())
                    scores.append(int(a[1].strip()))

    data = dict(zip(users, scores))

    if len(scores) < 5 or score > min(scores):
        # must be added to the leader board
        # if the user already exists then update their score -
        # if greater than their existing score
        if username in users:
            if score > data.get(username):
                print("Congrats! Your Leaderboard Updated!")
                data[username] = score
        else:
            # add a new user
            print("Congrats! You got into the Leaderboard!")
            data[username] = score

    # sort the dictionary in order
    sorted_data = sorted(data.items(), key=lambda item: -item[1])

    # write to the leaderboard (only top 5)
    i = 0
    with open("resources/leaderboard.txt", "w") as lbf:
        print("\n----------------\nLead board\n-----------------")
        print("User\tScore\n-------------------")
        for user, score in sorted_data:
            i += 1
            if i > 5:
                break
            print("%s \t %s"%(user, score))
            lbf.write(user + "," + str(score) + '\n')


def save_state(game_state):    
    print("The game is Paused!\nSaving the current Game state...")
    filename = os.path.join('resources', game_state.user + ".pkl")
    with open(filename, 'wb') as f:
        pickle.dump(game_state, f)
    
    quit()


#============================================================================================
# Level One
#============================================================================================

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
    hero_accuray = [0.7, 0.5, 0.2, 0.8]
    hero_power = [10, 20, 30]
    # the accuracy & power of sebbac & hero are the same in level 1
    sebbac_accuray = [0.7, 0.5, 0.2, 0.8]
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
                    print("Block by Sebbac failed!!")
                    sebbac_got_hit = True
                else:
                    print("Succesful block by Sebacc")
            
            else:
                print("In-accurate action by You")


        # print a congratulatory message if sebbac got a hit
        if sebbac_got_hit:
            print_congrats(hero_action)
            sebbac_health -= hero_power[hero_action_index]
            if sebbac_health <= 0:
                # stop
                hero_won = True
                break

        # decide hero action
        print("Press 1 to punch, press 2 to kick, press 3 to stab, press 4 to block: ")
        action = input("Press ANY other key to PAUSE the game: ")
        if action in ['1', '2', '3', '4']:
            action = int(action) - 1
            hero_action = actions[action]
        else:
            # need to pause the game
            game_state.hero_health = hero_health
            game_state.sebbac_health = sebbac_health
            game_state.sebbac_last_move = sebbac_action
            save_state(game_state)
        
        print("You " + hero_action)

        # convert action to a number
        hero_action_index = actions.index(hero_action)

        hero_got_hit = False
        if sebbac_action != "blocked":
            if random.random() < sebbac_accuray[sebbac_action_index]:
                # the action of sebbac is accurate
                if hero_action != "blocked":
                    # hero will take a hit
                    hero_got_hit = True
                elif random.random() > hero_accuray[3]:
                    # if sebbacc failed to block
                    print("Your Block failed!!")
                    hero_got_hit = True
                else:
                    print("Your block was successful")

            else:
                print("In-accurate action by Sebbac")
        
        # print a sorry message if the hero got a hit
        if hero_got_hit:
            print_sorry(sebbac_action)
            hero_health -= sebbac_power[sebbac_action_index]
            if hero_health <= 0:
                # stop
                hero_won = False
                break
        
        print_health(hero_health, sebbac_health)

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
        check_leaderboard(game_state.user, hero_health)
    
    else:
        print("Hawkman got killed! Dr. Fate will fight Sebbac in Level 2")
        print("Good luck! See you Level Two") 
        levelTwo(game_state) 


#============================================================================================
# Level Two
#============================================================================================

def levelTwo(game_state):
    print("""
            +-+-+-+-+-+ +-+-+-+             
            |L|E|V|E|L| |T|W|O|             
 +-+-+-+-+-+-+++-+-+-+-+++-+-+++-+-+-+-+-+-+
 |D|O|C|T|O|R| |F|A|T|E| |V|S| |S|E|B|B|A|C|
 +-+-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+-+-+
    """)

    game_state.level = 2
    print("You have the powers of A-Amon (Increased power) & Z-Zehuti (Scholarly wisdom)")
    print("You have S-Shu & H-Hours as well. (SHAZ of SHAZAM)")
    hero_health = 120
    allowed_time = 100
    # Sebbac starts with a health of 100
    sebbac_health = 100

    # weapons accuracy & power
    hero_accuray = [0.7, 0.5, 0.2, 0.8]
    hero_power = [15, 25, 35]
    # the power of sebbac is slightly lower than Dr. Fate in level 2
    sebbac_accuray = [0.7, 0.5, 0.2, 0.8]
    sebbac_power = [10, 20, 30]

    print("\n Fasten your trousers Dr. Fate! Fighting Begins!!!!! ")

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
                    print("Block by Sebbac failed!!")
                    sebbac_got_hit = True
                else:
                    print("good block by Sebbac")
            else:
                print("In-accurate action by You")
        
        # print a congratulatory message if sebbac got a hit
        if sebbac_got_hit:
            print_congrats(hero_action)
            sebbac_health -= hero_power[hero_action_index]
            if sebbac_health <= 0:
                # stop
                hero_won = True
                break

        # decide hero action
        print("Press 1 to punch, press 2 to kick, press 3 to stab, press 4 to block: ")
        action = input("Press ANY other key to PAUSE the game: ")
        if action in ['1', '2', '3', '4']:
            action = int(action) - 1
            hero_action = actions[action]
        else:
            # need to pause the game
            game_state.hero_health = hero_health
            game_state.sebbac_health = sebbac_health
            game_state.sebbac_last_move = sebbac_action
            save_state(game_state)
        
        print("You " + hero_action)

        # convert action to a number
        hero_action_index = actions.index(hero_action)

        hero_got_hit = False
        if sebbac_action != "blocked":
            if random.random() < sebbac_accuray[sebbac_action_index]:
                # the action of sebbac is accurate
                if hero_action != "blocked":
                    # hero will take a hit
                    hero_got_hit = True
                elif random.random() > hero_accuray[3]:
                    # if sebbacc failed to block
                    print("Your Block failed!!")
                    hero_got_hit = True
                else:
                    print("Your block was good!")
            
            else:
                print("In-accurate action by Sebbac")

        # print a sorry message if the hero got a hit
        if hero_got_hit:
            print_sorry(sebbac_action)
            hero_health -= sebbac_power[sebbac_action_index]
            if hero_health <= 0:
                # stop
                hero_won = False
                break

        print_health(hero_health, sebbac_health)

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
        print("Congratulations. Dr. Fate defeated Sebbac in Level 2! ")
        print(f"Your score is {hero_health}")
        print("You get a bonus of 100 points!")
        hero_health += 100
        if elapsed_time < (allowed_time - 20):
            print("You finished Sebbac in %d seconds" %(elapsed_time))
            print("You get a bonus of 50 points!")
            hero_health += 50

        print("Your total score is %d"%(hero_health))
        check_leaderboard(game_state.user, hero_health)
    
    else:
        print("Dr. Fate got killed! Black Adam will fight Sebbac in Level 3")
        print("Good luck! See you Level Three")
        levelThree(game_state)   



#============================================================================================
# Level Three
#============================================================================================

def levelThree(game_state):
    print("""
                  +-+-+-+-+-+ +-+-+-+-+-+         
                  |L|E|V|E|L| |T|H|R|E|E|         
         +-+-+-+-+-+++-+-+-+-+++-+-+++-+-+-+-+-+-+
         |B|L|A|C|K| |A|D|A|M| |V|S| |S|E|B|B|A|C|
         +-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+-+-+
        """)

    game_state.level = 3
    print("You have the powers of A-Aten (Impervious to magic spells) & M-Mehen (Supreme Accuracy)")
    print("You have all the powers of SHAZAM in level 3")
    hero_health = 120
    allowed_time = 100
    # Sebbac starts with a health of 100
    sebbac_health = 100

    # weapons accuracy & power
    hero_accuray = [0.9, 0.9, 0.6, 0.8]
    hero_power = [15, 25, 35]
    # the power & accuracy of sebbac is lower than Black Adam in level 3
    sebbac_accuray = [0.7, 0.5, 0.3, 0.8]
    sebbac_power = [10, 20, 30]

    print("\n Fasten your trousers Black Adam! Fighting Begins!!!!! ")

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
                    print("Block by Sebbac failed!!")
                    sebbac_got_hit = True
                else:
                    print("good block by Sebbac")
            else:
                print("In-accurate action by You")
        
        # print a congratulatory message if sebbac got a hit
        if sebbac_got_hit:
            print_congrats(hero_action)
            sebbac_health -= hero_power[hero_action_index]
            if sebbac_health <= 0:
                # stop
                hero_won = True
                break

        # decide hero action
        print("Press 1 to punch, press 2 to kick, press 3 to stab, press 4 to block: ")
        action = input("Press ANY other key to PAUSE the game: ")
        if action in ['1', '2', '3', '4']:
            action = int(action) - 1
            hero_action = actions[action]
        else:
            # need to pause the game
            game_state.hero_health = hero_health
            game_state.sebbac_health = sebbac_health
            game_state.sebbac_last_move = sebbac_action
            save_state(game_state)
        
        print("You " + hero_action)

        # convert action to a number
        hero_action_index = actions.index(hero_action)

        hero_got_hit = False
        if sebbac_action != "blocked":
            if random.random() < sebbac_accuray[sebbac_action_index]:
                # the action of sebbac is accurate
                if hero_action != "blocked":
                    # hero will take a hit
                    hero_got_hit = True
                elif random.random() > hero_accuray[3]:
                    # if sebbacc failed to block
                    print("Your Block failed!!")
                    hero_got_hit = True
                else:
                    print("Your block was good!")
            
            else:
                print("In-accurate action by Sebbac")

        # print a sorry message if the hero got a hit
        if hero_got_hit:
            print_sorry(sebbac_action)
            hero_health -= sebbac_power[sebbac_action_index]
            if hero_health <= 0:
                # stop
                hero_won = False
                break

        print_health(hero_health, sebbac_health)

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
        print("Congratulations. Black Adam defeated Sebbac in Level 3! ")
        print(f"Your score is {hero_health}")
        if elapsed_time < (allowed_time - 20):
            print("You finished Sebbac in %d seconds" %(elapsed_time))
            print("You get a bonus of 50 points!")
            hero_health += 50

        print("Your total score is %d"%(hero_health))
        check_leaderboard(game_state.user, hero_health)
    
    else:
        print("Black Adam got killed! Sad Ending")
         



# Main section; display welcome message
welcome_message()
# Ask user to login/signup
user_name = user_login()

# check whether the game state is present to continue the game
state_loaded = False
filename = os.path.join('resources', user_name + '.pkl')
if os.path.exists(filename):
    print("Do you want to continue from where you left off last time?")
    opt = input("1. Yes (Continue) 2. No (Restart the Game): ")
    if opt == '1'
        # recover game state
        with open(filename, 'rb') as f:
            game_state = pickle.load(f)
            state_loaded = True
            level = str(game_state.level)

if not state_loaded:
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


