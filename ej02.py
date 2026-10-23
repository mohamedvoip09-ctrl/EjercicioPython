import multiprocessing
import time

def saludar():
    print("Hola mundo")


def despedir():
    print("Adios")

def tarea():
    saludar()
    time.sleep(1)
    despedir()


if __name__=="__main__":
    proceso= multiprocessing.Process(target=tarea)
    proceso.start()
    proceso.join()
    



