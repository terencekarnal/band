class Musician(object):
    instances = []  
    def __init__(self, sounds):
        self.sounds = sounds
        self.instances.append(self) 

    def solo(self, length):
        for i in range(length):
           print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang", "Bong", "Bip", "Boop"])
        
    def count(self):
        print("1 2 3 4!")
        
    def spont_ouchy(self):
        print("BOOM")
        
nigel = Guitarist()

cindy = Bassist()

bro = Guitarist()

bart = Drummer()


class Band(object):
    def __init__(self):
        self.members = []
    
    def other_attributes(self):
        self.manager = "Mr Thinkful"
    
    def hire(self,person):
        self.members.append(person)
    
    def fire(self, person):
        self.members.remove(person)
    
    def play(self):
        self.members[0].count()
        
        for member in self.members:
            member.solo(4)
        
        self.members[0].spont_ouchy()
        
        
the_rosuavs = Band()
the_rosuavs.hire(bart)
the_rosuavs.hire(bro)
the_rosuavs.hire(cindy)
the_rosuavs.hire(nigel)

the_rosuavs.play()


        


#print("Number of musicians in the band: " + str(len(Musician.instances)))
