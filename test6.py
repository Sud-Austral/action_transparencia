import pandas as pd
from datetime import datetime

date_format = "%Y/%m/%d"

columnas_deseadas = ['organismo_nombre', 'organismo_codigo', 'fecha_publicacion_ta', 'anyo',
       'Mes']

columnas_deseadas2 = ['organismo_nombre', 'organismo_codigo', 'fecha_publicacion', 'anyo',
       'Mes']

base = "https://www.cplt.cl/transparencia_activa/datoabierto/archivos/"
TA_PasivosMunicipio                     = f"{base}TA_PasivosMunicipio.csv"
TA_ActosDocPublicadosenDO               = f"{base}TA_ActosDocPublicadosenDO.csv"
TA_Potestades_otras                     = f"{base}TA_Potestades_otras.csv"
TA_Marco_normativo                      = f"{base}TA_Marco_normativo.csv"
TA_Facultades_funciones_atribuciones    = f"{base}TA_Facultades_funciones_atribuciones.csv"
TA_Otras_transferencias                 = f"{base}TA_Otras_transferencias.csv"
TA_Tramites_ante_consejo                = f"{base}TA_Tramites_ante_consejo.csv"
TA_ParticipacionCiudadana               = f"{base}TA_ParticipacionCiudadana.csv"
TA_Auditorias                           = f"{base}TA_Auditorias.csv"
TA_Subsidios_beneficios_intermediarios  = f"{base}TA_Subsidios_beneficios_intermediarios.csv"
TA_Subsidios_beneficios                 = f"{base}TA_Subsidios_beneficios.csv"
TA_PersonalPlanta                       = f"{base}TA_PersonalPlanta.csv"
TA_PersonalContrata                     = f"{base}TA_PersonalContrata.csv"
TA_PersonalCodigotrabajo                = f"{base}TA_PersonalCodigotrabajo.csv"
TA_PersonalContratohonorarios           = f"{base}TA_PersonalContratohonorarios.csv"
TA_Otras_compras                        = f"{base}TA_Otras_compras.csv"
TA_Otras_autoridades                    = f"{base}TA_Otras_autoridades.csv"
TA_Nomina_beneficiarios                 = f"{base}TA_Nomina_beneficiarios.csv"
TA_Licitaciones                         = f"{base}TA_Licitaciones.csv"

def getDF(url):
    return pd.read_csv(url,sep=";",encoding="latin")


parte1 = [TA_PasivosMunicipio                      ,
                TA_ActosDocPublicadosenDO               ,
                TA_Potestades_otras                     ,
                TA_Marco_normativo                      ,
                TA_Facultades_funciones_atribuciones    ,
                TA_Otras_transferencias                 ,
                TA_Tramites_ante_consejo                ,
                TA_ParticipacionCiudadana               ,
                TA_Auditorias                           ,
                TA_Subsidios_beneficios_intermediarios  ,
                TA_Subsidios_beneficios                 ,
                #TA_PersonalPlanta                       ,
                #TA_PersonalContrata                     ,
                #TA_PersonalCodigotrabajo                ,
                #TA_PersonalContratohonorarios           ,
                #TA_Otras_compras                        ,
                #TA_Otras_autoridades                    ,
                #TA_Nomina_beneficiarios                 ,
                #TA_Licitaciones
                ]
parte2 = [TA_PersonalPlanta]
parte3 = [TA_PersonalContrata]
parte4 = [TA_PersonalCodigotrabajo]
parte5 = [
                #TA_PersonalContratohonorarios           ,
                #TA_Otras_compras                        ,
                #TA_Otras_autoridades                    ,
                TA_Nomina_beneficiarios                 ,
                TA_Licitaciones
                ]

parte6 = [TA_PersonalContratohonorarios]


def descarga():
    salida = []
    for url in parte6:       
        #df = pd.read_csv(url, sep=";", encoding="latin")     
        df = pd.read_csv(url, sep=";", encoding="latin", usecols=columnas_deseadas2)   
        nombreArchivo = url.replace(base,"").replace(".csv","")        
        df["Archivo"] = nombreArchivo
        #print(df.shape)
        salida.append(df.copy())
    return salida

def consolidar():
    lista = descarga()

    consolidador = []
    for df in lista:
        acumulador = []
        diccionario = {}
        diccionario["Archivo"] = df.iloc[0]["Archivo"]
        
        diccionario["Institucion"] = "No Institucion"
        diccionario["Última Actualización"] = ""
        for mes in ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]:
            diccionario[mes] = 0
        diccionario["Sin Año-Mes"] = 0
        diccionario["Sin Mes"] = 0
        diccionario["Sin Año"] = 0
        diccionario["Total"] = 0
        acumulador.append(diccionario.copy())
        for anyo in [2022,2023,2024]:
            df2 = df[df["anyo"] == anyo]
            for institucion in df2['organismo_nombre'].unique()[:5]: 
                dfIntitucion = df2[df2['organismo_nombre'] == institucion]
                diccionario = {}
                diccionario["Archivo"] = df.iloc[0]["Archivo"]
                try:
                    diccionario["Última Actualización"] = dfIntitucion["fecha_publicacion_ta"].max()
                    #print("fecha1",diccionario["Última Actualización"])
                except:
                    diccionario["Última Actualización"] = dfIntitucion["fecha_publicacion"].max()
                    #print("fecha2",diccionario["Última Actualización"])   
                print(anyo,institucion,diccionario["Última Actualización"])
                diccionario["Institucion"] = institucion
                diccionario["Codigo"] = dfIntitucion.iloc[0]["organismo_codigo"]
                diccionario["Sin Año-Mes"] = len(dfIntitucion.query('Mes.isnull() and anyo.isnull()'))
                for mes in dfIntitucion["Mes"].unique():
                    diccionario[mes] = "x"
                diccionario["Sin Mes"] = len(dfIntitucion.query('Mes.isnull() and anyo.notnull()'))
                diccionario["Sin Año"] = len(dfIntitucion.query('Mes.notnull() and anyo.isnull()'))
                diccionario["Total"] = len(dfIntitucion)    
                diccionario["año_auditoria"] = anyo
                acumulador.append(diccionario.copy())
        salida = pd.DataFrame(acumulador)
        salida2 = salida[salida["Institucion"] != "No Institucion"]
        salida2["Fecha"] = salida2["Última Actualización"].apply(lambda x:datetime.strptime(x, date_format))
        consolidador.append(salida2.copy())
    final = pd.concat(consolidador)
    final.to_excel("consolidado6.xlsx", index=False)


if __name__ == '__main__':
    consolidar()