resultat = int(input('Ange ditt resultat: '))
if resultat >= 48 and resultat <= 50:
  print('Ditt betyg är: A')
elif resultat >= 40 and resultat < 48:
  print('Ditt betyg är: B')
elif resultat >= 32 and resultat < 40:
  print('Ditt betyg är C')
elif resultat >= 24 and resultat < 32:
  print('Ditt betyg är: D')
elif resultat >= 16 and resultat < 24:
  print('Ditt betyg är: E')
elif resultat >= 0 and resultat <= 15:
  print('Ditt betyg är F')
else:
  print('Inga negativa värden eller värden över 50')
