def compare(team_a_points, team_b_points):
    # complete this function
    if team_a_points > team_b_points:
        return "Win"
    elif team_a_points == team_b_points:
        return "Draw"
    else:
        return "Lose"


team_a_points = int(input())
team_b_points = int(input())
compare_result = compare(
    team_a_points, team_b_points
)  # Call the compare function
print(compare_result)