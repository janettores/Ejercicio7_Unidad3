class Personal:
    __cuil: str
    __apellido: str
    __nombre: str
    __sueldobasico: float
    __antiguedad: int

    def __init__(self, cuil='', apellido='', nombre='', sueldobasico=0, antiguedad=0):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldobasico = sueldobasico
        self.__antiguedad = antiguedad

    def getCuil(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldoBasico(self):
        return self.__sueldobasico

    def getAntiguedad(self):
        return self.__antiguedad

    def __str__(self):
        return self.__nombre + " " + self.__apellido + " CUIL: " + self.__cuil + " Sueldo: $" + str(
            self.__sueldobasico) + " antiguedad: " + str(self.__antiguedad)

    def __lt__(self, otro):
        return (self.getNombre(), self.getApellido()) < (otro.getNombre(), otro.getApellido())