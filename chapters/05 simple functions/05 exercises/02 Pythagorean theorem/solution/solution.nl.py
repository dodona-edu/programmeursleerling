# lengte van rechthoekszijden inlezen
zijde1 = float(input())
zijde2 = float(input())

# lengte van schuine zijde berkenen
schuine_zijde = (zijde1 ** 2 + zijde2 ** 2) ** 0.5

# lengte van schuine zijde uitschrijven
print(f'Lengte van de schuine zijde: {schuine_zijde:.3f}')
