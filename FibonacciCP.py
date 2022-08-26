def fibonacci(num):
    arreglo = [0,1]
    if num==1:
        print('0')
    elif num==2:
        print('[0,','1]')
    else:
        while(len(arreglo)<num):
            arreglo.append(0)
        if(num==0 or num==1):
            return 1
        else:
            arreglo[0]=0
            arreglo[1]=1
            for i in range(2,num):
                arreglo[i]=arreglo[i-1]+arreglo[i-2]
            print(arreglo)

fibonacci(50)
