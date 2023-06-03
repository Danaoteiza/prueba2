
import urllib.parse
import requests
import datetime

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Ml2LpD0hkaowqQno2QXIjhACICrxwQjT"

while True:
    orig = input("Ubicación de partida: ")
    if orig == "exit" or orig == "exit":
        break
    dest = input("Destino: ")
    if dest == "exit" or dest == "exit":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("Estado de la API: " + str(json_status) + " = Llamada de ruta exitosa.\n")
        print("=============================================")
        
        # Obtener la hora local
        current_time = datetime.datetime.now().strftime("%H:%M")
        print("¡Bienvenido! La hora local es: " + current_time)
        
        print("Cómo llegar desde " + orig + " a " + dest)
        print("Duración del viaje: " + json_data["route"]["formattedTime"])
        print("Kilómetros: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.61)))

        print("=============================================")

        print("Maniobras:")
        maneuvers = json_data["route"]["legs"][0]["maneuvers"]
        for maneuver in maneuvers:
            narrative = maneuver["narrative"]
            distance_km = maneuver["distance"] * 1.61
            print("- " + narrative + " (" + str("{:.4f}".format(distance_km)) + " km)")

        print("=============================================")
        
    elif json_status == 402:
        print("**********************************************")
        print("Código de estado: " + str(json_status) + "; Entradas de usuario inválidas para una o ambas ubicaciones.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Código de estado: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        