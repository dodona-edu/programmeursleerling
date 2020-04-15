alles = {'Socrates', 'Plato', 'Eratosthenes', 'Zeus', 'Hera', 'Athene', 'Acropolis', 'Kat', 'Hond'}
mensen = {'Socrates', 'Plato', 'Eratosthenes'}
sterfelijken = {'Socrates', 'Plato', 'Eratosthenes', 'Kat', 'Hond'}

A = mensen.issubset(sterfelijken)
B = 'Socrates' in mensen
C = 'Socrates' in sterfelijken
D = bool(sterfelijken.difference(mensen))
E = bool(alles.difference(sterfelijken))
