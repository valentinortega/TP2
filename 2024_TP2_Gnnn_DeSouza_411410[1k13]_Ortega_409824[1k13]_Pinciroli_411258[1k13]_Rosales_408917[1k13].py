# Importamos los envíos
txt = open('envios.txt')
envios = txt.read()
txt.close()

def tipo_de_control(envios):
    th = ts = False
    for car in envios:
        if car == 'H':
            th = True
            ts = False
        elif car == 'S':
            ts = True
            th = False
        elif car == 'C':
            if th:
                return 'Hard Control'
            elif ts:
                return 'Soft Control'
            th = ts = False

print(' (r1) - Tipo de control de direcciones:', tipo_de_control(envios))
