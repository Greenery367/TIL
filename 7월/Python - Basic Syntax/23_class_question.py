
class Juggling:
    def __init__(self):
        self.hp = 20
        self.mana = 50
    
    def run(self):
        print("뛴다")
        self.hp -= 1
        self.mana -= 1
        
    def show_status(self):
        print(f"현재 hp는 {self.hp} 입니다.")
        print(f"현재 mana는 {self.mana} 입니다.")
        
x1 = Juggling()
x2 = Juggling()

x1.run()
x1.show_status()

for i in range(5):
    x2.run()
    
x2.show_status()