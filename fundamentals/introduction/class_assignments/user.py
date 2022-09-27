from os import umask
from runpy import run_module
from xml.etree.ElementPath import get_parent_map


class user:
    def __init__(self, firstname, lastname, email, age, rewards_member=False, gold_card_points=0 ):
        self.first_name= firstname
        self.last_name= lastname
        self.email= email 
        self.age= age
        self.is_rewards_member = rewards_member
        self.gold_card_points = gold_card_points
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(f"Gold card points = {self.gold_card_points}")

    def enroll(self):
        if (self.is_rewards_member==False):
            self.is_rewards_member=True
            self.gold_card_points=200
        else:
            return True

    def spend_points(self, amount):
        if(self.gold_card_points < amount):
            print("User can't spend more points than they have!")
            return False
        else:
            self.gold_card_points-=amount


user_thane = user("Thane", "Abel", "thaneemail@email.com", 427, True)

user_shark = user("Shark", "Of the Covenant", "sharkofthecovenant@sharks.shark", 126, False)

user_shark.display_info()

user_shark.enroll()

user_shark.spend_points(50)

user_shark.display_info()

user_thane.spend_points(80)

user_thane.display_info()
