def max_ciag(L):

    n = len(L) # długość ciągu

    dl_ciagu = 1 # aktualna długość podciągu rosnącego
    res = 1 # najdłuższy dotychczasowy podciąg rosnący
    
    for i in range(1, n):
        if L[i] > L[i-1]: # liczba jest wieksza od poprzedniej
            dl_ciagu += 1
            res = max(dl_ciagu, res) # 
        else:
            dl_ciagu = 1 # koniec poprzedniego podciagu moze byc poczatkiem nowego

    return res

print(max_ciag([2, 4, 3, 4, 5, 1]))