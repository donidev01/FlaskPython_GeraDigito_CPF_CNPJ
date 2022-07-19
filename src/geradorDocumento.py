import random

from flask import request


# Recebe documentos via form
def get_qtddoc():
    qtddoc = request.form.get("qtddocs")
    if qtddoc != None:
        qtddoc = int(qtddoc)
    return qtddoc

# Recebe o tipo de pessoa via form
def get_tp_pess():
    tipo_pess = request.form.get("tipo_pess")
    if tipo_pess != None:
        tipo_pess = tipo_pess.upper()

        if tipo_pess == 'CPF':    
            listadocs = []
            qtddocs = get_qtddoc()
            for e in range(qtddocs):  # type: ignore
                cpf = [random.randrange(10) for _ in range(9)]

                for e in range(2):
                    value = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
                    cpf.append(11 - value if value > 1 else 0)
                listadocs.append("".join(str(x) for x in cpf))
            return listadocs
        else:
            listadocs = []
            qtddocs = get_qtddoc()
            for e in range(qtddocs):  # type: ignore
                cnpj = [random.randrange(10) for _ in range(8)] + [0, 0, 0, 1]

                for e in range(2):
                    value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
                    digit = 11 - value % 11
                    cnpj.append(digit if digit < 10 else 0)
                listadocs.append("".join(str(x) for x in cnpj))
            return listadocs
