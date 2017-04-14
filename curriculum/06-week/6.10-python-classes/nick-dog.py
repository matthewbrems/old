class dog:
    def __init__(self, name, breed, age=10, is_hungry=True):
        self.breed = breed
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
        self.prodigy = []
        
    def __repr__(self):
        hunger = "hungry" if self.is_hungry else "not hungry"
        if self.prodigy:
            return'I am a {} of age {} who is {}. I have {} pup(s) named {}'.\
        format(self.breed, self.age, hunger, len(self.prodigy), ' and '.join([x.name for x in self.prodigy]))
        
        else:
            
            return'I am a {} of age {} who is {}'.format(self.breed,
                                                    self.age,
                                                    hunger)
    def set_weight(self, weight):
        self.weight = weight
        
    def go_for_a_run(self, length):
        print('your dog is going for a run for {} minutes').format(length)
    
    def eat(self):
        print('{} is eating'.format(self.name))
        self.is_hungry = False
        
    def reproduce(self, name):
        self.prodigy.append(dog(name, self.breed))