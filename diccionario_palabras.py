meme_dict = {
            "LOL": "una respuesta a algo gracioso",
            "CRINGE": "algo raro o embarazoso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            }
for i in range (5):
    word = input("¿Que palabra no entiendes?")

    if word in meme_dict.keys():
        print ( meme_dict[word])
    else:
        print ("No se encontro la palabra :(")
