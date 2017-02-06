
#EP3 - Identificando Imagens Binárias
#Aline Dominique e Jhonisson Gabriel
#3º semestre A
# Analise e Desenvolvimento de Sistemas
# EP3 - 02 / 11 / 2016

# Variáveis 
txt='''
010
111
000
010
'''

txt2='''
10101
10101
11111
'''

txt3='''
0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110
'''
txt4='''
0011001010001100
0110001010001100
0000000000001000
0010011111111110
0010001110001000
0110001010001100
0000000000001000
0010011111111110
0010001110001000
'''
lista = txt3.split()
matriz = []


# criando matriz com as Strings
for i in range(0,len(lista)):
    linha = lista[i]
    coluna = []
    for j in range(0,len(linha)):
        coluna += linha[j]   
    matriz.append(coluna)
    
# Variáveis para percorrer Matriz
ums=[]
zeros=[]
c=0
q=0
vizinhos=[]

print("++++Entrada++++")
for l in matriz:
    print (l)

for m in range (0,len(matriz)):
    line = matriz[m]
    colune = []
    for n in range(0,len(line)):
        if line[n] == '1':
            q+=1
            ums.append(list([q,m,n]))
            ##vizinhos da posição primeira linha, primeira coluna
            if m == 0 and n == 0:
                c+=1
                vizinhos.append(list([c,'0','0','0',matriz[m][n+1],matriz[m+1][n+1],matriz[m+1][n],'0','0']))          
                                    # i  se  s  sd  d               id              in              ie   e
            ##vizinhos da posição ultima linha, primeira coluna
            elif m == len(matriz)-1 and n == 0:
                c+=1
                vizinhos.append(list([c,'0',matriz[m-1][n],matriz[m-1][n+1],matriz[m][n+1],'0','0','0','0']))
            ##vizinhos da posição ultima linha, ultima coluna
            elif m == len(matriz)-1 and n == len(line)-1:
                c+=1
                vizinhos.append(list([c,matriz[m-1][n-1],matriz[m-1][n],'0','0','0','0','0',matriz[m][n-1]]))
            ##vizinhos da posição primeira linha, ultima coluna
            elif m == 0 and n == len(line)-1:
                c+=1
                vizinhos.append(list([c,'0','0','0','0','0',matriz[m+1][n],matriz[m+1][n-1],matriz[m][n-1]]))
            ##vizinhos da primeira coluna, exceto extremos    
            elif (m>0 and m<len(matriz)) and n==0:
                c+=1
                vizinhos.append(list([c,'0',matriz[m-1][n],matriz[m-1][n+1],matriz[m][n+1],matriz[m+1][n+1],matriz[m+1][n],'0','0']))
            ##vizinhos da ultima coluna, exceto extremos    
            elif (m>0 and m<len(matriz) and n==len(line)-1):
                c+=1
                vizinhos.append(list([c,matriz[m-1][n-1],matriz[m-1][n],'0','0','0',matriz[m+1][n],matriz[m+1][n-1],matriz[m][n-1]]))
            ##vizinhos da primeira linha, exceto extremos    
            elif m==0 and (n>0 and n<len(line)):
                c+=1
                vizinhos.append(list([c,'0','0','0',matriz[m][n+1],matriz[m+1][n+1],matriz[m+1][n],matriz[m+1][n-1],matriz[m][n-1]]))
            ##vizinhos da ultima linha, exceto extremos    
            elif m==len(matriz)-1 and (n>0 and n<len(line)):
                c+=1
                vizinhos.append(list([c,matriz[m-1][n-1],matriz[m-1][n],matriz[m-1][n+1],matriz[m][n+1],'0','0','0',matriz[m][n-1]]))
            else: 
                c+=1
                vizinhos.append(list([c,matriz[m-1][n-1],matriz[m-1][n],matriz[m-1][n+1],matriz[m][n+1],matriz[m+1][n+1],matriz[m+1][n],matriz[m+1][n-1],matriz[m][n-1]]))
                

    #Variável local
    num=0

    # Verificando posições e rotulando a Matriz
    for u in range(0,len(ums)):
        lis = ums[u]
        lisvz = vizinhos[u]
        tam = len(lis)
 
        for t in range(0,tam):
            if lis[t] == lisvz[t]:              
                if lisvz[8] == '0' and lisvz[2] == '0':
                    num+=1
                    matriz [lis[1]] [lis[2]]= str(num)
                
                     
            if (lisvz[8] == '0' and lisvz[2] != '0'):
                matriz [lis[1]] [lis[2]]= matriz [lis[1]-1] [lis[2]]
            
            if (lisvz[8] != '0' and lisvz[2] == '0'):
                matriz [lis[1]] [lis[2]]= matriz [lis[1]] [lis[2]-1]
                    
                
            if matriz [lis[1]] [lis[2]-1]!= '0' and matriz [lis[1]-1] [lis[2]]!='0':
                if matriz [lis[1]] [lis[2]-1]< matriz [lis[1]-1] [lis[2]]:                   
                    matriz [lis[1]] [lis[2]] = matriz[lis[1]][lis[2]-1]
                    matriz [lis[1]-1] [lis[2]] = matriz[lis[1]][lis[2]-1]
                else:
                    matriz [lis[1]] [lis[2]] = matriz[lis[1]-1][lis[2]]
                    matriz [lis[1]] [lis[2]-1] = matriz[lis[1]-1][lis[2]]

print("\n")
print("++++Saída++++")
for f in matriz:
    print(f)










 
