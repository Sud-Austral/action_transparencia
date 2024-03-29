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
    dfSalida = pd.concat(salida)
    dfSalida2 = dfSalida[['Archivo', 'Institucion', 'Última Actualización', 'Enero', 'Febrero',
       'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
       'Octubre', 'Noviembre', 'Diciembre', 'Sin Año-Mes', 'Sin Mes',
       'Sin Año', 'Total', 'Codigo', 'año_auditoria', 'Fecha']]
    dfSalida.to_excel("Consolidado_final.xlsx", index=False)


    lista_historico = ['consolidado_historico.xlsx',
                        "consolidado_historico2.xlsx",
                        "consolidado_historico3.xlsx",
                        "consolidado_historico4.xlsx",
                        "consolidado_historico5.xlsx",
                        "consolidado_historico6.xlsx"]
    salida_historico = []
    for name in lista_historico:
        salida_historico.append(pd.read_excel(name).copy())
    dfSalida_historico = pd.concat(salida_historico)
    dfSalida_historico.to_excel("Consolidado_historico_final.xlsx", index=False)

