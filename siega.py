# felicity_siega.py

# Personalized coordinates based on bonus points
# Felicity Jane: "Grok" -> player_x = len("Grok") = 4
# Siega: "xAI" -> last letter 'I' -> position in alphabet (A=1, B=2, ..., I=9) = 9 -> treasure_x = 9
player_x = 0
player_y = 0
treasure_x = 1
treasure_y = 3  # Assuming 's' was a typo for a number, set to 3 for up direction
game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    move = input("Enter move (w/a/s/d or q to quit): ")

    if move == 'w':
        player_y += 1  # up
    elif move == 's':
        player_y -= 1  # down
    elif move == 'a':
        player_x -= 1  # left 
    elif move == 'd':
        player_x += 1  # right
    elif move == 'q':
        game_running = False
    else:
        print("Invalid move. Use w (up), a (left), s (down), d (right), or q (quit).")
        continue

    print(f"Player position: ({player_x}, {player_y})")

    if player_x == treasure_x and player_y == treasure_y:
        print("Win!")
        game_running = False

