import math
ang = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('O seno de {} é {:.2f};\n O cosseno de {} é {:.2f};\n E a Tangente de {} é {:.2f}.'.format(ang,s,ang,c,ang,t))

