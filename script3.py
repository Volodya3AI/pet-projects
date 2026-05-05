import random
import time


class Country:
    def __init__(self, name):
        self.name = name
        self.stability = 70  # %
        self.political_power = 100
        self.money = 1000
        self.factories = 5
        self.divisions = 10
        self.war_support = 20  # %
        self.ideology = "Neutral"

    def status(self):
        print(f"\n--- {self.name} | {self.ideology} ---")
        print(f"💰 Гроші: {self.money} | 🏭 Заводи: {self.factories}")
        print(f"⚡ Політ. влада: {self.political_power} | ⚖️ Стабільність: {self.stability}%")
        print(f"🎖️ Дивізії: {self.divisions} | 🔥 Підтримка війни: {self.war_support}%")
        print("----------------------------")


def battle(player, enemy_divisions):
    print(f"\n⚔️ Почалася битва проти ворога ({enemy_divisions} дивізій)!")
    player_roll = random.randint(1, 6) + (player.divisions // 5)
    enemy_roll = random.randint(1, 6) + (enemy_divisions // 5)

    if player_roll > enemy_roll:
        loss = random.randint(1, 3)
        player.divisions -= loss
        print(f"✅ Перемога! Ми втратили {loss} дивізій, але ворог розбитий.")
        player.political_power += 20
    else:
        loss = random.randint(3, 6)
        player.divisions -= loss
        player.stability -= 10
        print(f"❌ Поразка! Втрачено {loss} дивізій. Стабільність впала.")


def main():
    player = Country("Україна")
    turn = 1

    while player.divisions > 0 and player.stability > 0:
        player.status()
        print(f"Хід №{turn}")
        print("1. Побудувати завод (-200💰, +1🏭)")
        print("2. Мобілізація (-100💰, -20⚡, +3🎖️)")
        print("3. Пропаганда (-50⚡, +10% 🔥)")
        print("4. Напасти на сусіда")
        print("5. Нічого не робити (+50💰, +10⚡)")

        choice = input("Ваше рішення: ")

        if choice == "1":
            if player.money >= 200:
                player.money -= 200
                player.factories += 1
                print("🏭 Завод побудовано!")
            else:
                print("Недостатньо грошей!")

        elif choice == "2":
            if player.money >= 100 and player.political_power >= 20:
                player.money -= 100
                player.political_power -= 20
                player.divisions += 3
                print("🎖️ Дивізії сформовані!")
            else:
                print("Бракує ресурсів для мобілізації.")

        elif choice == "3":
            if player.political_power >= 50:
                player.political_power -= 50
                player.war_support = min(100, player.war_support + 10)
                print("📢 Підтримка війни зросла!")
            else:
                print("Немає політичної волі.")

        elif choice == "4":
            if player.war_support < 30:
                print("🚫 Народ не хоче війни! (Треба >30% підтримки)")
            else:
                enemy_strength = random.randint(5, 15)
                battle(player, enemy_strength)

        # Економіка в кінці ходу
        player.money += player.factories * 20
        player.political_power += 5
        turn += 1
        time.sleep(1)

    print("\nГРА ЗАКІНЧЕНА. Ваша країна пала.")


if __name__ == "__main__":
    main()
