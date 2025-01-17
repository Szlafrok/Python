def sito(n:int) -> list:
    if n < 2:
        return[] # Przypadek szczególny OK

    is_num_prime = [True] * (n + 1)
    is_num_prime[0] = is_num_prime[1] = False # 0i 1 nie są liczbami pierwszymi

    for i in range(2, int(n**0.5) + 1 ): # Sprytna optymalizacja ;)
        if is_num_prime[i]: ############################################### tu było [1] zamiast [i] - błąd nieuwagi :P
            for multiple in range(i * i, n + 1, i):
                is_num_prime[multiple] = False
    
    return [i for i in range(n + 1) if is_num_prime[i]] # Sprytnie!

# Przykład użycia:
wynik = sito(500)
print(f"Zadanie dodatkowe 2: Wynik = {wynik}")

# (+1.75 / 2.00)


#__________________________3)_______________  o_O
is_palindrome = lambda s: s == s[::-1] # Elegancko ;)
# przykład uZycia
print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
