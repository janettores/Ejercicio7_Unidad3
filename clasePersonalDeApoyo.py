from clasePersonal import Personal

class PersonalApoyo(Personal):
    __categoria: int

    def __init__(self, cuil='', apellido='', nombre='', sueldobasico=0, antiguedad=0, categoria=0):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__categoria = categoria

    def getCategoria(self):
        return self.__categoria

    def getSueldo(self):
        sueldotot = super().getSueldoBasico() + (super().getSueldoBasico() * (super().getAntiguedad() / 100))

        if self.__categoria >= 1 and self.__categoria <= 10:
            sueldotot += (super().getSueldoBasico() * (10 / 100))

        elif self.__categoria >= 11 and self.__categoria <= 20:
            sueldotot += (super().getSueldoBasico() * (20 / 100))

        elif self.__categoria >= 21 and self.__categoria <= 22:
            sueldotot += (super().getSueldoBasico() * (30 / 100))

        return sueldotot

    def __str__(self):
        return super().__str__() + "\nCategoria: " + str(self.__categoria)