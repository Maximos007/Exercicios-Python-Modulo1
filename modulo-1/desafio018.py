from math import radians, sin, cos, tan

number = float(input('Ângulo : '))
print("Seno: {:.2f}".format(sin(radians(number))))
print('Cosseno : {:.2f}'.format(cos(radians(number))))
print('Tangente : {:.2f}'.format(tan(radians(number))))