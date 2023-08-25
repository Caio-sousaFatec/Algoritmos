#Mostre, através de teste de mesa, o resultado das seguintes funções:
def f1(n = int):
    if (n == 0):
        return (1);
    else:
        return(n * f1(n-1));


resultado = f1(5)
print(resultado)



#Considere as entradas:
#i. f1(0);
##ii. f1(1);
##iii. f1(5)
#
#i. f1(0) 
#
#1- é determinado que n = 0
#2- é realizado uma comparação, caso n seja 0 retorna 1
#3- é retornado 1
#
#i.f1(1)
#
#1- É determinado que n = 0
#2- É realizado uma comparação, caso n seja 0 retorna 1
#3- É dada a função (n* f1(n-1))
#em função
#	1 * f1(0)
#	1*0 = 0
#i. f1(5)
#1- É determinado que n = 0
#2- É realizado uma comparação, caso n seja 0 retorna 1
#3- É dada a função (n* f1(n-1))
#em função
#	5*f1(n-1)
#	5*f1(4*f1(n-1))
#	5*f1(4*f1(3*f1(n-1)))
#	5*f1(4*f1(3*f1(2*f1(n-1))))
#	5*f1(4*f1(3*f1(2*f1(1*f1(n-1)))))
#	5*f1(4*f1(3*f1(2*f1(1*f1(1)))))
#	120<5*24<4*6<3*2<2*1<1*1	
