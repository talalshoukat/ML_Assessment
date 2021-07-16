import pandas as pd 

def mapping(notes_path,patient_path,admission_path,processed_path):
    notes = pd.read_csv(notes_path).drop('id', axis=1)
    patient = pd.read_csv(patient_path)
    admission = pd.read_csv(admission_path).drop('id', axis=1) 
    processed = pd.read_csv(processed_path).drop('id', axis=1) 
    admission.rename(columns={'admision_type': 'admission_type'},inplace=True)
    # notes['admission_type'] = notes.reg_number.astype(str).str[:2]
    notes['patient_number'] = notes.reg_number.astype(str).str[2:8]
    notes['year'] ='20'+notes.reg_number.astype(str).str[-2:]
    notes.drop('reg_number', axis=1,inplace=True)
    notes["patient_number"] = pd.to_numeric(notes["patient_number"])
    processedpatient = patient.merge(processed, how='left', on='patient_number',suffixes=('', '_proc'))
    processed_notes_pat = processedpatient.merge(notes, how='left', on='patient_number',suffixes=('', '_notes'))
    merged_df = processed_notes_pat.merge(admission, how='left', on='citizen_number',suffixes=('', '_adm'))
    merged_df['admission_date'].fillna(merged_df['admission_date_adm'],inplace=True)
    merged_df['admission_type'].fillna(merged_df['admission_type_adm'],inplace=True)
    merged_filter =  merged_df[merged_df.iloc[:, -4:].isnull().all(axis='columns')].groupby(["admission_date","admission_type"]).filter(lambda x: len(x) == 1)
    merged_filter.drop(merged_filter.iloc[:, -4:], axis=1,inplace=True)
    
    # Filtering data in admission DF where Citizen Number is null and admission_date and admission_type are unique
    adm_filter = admission[admission["citizen_number"].isna()].groupby(["admission_date","admission_type"]).filter(lambda x: len(x) == 1)
    adm_filter.drop(['citizen_number'], axis=1,inplace=True)
    
    # Joining filtered unmatched data with the Admission data (in which CNIC is NA) based on admission date and Type
    temp =merged_filter.merge(adm_filter, how='left', on= ['admission_date','admission_type'])
    merged_df = merged_df.set_index("citizen_number").combine_first(temp.set_index("citizen_number")).reset_index()
    merged_df.drop('admission_date_adm', axis=1,inplace=True)
    merged_df.drop('admission_type_adm', axis=1,inplace=True)
    return merged_df[merged_df["discharge_date"].notna()]
    