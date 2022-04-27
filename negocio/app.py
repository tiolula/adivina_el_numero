from flask import Flask, escape, request

import negocio.adivina_el_numero as juego

app = Flask(__name__)

@app.route('/adivina_el_numero/<int:numero>')
def adivinar(numero):
    return juego.intentar_adivinar(numero)

@app.route('/adivina_el_numero/nuevo_juego')
def nuevo_juego():
    juego.eligir_numero_secreto()
    return 'Nuevo juego iniciado!'
