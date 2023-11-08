import pandas as pd



if __name__ == '__main__':
    lista = ['consolidado.xlsx',
            'consolidado2.xlsx',
            'consolidado3.xlsx',
            'consolidado4.xlsx',
            'consolidado5.xlsx',
            'consolidado6.xlsx',
            'consolidado7.xlsx']
    salida = []
    for name in lista:
        salida.append(pd.read_excel(name).copy())
    pd.concat(salida).to_excel("Consolidado_final.xlsx", index=False)