import math

def teta_zenital(comprimento,altura):
	""" comprimento e altura da sombra em metros """
	teta_zenital = math.atan(comprimento/altura)
	print('o ângulo zenital do Sol ao meio-dia é', round(teta_zenital,2), 'radianos ou', round(math.degrees(teta_zenital),2), 'graus')

teta_zenital(0.5,5)
