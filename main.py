from gamedata import data
import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


score = 0

def choose_first(): #Chooses the first person
        number = random.randint(0,49)
        dictionary = data[number]
        first_name = dictionary['name']
        first_follower_count = int(dictionary['follower_count'])
        first_description = dictionary['description']
        first_country = dictionary['country']
        first_person = {'name': first_name,
                        'follower_count': first_follower_count,
                        'description': first_description, 
                        'country': first_country}
        return first_person

def choose_second(): #Chooses the second person
        number = random.randint(0,49)
        dictionary = data[number]
        second_name = dictionary['name']
        second_follower_count = int(dictionary['follower_count'])
        second_description = dictionary['description']
        second_country = dictionary['country']
        second_person = {'name': second_name,
                        'follower_count': second_follower_count,
                        'description': second_description, 
                        'country': second_country}
        return second_person

first = choose_first()
second = choose_second()

def changer(): #Changes the first peroson according to follower count
        
        global first
        global second
        first_follower_count = int(first['follower_count'])
        second_follower_count = int(second['follower_count'])
        if first_follower_count > second_follower_count:
                first = first
                return first
        elif first_follower_count < second_follower_count:
                first = second
                return first

def answer():
       first_follower_count = int(first['follower_count'])
       second_follower_count = int(second['follower_count'])
       if first_follower_count > second_follower_count:
              return 1
       elif first_follower_count < second_follower_count:
              return 2
       

stop = False
while not stop:
        
        first_name = first['name']
        first_follower_count = int(first['follower_count'])
        first_description = first['description']
        first_country = first['country']

        second_name = second['name']
        second_follower_count = int(second['follower_count'])
        second_description = second['description']
        second_country = second['country']
       
        clear()

        #----------------------------------------------------------------------------
        #print(first_follower_count,second_follower_count) 
        #if you want to cheat
        #-----------------------------------------------------------------------------
        print('THE HIGHER LOWER GAME!\n\n')

        print(f"Your score currently is = {score}")

        print(f"\n{first_name}, {first_description}, from {first_country}\n")
        print('''-------------------------
                VS
        ------------------------''')
        print(f"\n{second_name}, {second_description}, from {second_country}\n")
        
        choice = int(input('Who has more followers(1/2): '))
        if answer() == choice:
              score += 1
              stop = False
              first = changer()
              second = choose_second()
        else:
              print(f"Your score is = {score}")
              stop = True
 
time.sleep(5)