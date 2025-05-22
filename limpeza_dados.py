import pandas as pd
import numpy as np
from typing import Dict, Optional, List, Union
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def limpar_colunas_numericas(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include=['float64']).columns:
        df[col] = df[col].astype('float32')
    for col in df.select_dtypes(include=['int64']).columns:
        df[col] = df[col].astype('int32')
    return df

def limpar_colunas_categoricas(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')
    return df

def remover_duplicatas(df: pd.DataFrame, subset: Optional[List[str]] = None) -> pd.DataFrame:
    original_len = len(df)
    df = df.drop_duplicates(subset=subset)
    removed = original_len - len(df)
    if removed > 0:
        logging.info(f"Removed {removed} duplicate rows")
    return df

def tratar_valores_faltantes(df: pd.DataFrame, 
                           estrategia_numerica: str = 'mean',
                           estrategia_categorica: str = 'mode') -> pd.DataFrame:
    
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if pd.api.types.is_numeric_dtype(df[col]):
                if estrategia_numerica == 'mean':
                    df[col] = df[col].fillna(df[col].mean())
                elif estrategia_numerica == 'median':
                    df[col] = df[col].fillna(df[col].median())
                elif estrategia_numerica == 'zero':
                    df[col] = df[col].fillna(0)
            else:
                if estrategia_categorica == 'mode':
                    df[col] = df[col].fillna(df[col].mode()[0])
                elif estrategia_categorica == 'missing':
                    df[col] = df[col].fillna('MISSING')
    
    return df

def normalizar_coluna(df: pd.DataFrame, coluna: str, metodo: str = 'min-max') -> pd.DataFrame:
    if metodo == 'min-max':
        df[f'{coluna}_normalizado'] = (df[coluna] - df[coluna].min()) / (df[coluna].max() - df[coluna].min())
    elif metodo == 'z-score':
        df[f'{coluna}_normalizado'] = (df[coluna] - df[coluna].mean()) / df[coluna].std()
    return df

def remover_outliers(df: pd.DataFrame, coluna: str, metodo: str = 'iqr', limite: float = 1.5) -> pd.DataFrame:
    if metodo == 'iqr':
        Q1 = df[coluna].quantile(0.25)
        Q3 = df[coluna].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - limite * IQR
        limite_superior = Q3 + limite * IQR
        df = df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]
    elif metodo == 'z-score':
        z_scores = np.abs((df[coluna] - df[coluna].mean()) / df[coluna].std())
        df = df[z_scores < limite]
    return df

def limpar_strings(df: pd.DataFrame, colunas: List[str]) -> pd.DataFrame:
    for col in colunas:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.upper()
    return df

def converter_datas(df: pd.DataFrame, colunas: List[str], formato: str = '%Y-%m-%d') -> pd.DataFrame:
    for col in colunas:
        if col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col], format=formato)
            except Exception as e:
                logging.warning(f"Could not convert column {col} to datetime: {e}")
    return df

def limpar_dados_completos(df: pd.DataFrame, 
                          colunas_string: Optional[List[str]] = None,
                          colunas_data: Optional[List[str]] = None,
                          remover_duplicatas_colunas: Optional[List[str]] = None) -> pd.DataFrame:
    
    df = limpar_colunas_numericas(df)
    df = limpar_colunas_categoricas(df)
    
    if colunas_string:
        df = limpar_strings(df, colunas_string)
    
    if colunas_data:
        df = converter_datas(df, colunas_data)
    
    if remover_duplicatas_colunas:
        df = remover_duplicatas(df, remover_duplicatas_colunas)
    
    df = tratar_valores_faltantes(df)
    
    return df

if __name__ == "__main__":
    logging.info("This module contains data cleaning functions. Import and use them in your main script.") 