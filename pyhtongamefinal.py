import random

Hero_health = 100
Sebbac_health = 100
boosted_flag1 = False
boosted_flag2 = False
boosted_flag3 = False
boosted_flag4 = False
boosted_flag5 = False
boosted_flag6 = False
boosted_flag7 = False

list1 = ["Sebbac punched", "Sebbac kicked", "Sebbac stabbed", "Sebbac blocked"]
list2 = ["Shu deployed ", "Horus deployed ", "Aten deployed", "Zehuti deployed ", "Mehen deployed ", " Amon deployed "]
slice1 = slice(0, 2)
slice2 = slice(0, 4)
slice3 = slice(0, 6)
list3 = list2[slice(0, 2)]
list4 = list2[slice(0, 4)]
list5 = list2[slice(0, 6)]



name = input("Enter your name: ")
level = input(f"Hi {name}, For LEVEL 1 press any key")

print("""
   +-+-+-+-+-+ +-+-+-+          
   |L|E|V|E|L| |O|N|E|          
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|H|A|C|K|M|A|N| |V|S| |S|E|B|B|A|C|
+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+

""")

while Hero_health > 0 and Sebbac_health > 0:
    Sebbac_action = random.sample(list1, 1)
    print(Sebbac_action)
    action = int(input("Press 1 to punch, press 2 to kick, press 3 to stab, press 4 to block. "))
    if action == 4:
        if random.random()<.8:
            print("Wow! attack blocked! ")
        else:
            print("You took a blow! ")
            Hero_health -= 15
    elif Sebbac_health < 20 and boosted_flag6 == False:
        print(random.sample(list3, 1))
        Sebbac_health += 20
        boosted_flag6 = True
    elif Sebbac_action == ["Sebbac blocked"]:
        if random.random()<.2:
            print("Sebbac blocked your punch!")

        else:
            print("You got him! ")

            Sebbac_health -= 15

    elif Hero_health < 25 and boosted_flag1 == False:
        skill = input("Press any key to deploy skills ")
        Hero_health += 20
        print(random.sample(list3, 1))
        boosted_flag1 = True
    elif action == 1 or action == 2 or action == 3:
        if random.random()< .7:
            print("damage! ")
            Hero_health -= 15

        random.random() < .7
        Sebbac_health -= 15
    else:
        print("Enter a valid key! ")
    print(f"Hero_health is {Hero_health}")
    print(f"Sebbac_health is {Sebbac_health}")
else:
    if Hero_health <= 0:
        print("You lost, try again ")

    else:
        print("You won! ")
        print(f"Your score is {Hero_health}")

        level2 = input("Enter 5 to quit or enter any other key to progress to Level 2  : ")

        if level2 == int(5):
            quit()
        else:
            print("""
            +-+-+-+-+-+ +-+-+-+             
            |L|E|V|E|L| |T|W|O|             
 +-+-+-+-+-+-+++-+-+-+-+++-+-+++-+-+-+-+-+-+
 |D|O|C|T|O|R| |F|A|T|E| |V|S| |S|E|B|B|A|C|
 +-+-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+-+-+
 """)

            Hero_health = 100
            Sebbac_health = 100

            while Hero_health > 0 and Sebbac_health > 0:
                Sebbac_action = random.sample(list2, 1)
                print(Sebbac_action)
                action = int(input("Press 1 to punch, press 2 to kick, press 3 to stab, press 4 to block. "))
                if action == 4:
                    if random.random()<.8:
                        print("Wow! attack blocked! ")

                    else:
                        print("You took a blow! ")
                        Hero_health -= 20
                elif Sebbac_health < 20 and boosted_flag5 == False:
                    print(random.sample(list4, 1))
                    Sebbac_health += 20
                    boosted_flag5 = True
                elif Sebbac_action == ["Sebbac blocked"]:
                    if random.random()<.3:
                        print("Sebbac blocked your punch!")

                    else:
                        print("You got him! ")

                        Sebbac_health -= 20

                elif Hero_health < 25 and boosted_flag2 == False:
                    stamina_boost = input("Press any key to deploy skills ")
                    Hero_health += 20
                    print(random.sample(list4, 1))
                    boosted_flag2 = True
                elif action == 1 or action == 2 or action == 3:
                    if random.random()< .6:
                        print("damage! ")
                        Hero_health -= 20
                    random.random()< .7
                    Sebbac_health -= 20
                else:
                    print("Enter a valid key! ")
                print(f"Hero_health is {Hero_health}")
                print(f"Sebbac_health is {Sebbac_health}")
            else:
                if Hero_health <= 0:
                    print("You lost, try again ")
                    quit
                else:
                    print("You won! ")
                    print(f"Your score is {Hero_health}")

                    level3 = input("Enter 5 to quit or enter any other key to progress to Level 3 ")

                    if level3 == int(5):
                        quit()
                    else:
                        print("""
                  +-+-+-+-+-+ +-+-+-+-+-+         
                  |L|E|V|E|L| |T|H|R|E|E|         
         +-+-+-+-+-+++-+-+-+-+++-+-+++-+-+-+-+-+-+
         |B|L|A|C|K| |A|D|A|M| |V|S| |S|E|B|B|A|C|
         +-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+-+-+
        """)

                        Hero_health = 100
                        Sebbac_health = 100

                        while Hero_health > 0 and Sebbac_health > 0:
                            Sebbac_action = random.sample(list3, 1)
                            print(Sebbac_action)
                            action = int(input("Press 1 to punch, press 2 to kick, press 3 to stab, press 4 to block. "))
                            if action == 4:
                                if random.random()<.8:
                                    print("Wow! attack blocked! ")

                                else:
                                    print("You took a blow! ")
                                    Hero_health -= 20
                            elif Sebbac_health < 20 and boosted_flag7 == False:
                                print(random.sample(list5, 1))
                                Sebbac_health += 20
                                boosted_flag7 = True
                            elif Sebbac_action == ["Sebbac blocked"] and Hero_health < 20:
                                print("Magic spell deployed! ")
                                Sebbac_health -= 30
                            elif Sebbac_action == ["Sebbac blocked"]:
                                if random.random()<.3:
                                    print("Sebbac blocked your punch!")

                                else:
                                    print("You got him! ")

                                    Sebbac_health -= 20


                            elif Hero_health < 25 and boosted_flag3 == False:
                                stamina_boost = input("Press any key to deploy skills ")
                                Hero_health += 20
                                print(random.sample(list5, 1))
                                boosted_flag3 = True
                            elif action == 1 or action == 2 or action == 3:
                                if random.random()< .7:
                                    print("damage! ")
                                    Hero_health -= 20
                                random.random()< .7
                                Sebbac_health -= 20
                            else:
                                print("Enter a valid key! ")
                            print(f"Hero_health is {Hero_health}")
                            print(f"Sebbac_health is {Sebbac_health}")
                        else:
                            if Hero_health <= 0:
                                print("You lost, try again ")
                                quit()
                            else:
                                print("You won! ")
                                print(f"Your score is {Hero_health}")
