class Robot:
    def __init__(self, name, hp, attack, accuracy):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.accuracy = accuracy

    def attack_enemy(self, enemy):
        chance = self.accuracy * 100
        hit = int(chance) >= (100 - (enemy.attack % 100))
        if hit:
            damage = self.attack
            enemy.hp -= damage
            print(f'{self.name} menyerang {enemy.name} dan memberikan {damage} damage!')
        else:
            print(f'{self.name} gagal menyerang!')

    def regen_health(self):
        heal = 10
        self.hp += heal
        print(f'{self.name} memulihkan {heal} HP!')

    def is_alive(self):
        return self.hp > 0


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def play(self):
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f'\nRound-{self.round} ==========================================================')
            print(f'{self.robot1.name} [{self.robot1.hp}|{self.robot1.attack}]')
            print(f'{self.robot2.name} [{self.robot2.hp}|{self.robot2.attack}]')

            for robot, enemy in [(self.robot1, self.robot2), (self.robot2, self.robot1)]:
                print(f'\n1. Attack     2. Regen HP     3. Giveup')
                choice = int(input(f'{robot.name}, pilih aksi: '))

                if choice == 1:
                    robot.attack_enemy(enemy)
                elif choice == 2:
                    robot.regen_health()
                elif choice == 3:
                    print(f'{robot.name} menyerah!')
                    return

                if not enemy.is_alive():
                    print(f'{robot.name} menang!')
                    return

            self.round += 1


if __name__ == "__main__":
    robot1 = Robot("Atreus", 500, 10, 0.8)
    robot2 = Robot("Daedalus", 750, 8, 0.7)
    game = Game(robot1, robot2)
    game.play()
