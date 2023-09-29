'''Escreva um algoritmo para ler a hora de
início e a hora de fim de um jogo de Xadrez
(considere apenas horas inteiras, sem os
minutos) e calcule a duração do jogo em
horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo
pode iniciar em um dia e terminar no dia
seguinte'''

inicio = int(input("Que horas começará o jogo? (Apenas hora) "))
fim = int(input("Que horas o jogo termina? (Apenas hora) "))

if fim >= inicio:
  duracao = fim - inicio
  print("Duração do jogo foi de ",duracao," horas")
else:
  duração = 24 - inicio + fim
  print("Duração do jogo foi invalida, pois ",duracao," horas, excedem 24hrs.")



