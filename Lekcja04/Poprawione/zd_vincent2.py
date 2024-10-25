p = 123
q = 456

# A)
a = (p < q or p > q) # OK

# B)
b = (p == q) # Logicznie nie otrzymamy tego samego

# C)
c = (p == q) # OK, tu był mój błąd w zadaniu XD

# D)
d = not (p < q) # OK

# E)
e = not (p <= q) # Weryfikujesz równość - w tej sytuacji jeżeli p = q, nie spełnisz warunku.

# 3/5 -> (++)

# Razem 5 plusów, czyli odznaka ;)