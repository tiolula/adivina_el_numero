import random
import pickle

def jugar(a, b):
   if a == b:
      return "Ok"
   else: 
      return 'Incorrecto'

def eligir_numero_secreto():
   numero_secreto = random.randint(0,9)
   guardar_numero_secreto(numero_secreto)

def guardar_numero_secreto(numero_secreto):
   pickle.dump(numero_secreto, open( "secret_number.txt", "wb") )

def cargar_numero_secreto():
   return pickle.load(open( "secret_number.txt", "rb") )

def intentar_adivinar(conjectura):
   numero_secreto = cargar_numero_secreto()
   return jugar(numero_secreto, int(conjectura))