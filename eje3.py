import multiprocessing

def saludar(nombre):
    print("hola, "+nombre)

if __name__ == "__main__":
    nombre="Usuario"
    proceso=multiprocessing.Process(target=saludar, args=(nombre,))
    proceso.start()
    proceso.join()