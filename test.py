import pandas as pd

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


def descarga():
    for url in [TA_PasivosMunicipio                      ,
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
                TA_PersonalPlanta                       ,
                TA_PersonalContrata                     ,
                TA_PersonalCodigotrabajo                ,
                TA_PersonalContratohonorarios           ,
                TA_Otras_compras                        ,
                TA_Otras_autoridades                    ,
                TA_Nomina_beneficiarios                 ,
                TA_Licitaciones]
        print(url)


if __name__ == '__main__':
    descarga()