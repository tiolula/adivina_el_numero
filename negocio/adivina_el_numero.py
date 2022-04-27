import random
import pickle

def juego(a, b):
   if a == b:
      return "Ok"
   else: 
      return 'Incorrecto'

def nuevo_juego():
   numero_secreto = random.randint(1, 9)
   pickle.dump(numero_secreto, open( "secret_number.txt", "wb") )

def jugar(conjectura):
   numero_secreto = pickle.load(open( "secret_number.txt", "rb") )
   return juego(numero_secreto, int(conjectura))
