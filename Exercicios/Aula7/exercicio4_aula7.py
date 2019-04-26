import time

x1 = time.time() #segundos desde meia-noite de 01/01/1970
x2 = x1/(365.25*24*3600) #anos desde 1970

x3 = 1970 + int(x2) #ano atual
x4 = x2 - int(x2) #fração do ano atual
x5 = x4*365 #número de dias desde o início do ano

x6 = x5 - int(x5) #fracao já passada do dia de hoje
x7 = int(x5) + 1 #dia de hoje

# Para o ano ser bissexto:
if (x3 % 4) == 0 and (x3 % 100) != 0 or (x3 % 400) == 0:
    
    if x7 <= 31:
        print('data:', x7, 'de janeiro de', x3)
        
    if 32 <= x7 <= 60:
        print('data:', x7 - 31, 'de fevereiro de', x3)
        
    if 61 <= x7 <= 91:
        print('data:', x7 - 60, 'de março de', x3)
        
    if 92 <= x7 <= 121:
        print('data:', x7 - 91, 'de abril de', x3)
        
    if 122 <= x7 <= 152:
        print('data:', x7 - 121, 'de maio de', x3)
        
    if 153 <= x7 <= 182:
        print('data:', x7 - 152, 'de junho de', x3)
        
    if 183 <= x7 <= 213:
        print('data:', x7 - 182, 'de julho de', x3)

    if 214 <= x7 <= 244:
        print('data:',x7 - 213, 'de agosto de', x3)
        
    if 245 <= x7 <= 274:
        print('data:', x7 - 244, 'de setembro de', x3)
        
    if 275 <= x7 <= 305:
        print('data:', x7 - 274, 'de outubro de', x3)
        
    if 306 <= x7 <= 335:
        print('data:', x7 - 305, 'de novembro de', x3)
        
    if 336 <= x7 <= 366:
        print('data:', x7 - 335, 'de dezembro de', x3)

# E para não ser:
else:
        
    if x7 <= 31:
        print('data:', x7, 'de janeiro de', x3)
        
    if 32 <= x7 <= 59:
        print('data:', x7 - 31, 'de fevereiro de', x3)
        
    if 60 <= x7 <= 90:
        print('data:', x7 - 59, 'de março de', x3)
        
    if 91 <= x7 <= 120:
        print('data:', x7 - 90, 'de abril de', x3)
        
    if 121 <= x7 <= 151:
        print('data:', x7 - 120, 'de maio de', x3)
        
    if 152 <= x7 <= 181:
        print('data:', x7 - 151, 'de junho de', x3)
        
    if 182 <= x7 <= 212:
        print('data:', x7 - 181, 'de julho de', x3)

    if 213 <= x7 <= 243:
        print('data:', x7 - 212, 'de agosto de', x3)
        
    if 244 <= x7 <= 273:
        print('data:', x7 - 243, 'de setembro de', x3)
        
    if 274 <= x7 <= 304:
        print('data:', x7 - 273, 'de outubro de', x3)
        
    if 305 <= x7 <= 334:
        print('data:', x7 - 304, 'de novembro de', x3)
        
    if 335 <= x7 <= 365:
        print('data:', x7 - 334, 'de dezembro de', x3)

x8 = x6*24 #horas passadas hoje

x9 = x8 - int(x8) #fração da hora em andamento
x10 = x9*60 #minutos passados da hora int(x7)

x11 = x10 - int(x10) #fração do minuto em andamento
x12 = x11*60 #segundos passados do minuto int(x9)

print('hora:', int(x8), 'horas,', int(x10), 'minutos e', int(x12), 'segundos')
