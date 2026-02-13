# Import pandas
import pandas as pd

# charge source file
data = './data/Tarjetas_de_crédito_y_débito_20260213.csv'

# create DataFrame
tarjetas = pd.read_csv(data)

# Show all rows
pd.set_option('display.max_rows', None)

# Show all columns
pd.set_option('display.max_columns', None)

# Prevent column width truncation
pd.set_option('display.max_colwidth', None)

# Prevent line wrapping (optional but useful)
pd.set_option('display.width', None)

# verify DataFrame
print(tarjetas.head())

# Verify the datatypes on each column

print(tarjetas.dtypes)

# data type convertion and cleaning
tarjetas['FECHACORTE'] = pd.to_datetime(
    tarjetas['FECHACORTE'],
    format='%d/%m/%Y'
)



print(tarjetas.dtypes)

### Present Basic info about the DataFrame

print(tarjetas.head())
print(tarjetas.dtypes)
print(tarjetas.columns)
print(tarjetas.shape)

import pandas as pd

cols = ['PERSONA_NATURAL', 'PERSONA_JURIDICA', 'TOTAL_TARJETAS']

for col in cols:
    tarjetas[col] = (
        tarjetas[col]
        .str.replace(',', '', regex=False)  # remove thousands separator
    )

    tarjetas[col] = pd.to_numeric(tarjetas[col], errors='coerce')

# Create a new DataFrame based on specific criteria

bancolombia_visa_2025 = tarjetas[
    (tarjetas['NOMBREENTIDAD'] == 'BANCOLOMBIA S.A.') &
    (tarjetas['NOMBRE_UCA'] == 'CREDIBANCO-VISA') &
    (tarjetas['FECHACORTE'].dt.year == 2025) &
    (tarjetas['SUBCUENTA'] == 35)
]

bancolombia_visa_2025 = tarjetas[
    (tarjetas['NOMBREENTIDAD'] == 'BANCOLOMBIA S.A.') &
    (tarjetas['NOMBRE_UCA'] == 'CREDIBANCO-VISA') &
    (tarjetas['FECHACORTE'].dt.year == 2025)]


print(bancolombia_visa_2025.sort_values(by='SUBCUENTA'))




#print(bancolombia_visa_2025[['PERSONA_NATURAL', 'PERSONA_JURIDICA', 'TOTAL_TARJETAS']].sum())

summary_df = (
    tarjetas.loc[(tarjetas['NOMBREENTIDAD'].isin(['BANCOLOMBIA S.A.', 'BANCO DAVIVIENDA S.A.', 'BANCO DE BOGOTA S. A.', 'BANCO BILBAO VIZCAYA ARGENTARIA COLOMBIA S.A. BBVA COLOMBIA'])) &
    (tarjetas['NOMBRE_UCA'] == 'CREDIBANCO-VISA') &
    (tarjetas['FECHACORTE'].dt.year == 2025) &
    (tarjetas['SUBCUENTA'] == 55)]
    .groupby(
        ['TIPOENTIDAD','NOMBREENTIDAD', 'NOMBRE_UCA', 'SUBCUENTA'],
        as_index=False
    )[[
        'PERSONA_NATURAL',
        'PERSONA_JURIDICA',
        'TOTAL_TARJETAS'
    ]]
    .sum()
)

summary_df['FECHACORTE'] = '2025'

print(summary_df)