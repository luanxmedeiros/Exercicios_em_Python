#coding: utf-8
import os
while True:
    #Limpar no linux
    #os.system("clear")
    metros = float(input("Digite o valor em metros: "))
	#Limpar no windows
    os.system("cls")
    resultado = metros*1000
    print ("O valor de "+str(metros)+" em milimetros é: " + str(resultado))

os.system("pause")
