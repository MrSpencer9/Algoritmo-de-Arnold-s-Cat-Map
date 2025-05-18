import os
from PIL.Image import open as load_pic, new as new_pic

def arnolds_cat_map(path, iterations, keep_all=False, name="arnold_cat-{name}-{index}.png"):
    """
    Implementación del Arnold's Cat Map.
    Parámetros:
        path: str -> Ruta de la imagen a procesar.
        iterations: int -> Número de iteraciones a realizar.
        keep_all: bool -> Guardar todas las iteraciones.
        name: str -> Formato del nombre de archivo.
    """
    title = os.path.splitext(os.path.split(path)[1])[0]
    counter = 0

    # Verificar si la carpeta results existe, si no, crearla
    if not os.path.exists("results"):
        os.makedirs("results")

    while counter < iterations:
        with load_pic(path) as image:
            dim = width, height = image.size
            with new_pic(image.mode, dim) as canvas:
                for x in range(width):
                    for y in range(height):
                        nx = (2 * x + y) % width
                        ny = (x + y) % height
                        canvas.putpixel((nx, height - ny - 1), image.getpixel((x, height - y - 1)))

                # Crear el nombre del archivo con la ruta correcta
                filename = os.path.join("results", name.format(name=title, index=counter + 1))

                # Guardar la imagen en la carpeta results
                canvas.save(filename)

                if counter > 0 and not keep_all:
                    os.remove(path)

                counter += 1
                path = filename

    return canvas

if __name__ == "__main__":
    path = input("Ingrese la ruta a una imagen (por ejemplo, images/cat.jpg): \n\t")
    while not os.path.exists(path):
        path = input("No se encontró la imagen, intenta nuevamente: \n\t")
    iterations = int(input("Ingrese el número de iteraciones: "))
    result = arnolds_cat_map(path, iterations)
    result.show()
