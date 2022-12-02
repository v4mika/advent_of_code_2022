opponent_converter = ord('A') - 1

win = 'Z'
draw = 'Y'
lose = 'X' 

rock = 1
paper = 2
scissors = 3

def play_round(opponent, outcome):
    op = ord(opponent) - opponent_converter
    
    win_score = 6
    draw_score = 3
    lose_score = 0
        
    if outcome == draw:
        return op + draw_score
        
    if outcome == win:
        if op == rock: return paper + win_score
        if op == paper: return scissors + win_score
        if op == scissors: return rock + win_score
        
    if outcome == lose:
        if op == rock: return scissors + lose_score
        if op == paper: return rock + lose_score
        if op == scissors: return paper + lose_score

total_score = 0
with open("input.txt", "r") as plays:
    for play in plays:
        if play.strip():
            play_list = play.split()
            score = play_round(play_list[0], play_list[1])
            total_score += score
plays.close()
print(total_score)
        