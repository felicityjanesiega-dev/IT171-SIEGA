
player_jay = 0
player_fel = 0

treasure_x = 1
treasure_y = 3  
game_running = True

print("Welcome to Siegas's Maze")

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    move = input("Enter move: W to move up/ S to move down/ A to move left/ D to move right or Q to quit): ").upper()

    if move == 'W':
        player_fel += 1  
    elif move == 'S':
        player_fel -= 1  
    elif move == 'A':
        player_jay -= 1  
    elif move == 'D':
        player_jay += 1  
    elif move == 'Q':
        print("Not now but another time")
        break
    else:
        print("Invalid move!")

    print(f"Player position: ({player_jay}, {player_fel})")

    if player_jay == treasure_x and player_fel == treasure_y:
        print("Yeheyyy!")
        game_running = False


