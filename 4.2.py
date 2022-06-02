def rec_unique_set(S):
    if len(S) == 1:
        return True
    else:
        cand = S.pop()
        for elem in S:
            if cand == elem:
                return False
            return rec_unique_set(S)