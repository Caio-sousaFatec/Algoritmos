def f2(n = int):
    if n == 0:
        return (1);
    if n == 1:
        return (1);
    else:
        return(f2(n-1)+ 2 * f2(n-2));

resultado = f2(5)
print(resultado)
#Considere as entradas:
#i. f2(0);
#ii. f2(1);
#iii. f2(5);