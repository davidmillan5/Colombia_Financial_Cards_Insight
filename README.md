# Colombia Financial Cards Insight


The information corresponds to the number of active credit and debit 
cards as of the reporting date, active during the month, canceled and 
blocked, the outstanding loan portfolio balance from purchases and cash 
advances by card network, and the purchases and withdrawals made with debit 
cards at credit institutions.

| Column Name      | API Field Name   | Data Type        | Description |
|------------------|------------------|------------------|-------------|
| TIPOENTIDAD      | tipoentidad      | int              | Numeric code identifying the institutional classification of the reporting entity. Examples include: 01 = Banking institutions supervised by the Superintendencia Financiera de Colombia (SFC); 32 = Financial cooperatives under SFC supervision; 04 = Multi-activity cooperatives without savings and credit section (statistical classification used in solidarity economy datasets, not direct SFC supervision); 118 = Payment networks and electronic payment infrastructure operators (e.g., Credibanco, ACH Colombia, ATH, Redeban). |
| CODIGOENTIDAD    | codigoentidad    | int              | Unique identification code assigned to each reporting entity within regulatory or statistical reporting systems. Used to distinguish financial institutions, cooperatives, or payment operators. |
| NOMBREENTIDAD    | nombreentidad    | str              | Official name of the reporting entity (e.g., bank, cooperative, or payment network). |
| FECHACORTE       | fechacorte       | datetime64[ns]   | Reporting cutoff date for the financial data. Indicates the reference period for card balances, active cards, cancellations, and transaction activity. |
| COD_UCA          | cod_uca          | int              | Code corresponding to the reporting unit or accounting classification structure used for regulatory submissions. Organizes financial metrics within standardized reporting frameworks. |
| NOMBRE_UCA       | nombre_uca       | str              | Name of the reporting or accounting category associated with the UCA code. Provides higher-level grouping of financial metrics. |
| SUBCUENTA        | subcuenta        | int              | Specific sub-account code identifying the financial metric reported (e.g., active cards, cards active during the month, canceled cards, blocked cards, portfolio balance from purchases, cash advances). |
| DESCRIPCION      | descripcion      | str              | Text description explaining the metric represented by the sub-account, including operational definitions such as number of active cards, balance of credit portfolio, or transaction volume. |
| PERSONA_NATURAL  | persona_natural  | int              | Reported value (number of cards or monetary balance) corresponding to individual customers (natural persons). |
| PERSONA_JURIDICA | persona_juridica | int              | Reported value (number of cards or monetary balance) corresponding to corporate customers (legal entities). |
| TOTAL_TARJETAS   | total_tarjetas   | int              | Aggregate total of the metric reported, typically representing the sum of natural and legal persons where applicable. |
