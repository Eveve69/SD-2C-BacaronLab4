def find_max_min(S):
    def lwr_bnd(S, n):
        if n == 0:
            return S[n]
        else:
            return min(S[n], lwr_bnd(S, n-1))
        
        def uppr_bnd(S, n):
            if n == 0:
                return S[n]
            else:
                return max(S[n], uppr_bnd(S, n-1))
            print(lwr_bnd(S, len(S)-1), uppr_bnd(S, len(S)-1))