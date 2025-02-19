class Animal:
    def __init__(self,name,eat,sleep,move,bite,swim): 
        self.name=name
        self.__eat_behavior=eat
        self.__sleep_behavior=sleep
        self.__move_behavior=move
        self.__bite_behavior=bite
        self.__swim_behavior=swim
        
    def talk(self):
        print("cat is purring")
    def eat(self):
        print("cat is eating" )
    def sleep(self):
        print(" cat is sleeping")
    def move (self):
        print("cat is walking")
    def bite(self):
        print(" cat is eating " ' "nom nom" ')
    def swim(self):
        print("cat is swiming")
      

