from unittest import TestCase
import negocio.juego as negocio

# Ale
# estan vendo eso?
# Esto acáááá Quando tipeo acá vees ahsiiiiiiiiiiiiiiiiiiiiii ;) í@

class testsDelJuego(TestCase):

    def test_jugando_valor_elegido_4_valor_correcto_4_resultado_esperado_Ok(self):
        # Arrange
        valor_elegido = 4
        valor_correcto = 4
        resultado_esperado = "Ok"

        # Act        
        resultado = negocio.jugar(valor_correcto,valor_elegido)

        # Assert
        self.assertEqual(resultado_esperado, resultado)

    def test_jugando_valor_elegido_5_valor_esperado_4_resultado_esperado_incorrecto(self):
        # Arrange
        valor_elegido = 5   
        valor_correcto = 4
        resultado_esperado = "Incorrecto"

        # Act        
        resultado = negocio.jugar(valor_correcto,valor_elegido)

        # Assert
        self.assertEqual(resultado_esperado, resultado)
        
