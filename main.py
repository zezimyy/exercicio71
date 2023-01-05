saque = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0


saque = int(input("Digite o quanto quer sacar: "))

if saque >= 50:
  notas_50 = saque //  50
  saque = saque - (notas_50 * 50)
  print("{} notas de 50".format(notas_50))

  if saque >= 20 and saque < 50:
    notas_20 = saque // 20
    saque = saque - (notas_20 * 20)
    print("{} notas de 20".format(notas_20))

  if saque >=10 and saque < 20:
    notas_10 = saque // 10
    saque = saque - (notas_10 * 10)
    print("{} notas de 10".format(notas_10))

  if saque >= 1 and saque < 10:
    notas_1 = saque // 1
    saque = saque - (notas_1 * 1)
    print("{} notas de 1".format(notas_1))
