# Standard Library
from itertools import cycle


def validarRut(rut):
    rut = rut.upper().replace("-", "").replace(".", "")
    aux = rut[:-1]
    dv = rut[-1:]

    revertido = map(int, reversed(str(aux)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(revertido, factors))
    res = (-s) % 11

    if str(res) == dv:
        return True
    elif dv == "K" and res == 10:
        return True
    else:
        return False


def check_rut(document_number, fomat):
    if document_number:
        int_rut = document_number.upper().replace("-", '').replace(".", '').replace(",", '').replace("C", '').replace("L", '').replace(" ", '')
        int_rut_impio = int_rut.strip()
        ok = False
        if len(int_rut) > 8:
            if validarRut(int_rut):
                ok = True
        else:
            ok = True
        # Formateamos el RUT con el estandar 24.063.888-6
        position = len(int_rut) - 1
        int_rut = int_rut[:position] + '-' + int_rut[position:]
        int_rut = int_rut[:-5] + '.' + int_rut[-5:]
        if len(int_rut) > 9:
            # 24.063.888-6
            if fomat == 1:
                int_rut = int_rut[:-9] + '.' + int_rut[-9:]
            if fomat == 2:
                int_rut = 'CL' + int_rut_impio
        if not ok:
            return ''
        else:
            return int_rut
