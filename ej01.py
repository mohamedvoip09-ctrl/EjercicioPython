import subprocess

def mensaje():
    proceso=subprocess.Popen(["echo", "hola desde un proceso"],stdout=subprocess.PIPE, text=True)
    salida=proceso.communicate()
    print(salida)

if __name__ == "__main__":
    mensaje()