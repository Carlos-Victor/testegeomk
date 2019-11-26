from django.core.exceptions import ValidationError
import re

def placa(value):
    if len(value) < 7 or len(value) > 8:
        raise ValidationError(('A placa tem que possuir 7 caracteres'))
    if len(value) == 7:
        letras = re.findall("[a-zA-Z]", value[0:3])
        numeros = re.findall("[0-9]", value[3:8])
        if len(letras) != 3:
            raise ValidationError(('Os 3 primeiros digitos precisam ser Letras, EX:XXX0000'))
        if len(numeros) != 4:
            raise ValidationError(('Os 4 ultimos digitos precisam ser números, EX:XXX0000'))
    if len(value) == 8:
        letras = re.findall("[a-zA-Z]", value[0:3])
        numeros = re.findall("[0-9]", value[3:9])
        if len(letras) != 3:
            raise ValidationError(('Os 3 primeiros digitos precisam ser Letras, EX:XXX-0000'))
        if len(numeros) != 4:
            raise ValidationError(('Os 4 ultimos digitos precisam ser números, EX:XXX-0000'))
