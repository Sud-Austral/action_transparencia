import pandas as pd



if __name__ == '__main__':
    lista = ["consolidado.xlsx"] + [f"consolidado{i}.xlsx" for i in range(2,8)]
    salida = []
    for name in lista:
        salida.append(pd.read_excel(i).copy())
    pd.concat(salida).to_excel("Consolidado_final.xlsx", index=False)