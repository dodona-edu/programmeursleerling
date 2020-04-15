things = {'Socrates', 'Plato', 'Eratosthenes', 'Zeus', 'Hera', 'Athens', 'Acropolis', 'Cat', 'Dog'}
men = {'Socrates', 'Plato', 'Eratosthenes'}
mortals = {'Socrates', 'Plato', 'Eratosthenes', 'Cat', 'Dog'}

A = men.issubset(mortals)
B = 'Socrates' in men
C = 'Socrates' in mortals
D = bool(mortals.difference(men))
E = bool(things.difference(mortals))
