# ===================================
# Este script permite adicionar lineas
# a un archivo en formato CSV, con (;)
# ===================================

def agregar_contenido(archivo="", lineas=[]):
	"""
	params
		archivo - ubicacion del archivo
		lineas - contenido del archivo
	return
		void
	"""
	my_archivo = open(archivo, "a+")
	for linea in lineas:
		my_archivo.write(";".join( linea ))
	my_archivo.close()

if __name__ == "__main__":
	lineas = [
		"Marcela;diaz;diasmm@hotmail.com\n",
		"Daniel;pena;ddnnpena@hotmail.com\n",
	]
	agregar_contenido("miagenda.csv", lineas)
	
	


