def calculate_league_points(wins, draws, losses):
    # Complete this function
    total_points = (wins * 4) + (draws * 2) - (losses * 1)
    return total_points


statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
# Call the calculate_league_points function
total_points = calculate_league_points(wins, draws, losses)
print(total_points)