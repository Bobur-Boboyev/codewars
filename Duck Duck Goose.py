def duck_duck_goose(players, goose):
    a = len(players)
    return players[goose%a-1].name
