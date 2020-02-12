# ===================================
# ===================================
from script_crear import crear_archivo
import script_leer as lector
from script_add import agregar_contenido

numbre_archivo= "otragenda.csv"
lineas =[
	"NOMBRE;APELLIDO;CORREO_ELECTROONICO \n",
]
crear_archivo(numbre_archivo, lineas)
lineas2=[
	"Marcela;diaz;diasmm@hotmail.com\n",
	"Daniel;pena;ddnnpena@hotmail.com\n",
]
agregar_contenido(numbre_archivo, lineas2)
lineas= lector.leer_archivo(numbre_archivo)
print(f"{lineas}")
