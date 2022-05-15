import time
import random


def print_pause(text):
    print(text)
    time.sleep(2)


def winOrLose(state):
    if state == 'win':
        playAgain = input('You win! Do you want to play again? Y/N')
        if playAgain in ['y', 'Y']:
            startGame()
        elif playAgain in ['n', 'N']:
            print("Thanks for playing!")
    elif state == 'lose':
        playAgain = input('You lose! Do you want to play again? Y/N')
        if playAgain in ['y', 'Y']:
            startGame()
        elif playAgain in ['n', 'N']:
            print("Thanks for playing!")


def valid_input(nextSection, currentSection, item=None):
    choice = input('Make your choice!')
    if choice in ['1', 1, '2', 2] and item is None:
        nextSection(choice)
    elif choice in ['1', 1, '2', 2] and item is not None:
        nextSection(choice, item)
    else:
        if item is not None:
            first = (input('Try again! Press 1 or 2.'))
            restart = currentSection
            restart(first, item)
        else:
            first = (input('Try again! Press 1 or 2.'))
            restart = currentSection
            restart(first)


def startGame():
    print_pause('You enter a dark, damp cave the sound '
                'of bats flying around is '
                'made even more frightening by the pitch '
                'blackness that surrounds you.')
    print_pause('You have been told that a treasure lies somewhere '
                'in this cave and you are determined to find it.')
    print('Press 1 to take out your torch.')
    print('Press 2 to take out your dagger.')
    first = (input('Make your choice!'))
    enterCave(first)


def enterCave(choice):
    if choice == "1" or choice == 1:
        print_pause('You decide to take out your torch '
                    'lighting it quickly against a dry rock.')
        print_pause('The cave is illuminated.')
        print_pause('With the light shining, you can see'
                    'hundreds of bats lining the ceiling of the cave.')
        print_pause('They seem to be sleeping, at least for now.')
        print('Press 1 to shout at the top of your lungs.')
        print('Press 2 to stay quiet and keep moving.')
        second = (input('Make your choice!'))
        torch(second)

    elif choice == "2" or choice == 2:
        print_pause('You decided to pull out your dagger.')
        print_pause('Your dagger brings you some comfort as '
                    'you feel your way along the wall of the cave.')
        print_pause('What do you want to do next?')
        print('Press 1 to listen closely to your surroundings.')
        print('Press 2 to keep walking.')
        second = (input('Make your choice!'))
        dagger(second)

    else:
        valid_input(enterCave, enterCave)


def torch(choice):
    if choice == "1" or choice == 1:
        print_pause('You decided to shout at the top of your lungs.')
        print_pause('The bats screeched into a massive '
                    'cloud of fuzzy claws.')
        print_pause('Although you were blinded for some time, when '
                    'your vision returns left before '
                    'you is a mystical portal!')
        print('Press 1 to enter portal.')
        print('Press 2 to continue down cave.')
        third = (input('Make your choice!'))
        portal(third)

    elif choice == "2" or choice == 2:
        print_pause('You decided to stay quiet and keep moving.')
        print_pause('As you continue down you start to '
                    'have doubts with the decision you made.')
        print_pause('Walking unarmed, a goblin catches '
                    'you off guard and kills you!')
        winOrLose('lose')

    else:
        valid_input(torch, torch)


def portal(choice):
    if choice == "1" or choice == 1:
        equipment = random.choice(["Magic Armor", "Short Sword"])
        print_pause('You enter the portal confidently '
                    'in hopes it will help you.')
        print_pause('When you enter, you are immediately '
                    'spat out but you have aquired something.')
        print_pause('You have acquired ' + equipment + '!')
        print('Press 1 to continue down cave a brave man.')
        print('Press 2 to turn back like a scared baby.')
        fourth = (input('Make your choice!'))
        portalItem(fourth, equipment)

    elif choice == "2" or choice == 2:
        print_pause('You continue walking down the cave '
                    'with nothing but a torch.')
        print_pause('As you continue down you start to get an '
                    'uneasy feeling and maybe think '
                    'you should turn around.')
        print_pause('But')
        print_pause('Before you can decide to turn '
                    'around to go back.')
        print_pause('A mighty dragon stands before you!!!')
        print_pause('Trembling in fear and defenseless, you '
                    'realize you made the wrong decision.')
        print_pause('The dragon opens his mouth and breathes '
                    'a blazing fire.')
        print_pause('Songs will be sung of you as the naive '
                    'peasant who didnt plan very well.')
        winOrLose('lose')

    else:
        valid_input(portal, portal)


def portalItem(choice, equipment):
    if choice == "1" or choice == 1:
        print_pause('You continue down the cave with a '
                    'sense of courage you once did not have before.')
        print_pause('As you walk down deep into the cave you '
                    'know you can take on anything.')
        print_pause('The moment you think that a furious dragon '
                    'aoppears and trys to destroy you with '
                    'his powerful fire breathe.')

        if equipment == "Magic Armor":
            print_pause('But the Magic Armor you aquired had fire '
                        'resistance which made you impervious '
                        'to his breathe.')
            print_pause('You manage to block his fire and '
                        'swiftly get around the slow dragon.')
            print_pause('Standing behind the dragon is a '
                        'small room filled with glorious treasure!!')
            print_pause('You see there is an exit tunnel '
                        'out of the cave to which you take.')
            print_pause('When you get out you take your riches into '
                        'town and share your wealth with the '
                        'people of the land.')
            print_pause('Now they will sing songs around campfires '
                        'of your kindness and braveness for all of time!!')
            winOrLose('win')

        elif equipment == "Short Sword":
            print_pause('A light of hope glistens in your eye.')
            print_pause('You grip the Short Sword by the handle '
                        'to prepare and attack!')
            print_pause('But you cant evade his breathe to '
                        'land an attack and the rest is history.')
            print_pause('Now when people gather around '
                        'campfires to sing songs of great people.')
            print_pause('You are left out as you couldnt slay the '
                        'dragon.')
            winOrLose('lose')

    elif choice == "2" or choice == 2:
        print_pause('You chose to turn around like a scaredy cat.')
        print_pause('Now when people gathering around campfires '
                    'they sing of your tale to get a good laugh.')
        winOrLose('lose')

    else:
        valid_input(portalItem, portalItem, equipment)


def dagger(choice):
    if choice == "1" or choice == 1:
        goblinItem = random.choice(["Leather Armor", "Magic Ring", "Nothing"])
        print_pause('You decide to listen closely to your surroundings')
        print_pause('Thanks to your keen sense of hearing '
                    'you detect a goblin nearby.')
        print_pause('Before he gets a chance to notice you, you surprise '
                    'him and are able to overtake him with your dagger.')
        print_pause('After winning the battle with the goblin you '
                    'search his body and find ' + goblinItem + '!')
        print('Press 1 to continue down cave.')
        print('Press 2 to run out of the cave.')
        sixth = (input('Make your choice!'))
        itemG(sixth, goblinItem)

    elif choice == "2" or choice == 2:
        print_pause('You decided to keep walking in the dark.')
        print_pause('Since your vision is bad to due to low light.')
        print_pause('You cant see and you fall down a trap hole and die.')
        winOrLose('lose')

    else:
        valid_input(dagger, dagger)


def itemG(choice, goblinItem):
    if choice == "1" or choice == 1:
        print_pause('You decided to continue down the cave.')
        print_pause('When you do you eventually come across '
                    'a mighty dragon guarding something.')
        print_pause('The dragon starts to ready his attack.')
        if goblinItem == "Leather Armor":
            print_pause('TheLeather Armor you aquired is equiped.')
            print_pause('Too bad fire burns right through leather!')
            print_pause('The songs sung over campfires can be told '
                        'apart from the roasting of turkey or of you.')
            winOrLose('lose')

        elif goblinItem == "Magic Ring":
            print_pause('The Magic Ring you aquired is equiped.')
            print_pause('You notice the ring gives you the power of '
                        'invisibility!')
            print_pause('This new found power allows you to sneak past '
                        'the dragon.')
            print_pause('After sneaking around him you find his '
                        'treasure and go out the back entrance of the cave.')
            print_pause('When you get into town you decide to '
                        'blow all the treasure on a new house and '
                        'unlimited turkey legs.')
            winOrLose('win')

        elif goblinItem == "Nothing":
            print_pause('Unfortunately you didnt aquire anything from '
                        'the goblin.')
            print_pause('The dragon disposes of you easily.')
            print_pause('No one is singing of you over no campfires.')
            winOrLose('lose')

    elif choice == "2" or choice == 2:
        print_pause('You decide to run out of the cave.')
        print_pause('You cannot pay the dept you are deeply in.')
        winOrLose('lose')

    else:
        valid_input(itemG, itemG, goblinItem)


if __name__ == '__main__':
    startGame()
