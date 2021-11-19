
import argparse
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score
import pickle


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_path',
        type=str,     
        default='../data/Monografia_limpio.csv',  
        help='Path to the training data'
    )   
    args = parser.parse_args()
    df = pd.read_csv(args.data_path)
    df=df.drop('Unnamed: 0', axis=1)
    # df.columns=['EDAD','CANTIDAD_MARCA','CANT_HOSPITALIZACION','CANT_URG_ANIO','SEXO_CD_M','RAZA_DESC_BLANCO','RAZA_DESC_INDÍGENA','RAZA_DESC_MESTIZO','RAZA_DESC_MULATO','RAZA_DESC_ZAMBO','IMC_TXT_Normal','IMC_TXT_Obesidad','IMC_TXT_Sobrepeso','COLESTEROL_TOTAL_Limite_Alto','COLESTEROL_TOTAL_Normal','COLESTEROL_LDL_TXT_Limite_Alto','COLESTEROL_LDL_TXT_Normal','COLESTEROL_HDL_TXT_Normal','TRIGLICERIDOS_TXT_Limite_Alto','TRIGLICERIDOS_TXT_Normal','ESTADO_CIVIL_DESC_Separado(a)','ESTADO_CIVIL_DESC_Soltero(a)','ESTADO_CIVIL_DESC_UnionLibre','ESTADO_CIVIL_DESC_Viudo(a)','CLASIFICACION_POBLACION_DESC_Enfermo','CLASIFICACION_POBLACION_DESC_EnfermoPresuntivo','CLASIFICACION_POBLACION_DESC_SanoPresuntivo','IND_CIGARRILLO_S','IND_EJERCICIO_S','IND_LICOR_S','IND_POSHOSPITALIZADO_S','IND_POSURGENCIAS_S','IND_HIPERCONSULTANTE_S','IND_ANTICOAGULANTE_NO_WARFA_S','IND_PROTECCIONRENAL_S','IND_DIABETES_S','IND_HIPERTENSION_S','IND_EHC_S','IND_GESTANTES_S','IND_ASMA_S','IND_DISLIPIDEMIA_S','IND_VIH_S','IND_EPOC_S','IND_AUTOINMUNES_S','IND_CANCER_S','IND_INSUFICIENCIACARDIACA_S','IND_CARDIOVASCULAR_S','IND_CEREBROVASCULAR_S','IND_TUBERCULOSIS_S','IND_SIFILIS_S','IND_EVE_DIF_RCV_S','Y_S']
    X = df.drop(['Y_S'],axis=1) 
    y = df['Y_S']    
    # dividimos el conjunto de datos en conjunto de entrenamiento y conjunto de pruebas
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, stratify =y)    
    # estandarizar variables    
    scaler = StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    #Modelo
    Model=LogisticRegression(class_weight='balanced').fit(X_train,y_train)
    y_pred=Model.predict(X_test)
    print(balanced_accuracy_score(y_test,y_pred))
with open('../outputs/rcv_model.pkl', 'wb') as model_pkl:
    pickle.dump(Model, model_pkl)