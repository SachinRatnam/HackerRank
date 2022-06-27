def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    no_game = 0
    while s >= p :
        no_game += 1
        s = s - p
        if ( (p > m) and ((p-d) > m) ):
            p = p - d
        else:
            p = m
    return no_game
