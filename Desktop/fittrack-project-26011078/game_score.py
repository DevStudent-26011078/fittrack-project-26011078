# Input Collection
name = input("Enter player's name: ")

# Numeric Input Processing
games_played = int(input("Enter number of games played: "))

# Score Data Entry
total_score = int(input("Enter total score achieved: "))

# Computation
average_score = total_score / games_played

# Output Display
print(f"\nPlayer: {name}")
print(f"Games Played: {games_played}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")