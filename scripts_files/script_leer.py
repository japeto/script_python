# ===================================
# Este script permite leer un archivo
# en formato CSV, con (;)
# ===================================

def leer_archivo(archivo=""):
	"""
	params
		archivo - ubicacion del archivo
	return
		lista con lineas del archivo
	"""
	my_archivo = open(archivo, "r")
	lineas = my_archivo.readlines()
	my_archivo.close()
	return lineas

if __name__ == "__main__":
	lineas= leer_archivo("miagenda.csv")
	print(lineas)
	
	

