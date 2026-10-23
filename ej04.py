import multiprocessing
import time

def repetir(mensaje, veces,pausa):
    n=0
    while(n<veces):
        print(mensaje)
        time.sleep(pausa)
        n=n+1

    

if __name__ == "__main__":
    proceso=multiprocessing.Process(target=repetir,args=("Estoy trabajando",3, 0.5))
    proceso.start()
    proceso.join()
