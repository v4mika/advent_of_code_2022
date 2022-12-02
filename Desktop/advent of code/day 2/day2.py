player_1_converter = ord('A') - 1
player_2_converter = ord('X') - 1

win = 6
draw = 3
lose = 0

rock = 1
paper = 2
scissors = 3

def play_round(player_1, player_2):
    play_1 = ord(player_1) - player_1_converter
    play_2 = ord(player_2) - player_2_converter
    
    def calculate_score():
        if play_1 == play_2:
            return draw
    
        if ((play_2 == rock and play_1 == scissors) 
            or (play_2 == paper and play_1 == rock) 
            or (play_2 == scissors and play_1 == paper)):
            return win
    
        return lose
    
    return play_2 + calculate_score()

total_score = 0

with open("input.txt", "r") as plays:
    for play in plays:
        if play.strip():
            play_list = play.split()
            score = play_round(play_list[0], play_list[1])
            total_score += score
plays.close()
print(total_score)
        