#Aluno: Lucas Gabriel Nunes Geremias 
#Turma: Bcc 
#Turno: Manhã  

#---------------------------------------------Ler o arquivo----------------------------------------------------------

arq = open("teste3.txt", "r")
ler = arq.readlines()

#-----------------------------------------Declaração de variaveis-----------------------------------------------------
vet = []
rpi = []
rpd = []
rpu = []
cont = 0
#--------------------------------------------Ler as linhas----------------------------------------------------------
for i in ler:
    tb = i.strip()    
    vet.append(tb)

tam = len(vet)
n = int(vet[0])
print("O numero de Operações é: ", n)
print("\n")
for p in range(tam):

    if(cont<n):
    #União

        if("U" in vet[p] and not "," in vet[p]):
            conjum = vet[p+1].split(', ')
            conjdois = vet[p+2].split(', ')

            for i in range(len(conjum)):
                rpu.append(conjum[i])

            for j in range(len(conjdois)):
                if(conjdois[j]not in rpu):
                    rpu.append(conjdois[j])

            cjum = ','.join(conjum)
            cjdois = ','.join(conjdois)
            respu = ','.join(rpu)
            print("União: conjunto 1 {%s}, conjunto 2 {%s}. Resultado: {%s}" %(cjum,cjdois,respu))
            print("\n")
            cont+=1
            rpu = []

    #Interseção

        elif("I" in vet[p] and not "," in vet[p]):

            conj1 = vet[p+1].split(', ')
            conj2 = vet[p+2].split(', ')

            for i in range(len(conj1)):
                for j in range(len(conj2)):
                    if((conj1[i]==conj2[j]) and not conj1[i] in rpi):
                        rpi.append(conj1[i])

            cj1 = ','.join(conj1)
            cj2 = ','.join(conj2)
            respi = ','.join(rpi)
                            
            print("Interseção: conjunto 1 {%s}, conjunto 2 {%s}. Resultado: {%s}" %(cj1,cj2,respi))
            print("\n")
            cont+=1
            rpi = []

    #Diferença

        elif("D" in vet[p] and not "," in vet[p]):

            conja = vet[p+1].split(', ')
            conjb = vet[p+2].split(', ')

            for i in range(len(conja)):
                if(conja[i] not in conjb):
                    rpd.append(conja[i])         
            
            cja = ','.join(conja)
            cjb = ','.join(conjb)
            respd = ','.join(rpd)
            print("Diferença: conjunto 1 {%s}, conjunto 2 {%s}. Resultado: {%s}" %(cja,cjb,respd)) 
            print("\n")    
            cont+=1
            rpd = []

    #Produto cartesiano

        elif("C" in vet[p] and not "," in vet[p]):
            conjone = vet[p+1].split(', ')
            conjtwo = vet[p+2].split(', ')

            cjone = ','.join(conjone)
            cjtwo = ','.join(conjtwo)

            print("Produto Cartesiano: conjunto 1 {%s}, conjunto 2 {%s}. Resultado:" %(cjone,cjtwo), end="") 

            for i in range(len(conjone)):
                for j in range(len(conjtwo)):
                    print("{", conjone[i], ",", conjtwo[j], "}, ", end="")
                print("\n")
            cont+=1
 
