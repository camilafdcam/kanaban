


# df salobo
df_geral_sa = pd.read_excel(
    io = './data_sheets/KANBAN_.xlsx', # endereço do arquivo
    index_col=0, # referência inicial para contagem de coluna 
    #dtype=, # tipo de leitura de dados str
    engine='openpyxl', # biblioteca para leitura excel
    sheet_name='OUTUBRO',
    usecols='A:E', # delimitação de colunas
    nrows=4400 # delimitação de linhas
)


if  fMenu == 'Projeção mensal':
    st.title('Projeção mensal - Outubro 2024')
    
        # Adiciona um multiselect na aba "Entregas"
    proj_options = st.multiselect(
        'Selecione as projeções mensais:', 
        ['S11D', 'Carajás','Salobo'],
        default=[]  # Opção padrão selecionada
    )



# Exibe a descrição das opções selecionadas
    if proj_options:
        st.write(f"Descrição: {', '.join(proj_options)}")

        # Verifica se a opção 'salobo' foi selecionada
        if 'Salobo' in delivery_options:
            st.dataframe(df_geral_sa)
           
