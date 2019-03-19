# EXERCÍCIO 4

import math

# A altura do poste e a sombra que ela projeta ao meio-dia (em metros) são, respectivamente:
h = 5
s = 0.5

# Logo o ângulo zenital teta_z do Sol neste horário é dado por tan(teta_z) = s/h.
# Como o Python originalmente fornece o ângulo em radianos, há de se fazer a conversão para graus.
# Para tal, basta multiplicar o resultado por (180/pi):
teta_z = math.atan(s/h)*(180/math.pi)
print('o ângulo zenital do Sol ao meio-dia é de:', teta_z, 'graus')
