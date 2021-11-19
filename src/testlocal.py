import pickle
import numpy as np
import json
import pandas as pd
# Load the trained model from current directory
with open('./outputs/rcv_model.pkl', 'rb') as model_pkl:
    model = pickle.load(model_pkl)

if __name__ == "__main__":
    df = pd.DataFrame()
    df['EDAD'] = [59]
    df['CANTIDAD_MARCA'] = 4
    df['CANT_HOSPITALIZACION'] = 0
    df['CANT_URG_ANIO'] = 0
    df['SEXO_CD_M'] = 1
    df['RAZA_DESC_BLANCO'] = 0
    df['RAZA_DESC_INDÍGENA'] = 0
    df['RAZA_DESC_MESTIZO'] = 1
    df['RAZA_DESC_MULATO'] = 0
    df['RAZA_DESC_ZAMBO'] = 0
    df['IMC_TXT_Normal'] = 0
    df['IMC_TXT_Obesidad'] = 0
    df['IMC_TXT_Sobrepeso'] = 1
    df['COLESTEROL_TOTAL_Limite_Alto'] = 0
    df['COLESTEROL_TOTAL_Normal'] = 1
    df['COLESTEROL_LDL_TXT_Limite_Alto'] = 0
    df['COLESTEROL_LDL_TXT_Normal'] = 1
    df['COLESTEROL_HDL_TXT_Normal'] = 1
    df['TRIGLICERIDOS_TXT_Limite_Alto'] = 0
    df['TRIGLICERIDOS_TXT_Normal'] = 1
    df['ESTADO_CIVIL_DESC_Separado(a)'] = 0
    df['ESTADO_CIVIL_DESC_Soltero(a)'] = 1
    df['ESTADO_CIVIL_DESC_UnionLibre'] = 0
    df['ESTADO_CIVIL_DESC_Viudo(a)'] = 0
    df['CLASIFICACION_POBLACION_DESC_Enfermo'] = 0
    df['CLASIFICACION_POBLACION_DESC_EnfermoPresuntivo'] = 1
    df['CLASIFICACION_POBLACION_DESC_SanoPresuntivo'] = 0
    df['IND_CIGARRILLO_S'] = 0
    df['IND_EJERCICIO_S'] = 0
    df['IND_LICOR_S'] = 0
    df['IND_POSHOSPITALIZADO_S'] = 0
    df['IND_POSURGENCIAS_S'] = 0
    df['IND_HIPERCONSULTANTE_S'] = 0
    df['IND_ANTICOAGULANTE_NO_WARFA_S'] = 0
    df['IND_PROTECCIONRENAL_S'] = 1
    df['IND_DIABETES_S'] = 0
    df['IND_HIPERTENSION_S'] = 0
    df['IND_EHC_S'] = 0
    df['IND_GESTANTES_S'] = 0
    df['IND_ASMA_S'] = 0
    df['IND_DISLIPIDEMIA_S'] = 0
    df['IND_VIH_S'] = 0
    df['IND_EPOC_S'] = 1
    df['IND_AUTOINMUNES_S'] = 0
    df['IND_CANCER_S'] = 0
    df['IND_INSUFICIENCIACARDIACA_S'] = 0
    df['IND_CARDIOVASCULAR_S'] = 0
    df['IND_CEREBROVASCULAR_S'] = 0
    df['IND_TUBERCULOSIS_S'] = 0
    df['IND_SIFILIS_S'] = 0
    df['IND_EVE_DIF_RCV_S'] = 0
    print(df.shape)
    predict_result = model.predict(df)
    # print(predict_result)