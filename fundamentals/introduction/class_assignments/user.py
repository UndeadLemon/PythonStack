class user:
    def __init__(self, firstname, lastname, email, age, rewards_member=False, gold_card_points=0 ):
        self.first_name= firstname
        self.last_name= lastname
        self.email= email 
        self.age= age
        self.is_rewards_member = rewards_member
        self.gold_card_points = gold_card_points

user_thane = user("Thane", "Abel", "thaneemail@email.com", 427, True)

print(user_thane.gold_card_points)