
def hc_o_sc(oracion):
    """Esta función nos permite identificar si la estructura de control
    es rígida (HC) o suave (SC)"""
    h = s = False
    control = None
    for i in oracion:
        if i == 'C':
            if h:
                control = 'Hard Control'
            elif s:
                control = 'Soft Control'
        elif i == 'H':
            h = True
        elif i == 'S':
            s = True
        else:
            h = s = False
        if control:
            break
    return control
def contar_len_cp(oracion):
    """Esta función cuenta cuántos caracteres DIREFENTES de ' ' (blancos)
    tiene la linea en los primeros 9 caracteres"""
    contador = 0
    for i in range(9):
        if oracion[i] != ' ':
            contador += 1
    return contador
def rescatar_cp (oracion):
    """Esta función cuenta cuántos caracteres DIREFENTES de ' ' (blancos)
       tiene la linea en los primeros 9 caracteres"""
    cp  = ''
    for i in range(9):
        if oracion[i] != ' ':
            cp += oracion[i]
    return cp
# contador = contar_len_cp(ora)
def definir_pais(oracion):

    """Esta función nos permite ver de qué pais y región es el cp"""
    # Usamos la función contar_len_cp() dentro de la función definir_pais
    cod_p = rescatar_cp(oracion)
    contador = len(cod_p)
    pais = None
    if contador == 4:
        dig = 0
        for i in cod_p:
            if i.isdigit():
                dig += 1
        if dig == 4:
            pais = 'bolivia'
    elif contador == 5:
        primero = True
        mont = None
        dig = 0
        for i in cod_p:
            if i == ' ':
                continue
            elif i.isdigit():
                dig += 1
                if primero and i == '1':
                    mont = True
                else:
                    primero = False
        if dig == 5:
            pais = 'uruguay'
            if mont:
                pais = 'montevideo'
    elif contador == 6:
        dig = 0
        for i in cod_p:
            if i.isdigit():
                dig += 1
        if dig == 6:
            pais = 'paraguay'
    elif contador == 7:
        dig = 0
        for i in cod_p:
            if i.isdigit():
                dig += 1
        if dig == 7:
            pais = 'chile'
    elif contador == 9:
        dig = 0
        for i in cod_p:
            if i.isdigit():
                dig += 1
        if dig == 8 and cod_p[5] == '-':
            if cod_p[0] == '8' or cod_p[0] == '9':
                pais = 'brasil_20'
            elif cod_p[0] == '0' or cod_p[0] == '1' or cod_p[0] == '2' or cod_p[0] == '3':
                pais = 'brasil_25'
            elif cod_p[0] == '4' or cod_p[0] == '5' or cod_p[0] == '6' or cod_p[0] == '7':
                pais = 'brasil_30'
    elif contador == 8:
        prov = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        verif = 0
        primero = True
        dig = 0
        letra = 0
        for i in cod_p:
            if i == ' ':
                continue
            elif i.isalpha() and primero:
                primero = False
                if i.lower() in prov:
                    verif += 1
                else:
                    primero = True
            elif i.isdigit() and dig < 4 and not primero:
                dig += 1
                verif += 1
            elif i.isalpha() and dig == 4 and letra < 3:
                letra += 1
                verif += 1
            else:
                primero = True
                verif = 0
        if verif == 8:
            pais = 'argentina'
    if pais == None:
        pais = 'otros'
    return pais
def precio_envio(oracion):
    """Devuelve el id del envío y el valor a pagar.
    Hay que poner '-3' porque el último caracter de cada
    linea es '\n' """
    pen_ult = -2
    if oracion[-1] == '\n':
        pen_ult = -3
    if oracion[pen_ult] == '0':
        return int(oracion[pen_ult]), 1100
    elif oracion[pen_ult] == '1':
        return int(oracion[pen_ult]), 1800
    elif oracion[pen_ult] == '2':
        return int(oracion[pen_ult]), 2450
    elif oracion[pen_ult] == '3':
        return int(oracion[pen_ult]), 8300
    elif oracion[pen_ult] == '4':
        return int(oracion[pen_ult]), 10900
    elif oracion[pen_ult] == '5':
        return int(oracion[pen_ult]), 14300
    elif oracion[pen_ult] == '6':
        return int(oracion[pen_ult]), 17900
def ajuste_precios(region):
    """Devuelve el valor para multiplicar al precio para ajustar al exterior"""
    region_20 = 'bolivia', 'paraguay', 'montevideo', 'brasil_20'
    region_25 = 'chile', 'uruguay', 'brasil_25'
    region_30 = 'brasil_30'
    region_50 = 'otros'
    if region in region_20:
        return 1.20
    elif region in region_25:
        return 1.25
    elif region == region_30:
        return 1.30
    elif region == region_50:
        return 1.50
    elif region == 'argentina':
        return 1
def validar_direccion(oracion):
    cl = cn = 0
    num = sm = False
    solo_car = doble_mayus = True
    for car in oracion[9:29]:
        if 'A' <= car <= 'z':
            cl += 1
            if 'A' <= car <= 'Z' and sm:
                doble_mayus = False
            elif 'A' <= car <= 'Z':
                sm = True
            else:
                sm = False
        elif car.isdigit():
            cn += 1
            sm = False
        elif car == '.' or car == ' ':
            if cl == 0 and cn > 0:
                num = True
            cl = cn = 0
            sm = False
        else:
            solo_car = False
            break
    if solo_car and num and doble_mayus:
        return True
    else:
        return False
def mayor_carta(cs, cc, ce):
    """Devuelve la carta con más ocurrencias"""
    if cs > cc and cs > ce:
        mayor = "Carta Simple"
    elif cc > ce:
        mayor = 'Carta Certificada'
    else:
        mayor = 'Carta Expresa'
    return mayor
def calcular_promedio(cant, total):
    if total == 0:
        prom = 0
    else:
        prom = int(cant/total)
    return prom
def calcular_porcentaje(cant, total):
    if total == 0:
        porc = 0
    else:
        porc = int(cant*100/total)
    return porc
def es_brasil(region):
    if region in ('brasil_20', 'brasil_25', 'brasil_30'):
        return True
    else:
        return False
def es_exterior(region):
    if region != 'argentina':
        return True
    else:
        return False
def es_bsas(region, cp):
    if region == 'argentina' and cp[0].lower() == 'b':
        return True
    else:
        return False
def tiene_descuento(oracion):
    if oracion[-2] == '1':
        return True
    else:
        return False
def principal():
    hc = sc = False
    prim_linea = seg_linea = True
    control = tipo_mayor = primer_cp = menimp = mencp = None
    cedvalid = cedinvalid = imp_acu_total = ccs = ccc = cce = \
    contador = exterior = cont_bsas = suma_bsas = 0
    cant_primer_cp = descuento = 1
    with open("envios500b.txt", "r") as archivo:

        for linea in archivo:
            if prim_linea:
                control = hc_o_sc(linea)
                if control == 'Hard Control':
                    hc = True
                elif control == 'Soft Control':
                    sc = True
                prim_linea = False
            else:
                contador += 1
                cp = rescatar_cp(linea)
                if seg_linea:
                    primer_cp = cp
                    seg_linea = False
                elif cp == primer_cp:
                    cant_primer_cp += 1
                region = definir_pais(linea)
                descuento = 1
                if tiene_descuento(linea):
                    descuento = 0.9
                precio = precio_envio(linea)
                ajuste = ajuste_precios(region)
                importe = int(int(precio[1] * ajuste) * descuento)

                if es_brasil(region):
                    if menimp == None or importe < menimp:
                        menimp = importe
                        mencp = cp
                if hc:
                    if validar_direccion(linea):

                        cedvalid += 1
                        imp_acu_total += importe

                        if precio[0] == 0 or precio[0] == 1 or precio[0] == 2:
                            ccs += 1
                        elif precio[0] == 3 or precio[0] == 4:
                            ccc += 1
                        elif precio[0] == 5 or precio[0] == 6:
                            cce += 1

                        if es_exterior(region):
                            exterior += 1
                        elif es_bsas(region, cp):
                            cont_bsas += 1
                            suma_bsas += importe

                    else:
                        cedinvalid += 1

                elif sc:
                    cedvalid += 1
                    cp = rescatar_cp(linea)
                    region = definir_pais(linea)
                    precio = precio_envio(linea)
                    descuento = 1
                    if tiene_descuento(linea):
                        descuento = 0.9
                    ajuste = ajuste_precios(region)
                    importe = int(int(precio[1] * ajuste) * descuento)
                    imp_acu_total += importe

                    if precio[0] in (0, 1, 2):
                        ccs += 1
                    elif precio[0] in (3, 4):
                        ccc += 1
                    elif precio[0] in (5, 6):
                        cce += 1

                    if es_exterior(region):
                        exterior += 1
                    elif es_bsas(region, cp):
                        cont_bsas += 1
                        suma_bsas += importe

        tipo_mayor = mayor_carta(ccs, ccc, cce)
        porc = calcular_porcentaje(exterior, contador)
        prom = calcular_promedio(suma_bsas, cont_bsas)








        print(' (r1) - Tipo de control de direcciones:', control)
        print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
        print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
        print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
        print(' (r5) - Cantidad de cartas simples:', ccs)
        print(' (r6) - Cantidad de cartas certificadas:', ccc)
        print(' (r7) - Cantidad de cartas expresas:', cce)
        print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
        print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
        print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
        print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
        print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
        print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
        print('(r14) - Importe final promedio de los envios Buenos Aires:', prom)
principal()