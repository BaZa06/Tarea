#Data Access Object
""" Agregar prodcutos """
class PromedioDao:
    def _int_(self):
        self.promedio = []
        
    def add(self, promedio):
        self.promedio.append(promedio)
        
    def show(self):
        for promedio in self.promedio:
            print(promedio)
            
            