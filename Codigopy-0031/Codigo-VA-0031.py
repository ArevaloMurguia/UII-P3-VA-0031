# === Arevalo Rafael NC: 0031 === 

# Importamos las librerias
import os
import cv2
import matplotlib.pyplot as plt

# Obtenemos la ubicacion del archivo Python
carpeta_codigo = os.path.dirname(os.path.abspath(__file__))
carpeta_principal = os.path.dirname(carpeta_codigo)

# Rutas de las carpetas
carpeta_imagenes = os.path.join(
    carpeta_principal, "Img-Original-0031"
)

carpeta_resultados = os.path.join(
    carpeta_principal, "Resultados-Img-0031"
)

# Creamos la carpeta de resultados si no existe
os.makedirs(carpeta_resultados, exist_ok=True)

# Ruta de la imagen original
ruta_imagen = os.path.join(
    carpeta_imagenes, "Refrigerador.jpg"
)

# Cargamos la imagen en formato BGR
img_bgr = cv2.imread(ruta_imagen)

# Verificamos si se cargo correctamente
if img_bgr is None:
    print("Error: No se pudo cargar la imagen.")
    print("Ruta buscada:", ruta_imagen)

else:
    print("Imagen cargada correctamente.")

    # Mostramos las dimensiones de la imagen
    print("Dimensiones:", img_bgr.shape)

    # Convertimos de BGR a RGB
    img_rgb = cv2.cvtColor(
        img_bgr, cv2.COLOR_BGR2RGB
    )

    # Separamos los canales RGB
    R, G, B = cv2.split(img_rgb)

    # Reconstruimos la imagen RGB
    img_reconstruida = cv2.merge((R, G, B))

    # Guardamos la imagen original en BGR
    cv2.imwrite(
        os.path.join(
            carpeta_resultados, "01_Imagen_BGR.jpg"
        ),
        img_bgr
    )

    # Guardamos la imagen RGB convertida a BGR
    cv2.imwrite(
        os.path.join(
            carpeta_resultados, "02_Imagen_RGB.jpg"
        ),
        cv2.cvtColor(
            img_rgb, cv2.COLOR_RGB2BGR
        )
    )

    # Guardamos los canales individuales
    cv2.imwrite(
        os.path.join(carpeta_resultados, "03_Canal_Rojo.jpg"),
        R
    )

    cv2.imwrite(
        os.path.join(carpeta_resultados, "04_Canal_Verde.jpg"),
        G
    )

    cv2.imwrite(
        os.path.join(carpeta_resultados, "05_Canal_Azul.jpg"),
        B
    )

    # Guardamos la imagen reconstruida
    cv2.imwrite(
        os.path.join(
            carpeta_resultados, "06_Imagen_Reconstruida.jpg"
        ),
        cv2.cvtColor(
            img_reconstruida, cv2.COLOR_RGB2BGR
        )
    )

    # Creamos la figura para mostrar los resultados
    fig = plt.figure(figsize=(14, 9))

    # IMAGEN BGR
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    ax1.set_title("IMAGEN ORIGINAL BGR")
    ax1.axis("off")

    # IMAGEN RGB
    ax2 = fig.add_subplot(2, 3, 2)
    ax2.imshow(img_rgb)
    ax2.set_title("IMAGEN CONVERTIDA A RGB")
    ax2.axis("off")

    # CANAL ROJO
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.imshow(R, cmap="gray", vmin=0, vmax=255)
    ax3.set_title("CANAL ROJO (R)")
    ax3.axis("off")

    # CANAL VERDE
    ax4 = fig.add_subplot(2, 3, 4)
    ax4.imshow(G, cmap="gray", vmin=0, vmax=255)
    ax4.set_title("CANAL VERDE (G)")
    ax4.axis("off")

    # CANAL AZUL
    ax5 = fig.add_subplot(2, 3, 5)
    ax5.imshow(B, cmap="gray", vmin=0, vmax=255)
    ax5.set_title("CANAL AZUL (B)")
    ax5.axis("off")

    # IMAGEN RECONSTRUIDA
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.imshow(img_reconstruida)
    ax6.set_title("IMAGEN RECONSTRUIDA RGB")
    ax6.axis("off")

    # Ajustamos la presentacion
    plt.tight_layout()

    # Guardamos la figura completa
    ruta_figura = os.path.join(
        carpeta_resultados, "07_Resultados_Completos.png"
    )

    plt.savefig(
        ruta_figura,
        dpi=150,
        bbox_inches="tight"
    )

    # Mostramos los resultados
    plt.show()

    # Mensaje final
    print("\nResultados guardados en:")
    print(carpeta_resultados)
    print("\nArchivos guardados correctamente.")