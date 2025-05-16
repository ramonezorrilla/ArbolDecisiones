# Árbol de decision para recomendacion de peliculas

print("Bienvenido al recomendador de peliculas")

estado_animo = input("Como te sientes hoy? (feliz/triste): ").lower()

if estado_animo == "feliz":
    gusta_accion = input("Te gustan las peliculas de accion? (si/no): ").lower()
    if gusta_accion == "si":
        print("Te recomiendo ver: Avengers: Endgame")
    else:
        print("Te recomiendo ver: Forrest Gump")

elif estado_animo == "triste":
    tipo_pelicula = input("Prefieres comedias o dramas?: ").lower()
    if tipo_pelicula == "comedias":
        print("Te recomiendo ver: The Mask")
    elif tipo_pelicula == "dramas":
        print("Te recomiendo ver: The Pursuit of Happyness")
    else:
        print("No tengo una recomendacion para ese tipo.")
else:
    print("No entendi tu estado de animo. Intenta escribir feliz o triste.")

    ##Probando