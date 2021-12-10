#Autor : Joao alves

import RPi.GPIO as GPIO
from time import sleep
from socket import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

meuHost = ''
minhaPort = 5000
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPort))
sockobj.listen(5)
def concts():
   
    while True:
        conexão, endereço = sockobj.accept()
        print('Server conectado por', endereço)
    
        while True:
            data = conexão.recv(1024)
            if not data : break
            palavras = data.decode()
            if palavras == 'on':
                 GPIO.output(5,1)
            elif palavras == 'off':
                 GPIO.output(5,0)
            elif palavras == 'BCM2s':
                GPIO.output(2,1)
            elif palavras == 'BCM2n':
                GPIO.output(2,0)
            elif palavras == 'BCM3s':
                GPIO.output(3,1)
            elif palavras == 'BCM3n':
                GPIO.output(3,0)
            elif palavras == 'BCM4s':
                GPIO.output(4,1)
            elif palavras == 'BCM4n':
                GPIO.output(4,0)
            elif palavras == 'BCM10s':
                GPIO.output(10,1)
            elif palavras == 'BCM10n':
                GPIO.output(10,0)
            elif palavras == 'BCM6s':
                GPIO.output(6,1)
            elif palavras == 'BCM6n':
                GPIO.output(6,0)
            elif palavras == 'BCM7s':
                GPIO.output(7,1)
            elif palavras == 'BCM7n':
                GPIO.output(7,0)
            elif palavras == 'BCM8s':
                GPIO.output(8,1)
            elif palavras == 'BCM8n':
                GPIO.output(8,0)
            elif palavras == 'BCM9s':
                GPIO.output(9,1)
            elif palavras == 'BCM9n':
                GPIO.output(9,0)
            elif palavras == 'BCM11s':
                GPIO.output(11,1)
            elif palavras == 'BCM11n':
                GPIO.output(11,0)
            elif palavras == 'BCM12s':
                GPIO.output(12,1)
            elif palavras == 'BCM12n':
                GPIO.output(12,0)
            elif palavras == 'BCM13s':
                GPIO.output(13,1)
            elif palavras == 'BCM13n':
                GPIO.output(13,0)
            elif palavras == 'BCM14s':
                GPIO.output(14,1)
            elif palavras == 'BCM14n':
                GPIO.output(14,0)
            elif palavras == 'BCM15s':
                GPIO.output(15,1)
            elif palavras == 'BCM15n':
                GPIO.output(15,0)
            elif palavras == 'BCM16s':
                GPIO.output(16,1)
            elif palavras == 'BCM16n':
                GPIO.output(16,0)
            elif palavras == 'BCM17s':
                GPIO.output(17,1)
            elif palavras == 'BCM17n':
                GPIO.output(17,0)
            elif palavras == 'BCM18s':
                GPIO.output(18,1)
            elif palavras == 'BCM18n':
                GPIO.output(18,0)
            elif palavras == 'BCM19s':
                GPIO.output(19,1)
            elif palavras == 'BCM19n':
                GPIO.output(19,0)
            elif palavras == 'BCM20s':
                GPIO.output(20,1)
            elif palavras == 'BCM20n':
                GPIO.output(20,0)
            elif palavras == 'BCM21s':
                GPIO.output(21,1)
            elif palavras == 'BCM21n':
                GPIO.output(21,0)
            elif palavras == 'BCM22s':
                GPIO.output(22,1)
            elif palavras == 'BCM22n':
                GPIO.output(22,0)
            elif palavras == 'BCM23s':
                GPIO.output(23,1)
            elif palavras == 'BCM23n':
                GPIO.output(23,0)
            elif palavras == 'BCM24s':
                GPIO.output(24,1)
            elif palavras == 'BCM24n':
                GPIO.output(24,0)
            elif palavras == 'BCM25s':
                GPIO.output(25,1)
            elif palavras == 'BCM25n':
                GPIO.output(25,0)
            elif palavras == 'BCM26s':
                GPIO.output(26,1)
            elif palavras == 'BCM26n':
                GPIO.output(26,0)
            elif palavras == 'BCM27s':
                GPIO.output(27,1)
            elif palavras == 'BCM27n':
                GPIO.output(27,0)
            
            
            
             
                
        
                
        
            

        conexão.close()
try:
    concts()
except:
    print('ERRO AO TENTAR SE CONECTAR!!! \n VERIFIQUE SE ESTA CONECTADO A UMA REDE (WIFI)')
#Autor : Joao alves
