def v_mru(ro,r,t):
	# ro e r em metros, t em segundos
	v_mru = (r-ro)/t
	print('velocidade média do objeto em MRU é', v_mru, 'm/s')

v_mru(0,10,2)

def v_mrua(vo,g,t):
	# vo em m/s, g em m/s**2, t em segundos
	v_mrua = vo + g*t
	print('velocidade final do objeto em MRUA é', v_mrua, 'm/s')

v_mrua(0,10,5)

