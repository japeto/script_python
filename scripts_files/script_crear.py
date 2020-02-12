# ===================================
# Este script permite crea un archivo
# en formato CSV, con (;)
# ===================================

def crear_archivo(archivo="", lineas=[]):
	"""
	params
		archivo - ubicacion del archivo
		lineas - contenido del archivo
	return
		void
	"""
	my_archivo = open(archivo, "w+")
	for linea in lineas:
		my_archivo.write(linea)
	my_archivo.close()
	
	
def crear_archivov2(archivo="", lineas=[]):
	"""
	params
		archivo - ubicacion del archivo
		lineas - contenido del archivo
	return
		void
	"""
	my_archivo = open(archivo, "w+")
	for linea in lineas:
		my_archivo.write(linea)
	my_archivo.close()

if __name__ == "__main__":
	lineas = [
		"NOMBRE;APELLIDO;CORREO_ELECTROONICO \n",
		"Felipe;perez;soyfelipe@hotmail.com"
	]
	crear_archivo("miagenda.csv", lineas)
	
	

