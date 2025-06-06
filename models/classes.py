class Promedio:
    def __int__(self, name , lastname, carrier, year):
        self.name = name
        self.lastname = lastname
        self.carrier = carrier
        self.year = year
        self.promedio = 0.0
                
        def __str__(self):
            return f"Nombre:{self.name} \nLastname:{self.lastname} \nCarrier:{self.carrier} \nYear:{self.year} \nPromedio:{self.promedio}"