# Iris Chavez NC 0032
# Ejemplo 1

import cv2

# Cargar la imagen
imagen = cv2.imread("p9-act13-0032/imagenes/oso p9-act13-0032.jpg")

# Comprobar que la imagen fue cargada
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes mediante Canny
bordes = cv2.Canny(gris, 100, 200)

# Mostrar resultados
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen en escala de grises", gris)
cv2.imshow("Bordes Canny", bordes)

# Guardar resultado
cv2.imwrite("../resultados/ejemplo1_canny.jpg", bordes)

print("Detección de bordes completada.")
print("Resultado guardado en resultados/ejemplo1_canny.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

# Iris Chavez NC 0032