import mod_func  as mf
if __name__ == '__main__':
    mf.mensagem()
    
    n1 = int(input('primeiro número: '))
    n2 = int(input('segundo número: '))
    soma = mf.soma(n1, n2)
    print(soma)
