'''
Intervalos númericos

Diferente das linguaguens da familia C
o PYTHON PERMITE A DEFINIÇAO DE INTERVALOS NUMERICOS EM NOTAÇAO MATEMATICA:

valor1< variavel < valor2

'''

#not(0<=n1<=10)or not(0<+n2<=10)or not(0<=n3<=10)

n1 = float(input('n1:'))
n2 = float(input('n2:'))
n3 = float(input('n3:'))
if (n1<0 or n1>10)or(n2<0 or n2>10)or(n3<0 or n3>10):    
    print('Notas erradas!!')
else:
    m = (n1+n2+n3)/3
    if 0<=m and m<3:
        print('reprovado')
    elif 3<=m and m<7:
        print('recuperaçao')
    else:
        print('aprovado')

