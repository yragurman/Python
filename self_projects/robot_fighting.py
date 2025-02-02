from random import randint

"""
function that return damage in range min and max input from user
Arguments:
damage_min - minimum damage that can return function
damage_max - maximum damage that can return function
"""
def hit(damage_min, damage_max):
    return randint(damage_min, damage_max)


robot_name = "Big Boss"
robot_damage_min = 100
robot_damage_max = 250
robot_critical_damage = 500
robot_health = 1000

player_name = input("Enter your name: ")
player_damage_min = 100
player_damage_max = 250
player_critical_damage = 500
player_health = 1000


# game function
def game():
    global robot_health
    global player_health
    while robot_health >= 1 and player_health >= 1:
        print("Make choice shield or hit")
        player_choice = input("Enter your choice here (s/h): ")
        if player_choice == "s":
            chance_of_shield = randint(0, 100)
            if chance_of_shield <= 50:
                player_health -= hit(robot_damage_min, robot_damage_max)
                print("Shield was damaged, player health remain: " + str(player_health))
            else:
                robot_health -= hit(0, 100)
                print("Shield wasn`t damaged, robot health remain:" + str(robot_health))
        if player_choice == "h":
            robot_health -= hit(player_damage_min, player_damage_max)
            player_health -= hit(robot_damage_min, robot_damage_max)
            print("Robot health remain: " + str(robot_health))
            print("Player health remain: " + str(player_health))

    if robot_health <= 0:
        print(f"{player_name} win")
    else:
        print(f"Robot {robot_name} win")


# start game
if __name__ == '__main__':
    game()
