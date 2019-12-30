scores = [100, 90, 90, 80, 75 ,60]
alice = [50, 65, 77, 90, 102]
def climbingLeaderboard(scores, alice):
    res = []
    scores = list(set(scores))
    scores.sort(reverse = True)
    curr_rank  = len(scores) + 1
    for a in alice:
        print('a = ', a,' ', end=' ')
        if curr_rank ==1:
            res.append(1)
        else:
            for i in range(curr_rank-2,-1,-1):
                print(i)
                if scores[i]<a:
                    if i == 0:
                       curr_rank =1
                    else:
                        continue
                if scores[i] == a:
                    curr_rank = i+1
                elif scores[i] > a:
                    curr_rank = i+2
                res.append(curr_rank)
                break
    return res
print(climbingLeaderboard(scores, alice))