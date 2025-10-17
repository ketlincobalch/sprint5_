import pandas as pd

def process_dataframe(dataframe):
    df = dataframe.copy()
    
    # Ajustar nome das colunas
    df.columns = (
        df.columns
        .str.lower()
        .str.replace('\(%\)', '', regex=True)
        .str.strip()
        .str.replace(' ', '_')
        .str.replace('-', '_')
    )
    
    # Remover valores nulos
    df = df.dropna()
    
    # Salvar o dataframe tratado
    # df.to_csv(r'../data/superstore_clean.csv', index=False)
    
    return df