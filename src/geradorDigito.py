import random

from flask import request


# Recebe documentos via form
def get_doc():
    lista_docs = []
    docs = request.form.get("docs")
    if docs != None:
        # split por ','
        if " " in docs:
            lista_docs = docs.split(" ")
        else:
            lista_docs.append(docs.split(","))
            lista_docs = lista_docs[0]
    return lista_docs

# Recebe o tipo de pessoa via form
def get_tp_pess():
    tipo_pess = request.form.get("tipo_pess")
    if tipo_pess != None:
        tipo_pess = tipo_pess.upper()

    if tipo_pess == 'CPF':
            list_result_cpf = []
            cpfs = get_doc()
            #  Gera os primeiros nove dígitos (e certifica-se de que não são todos iguais)
            for doc in cpfs:
                if len(doc) != 11:
                    cpf = str(doc).rjust(9, "0")
                    cpf = list(cpf)
                    cpf = [int(val) for val in cpf]
                    # Gera os dois dígitos verificadores
                    for i in range(2):
                        value = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
                        cpf.append(11 - value if value > 1 else 0)
                    #  Retorna o CPF como string
                    result = "".join(map(str, cpf))
                    list_result_cpf.append(result)
                else:
                    list_result_cpf.append(doc)
            return list_result_cpf

    else:
    # Func chamada se tipo pessoal for igual a pj
        list_result_cnpj = []
        cnpjs = get_doc()
        #  Gera os primeiros nove dígitos (e certifica-se de que não são todos iguais)
        for doc in cnpjs:
            if len(doc) != 14:
                cnpj = str(doc).rjust(8, "0")
                cnpj = list(cnpj)
                cnpj = [int(val) for val in cnpj]
                cnpj += [0, 0, 0, 1]
                #  Gera os dois dígitos verificadores
                for i in range(2):
                    value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
                    digit = 11 - value % 11
                    cnpj.append(digit if digit < 10 else 0)
                #  Retorna o CNPJ como string
                result = "".join(map(str, cnpj))
                list_result_cnpj.append(result)
            else:
                list_result_cnpj.append(doc)
        return list_result_cnpj
