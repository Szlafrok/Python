def seq(T):
    n = len(T)
    for i in range(n-2):
        skalar = T[i+1] / T[i]
        cond = 1
        k = i+1
        j = i+2
        while j < n:
            if T[j] / T[k] == skalar:
                cond += 1
                k += 1
                
            else:
                break


T = [2,5,7,3,2,3,5,7,6,9,15,21,17,29,23]