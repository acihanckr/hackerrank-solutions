def minion_game(string):
    #start
    score_vow = 0
    score_cons = 0
    for i in range(len(string)):
        if string[i] in ['A', 'E', 'O', 'I', 'U']:
            score_vow += len(string) - i
        else:
            score_cons += len(string) - i
    if score_cons == score_vow:
        print('Draw')
        return 0
    else:
        score = max(score_cons, score_vow)
        if score_vow<score_cons:
            winner = 'Stuart'
        else:
            winner = 'Kevin'
        print(winner+ ' ' + str(score))
    #end
if __name__ == '__main__':
    s = input()
    minion_game(s)