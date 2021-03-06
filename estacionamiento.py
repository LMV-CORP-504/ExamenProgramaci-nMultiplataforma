# -*- coding: utf8 -*-
# Programa: Examen II Parcial // clase estacionamiento
# Autor: Akdiel Callejas Amador
# Fecha 13/03/20

from vehiculo import Vehiculo
import random
from datetime import datetime, timedelta

class Estacionamiento:
    """ 
    representa una lista de onjetos de clase vehículos, se encarga controlar
    el ingreso y salida de vehiculos al estacionamiento, tanto como el de generar
    el ticket para el cobro del estacinamiento.
    """

    def __init__(self):
        """ se encarga de inicializar un listado de objetos tipo vehiculo. """
        self.lista_estacionamiento = list()

    def ingreso_vehiculo(self):
        """ se encarga de reguistrar el ingreso de un vehículo al estacionamiento """
        placa_vehiculo = input("Ingrese la placa del vehículo: ")
        marca_vehiculo = input("Ingrese la marca del vehículo: ")
        modelo_vehiclo = input("Ingrese el modelo del vehículo: ")
        tipo_vehículo = input("Ingrese el tipo de vehículo(automóvil o bicicleta ): ")

        self.lista_estacionamiento.append(Vehiculo(placa_vehiculo,marca_vehiculo,modelo_vehiclo,tipo_vehículo))

        print("El vehículo fue ingresado Satisfactoriamente.")

    def calcular_tarifa(self, placa):
        """ Se encarga de calcular el la tarifa cuando el vehículo sale. """
        vehiculo = self.buscar_vehículo(placa)
        
        if vehiculo:
            hora_aleatoria = random.randint(1,3)
            self.horaSalida = datetime.now() + timedelta(hours=hora_aleatoria)

            if vehiculo.tipo_vehiculo == "automovil" or vehiculo.tipo_vehiculo == "automóvil":
                subtotal = 20
                total = (hora_aleatoria - 1) * 0.20 + subtotal
                return total
            elif vehiculo.tipo_vehiculo == "motocicleta":
                subtotal = 10
                total = (hora_aleatoria -1) * 0.10 + subtotal
            return total
        else:
            print("el vehículo no ha sido encontrado")


    def buscar_vehículo(self, placa):
        """ Busca entre los vehículos en el estacionamineto si existe una misma placa. """
        for vehiculo in self.lista_estacionamiento:
            if str(vehiculo.placa_vehiculo) == str(placa):
                return vehiculo
        else:
            print("No se ha encontrado el vehículo.")

    def salida_vehiculo(self):
        """ Reguistra la salida de un ehiculo y calcula el ticket """
        placa = input("Ingrese la placa del veículo: ")
        vehiculo = self.buscar_vehículo(placa)
        
        if vehiculo:
            vehiculo.estado_vehiculo = False
            print("el total a pagar es: {0}".format(self.calcular_tarifa(placa)))
        else:
            print("No se puede realizar el cobro.")
