def calcular_media(nota1, nota2):
  media = (nota1 + nota2) / 2
  return media
def verificar_aprovacao(media):
  if media >= 7:
    return "Aprovado"
  elif media >= 5:
    return "Recuperação"
  else:
    return "Reprovado"
if __name__ == '__main__':
  #name ´r uam variavel especial que pode determiinar o contexto em que um modulo py esta sendo executado.
  media = calcular_media(
    int(input("Informe a primeira nota: ")),
    int(input("Informe a segunda nota: ")),
  )
  print(f"A média final é {media}. Estudante {verificar_aprovacao(media)}")