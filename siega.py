
player_jay = 0
player_fel = 0

treasure_x = 1
treasure_y = 3  
game_running = True

print("Welcome to Siegas's Maze")

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    move = input("Enter move (w/a/s/d or q to quit): ")

    if move == 'up':
        player_fel += 1  
    elif move == 'down':
        player_fel -= 1  
    elif move == 'left':
        player_jay -= 1  
    elif move == 'right':
        player_jay += 1  
    elif move == 'q':
        print("Not now but another time")
        break
    else:
        print("Invalid move!")

    print(f"Player position: ({player_jay}, {player_fel})")

    if player_x == treasure_x and player_y == treasure_y:
        print("Yeheyyy!")
        game_running = False


