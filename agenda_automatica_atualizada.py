import pandas as pd
from datetime import datetime

#path_file = r'C:\\Users\\Usuario\\Desktop\\Python\\licao_de_casa_2 18.05.23\\agenda_automatica_python.xlsx'
path_file = r'C:\\Users\\Usuario\\Desktop\\Python\\licao_de_casa_2 18.05.23\\agenda_automatica_python.xlsx'
agenda_df = pd.read_excel(path_file)
agenda_df_columns = pd.read_excel(path_file, usecols=['Data de Compromisso', 'Compromisso', 'Dinheiro Disponível'])

print('Bem vindo à sua agenda pessoal st4rboy!! Aqui armazenarei seus compromissos e quantidade financeira atual.')
print('O que deseja fazer?')
print('1:Adicionar um compromisso à sua agenda')
print('2.Atualizar um compromisso da sua agenda')
print('3.Deletar um compromisso da sua agenda')
print('4.Pesquisar um compromisso em sua agenda')
opcao_escolhida = int(input('Escolha uma das opções selecionáveis: '))
if opcao_escolhida == 1:
    comp = input(str('Qual será seu próximo compromisso st4rboy?: '))
    #em comp colocar opções: lazer, recurso, comida
    d_comp = input('Escreva a data do compromisso no seguinte parâmetro: %d/%m/%Y  ')
    h_comp = input('Escreva a hora do compromisso no seguinte parâmetro: %H:%M:%S  ')
    din = input ('Insira a atual quantidade de dinheiro armazenada: ')
    h_dalt = str(datetime.now())   
    novo_item = {'Datalog': h_dalt, 'Compromisso': comp, 'Data de Compromisso': d_comp, 'Dinheiro Disponível': din, 'Horário de Compromisso': h_comp}
    novo_df = pd.DataFrame([novo_item])
    agenda_df = pd.concat([agenda_df, novo_df])  
    agenda_df.to_excel(path_file, index=False)

if opcao_escolhida == 2:
    print(agenda_df_columns)
    data = input('Escreva a data do compromisso no seguinte parâmetro: %d/%m/%Y %H:%M:%S:   ')      
    try:
        agenda_df.loc[agenda_df['Data de Compromisso'] == data, 'Data de Compromisso'] = data
        new_data = input('Escreva a nova data do compromisso: ')
        agenda_df.loc[agenda_df['Data de Compromisso'] == data, 'Data de Compromisso'] = new_data
        new_h_dalt = str(datetime.now())   
        new_comp = input('Escreva o compromisso atualizado: ')
        new_din = input('Escreva a quantidade de dinheiro atualizada: ')
        new_h_comp = input('Escreva a nova hora do compromisso: ')
        agenda_df.loc[agenda_df['Data de Compromisso'] == data, 'Datalog'] = new_h_dalt
        agenda_df.loc[agenda_df['Data de Compromisso'] == data, 'Compromisso'] = new_comp
        agenda_df.loc[agenda_df['Data de Compromisso'] == data, 'Dinheiro Disponível'] = new_din
        agenda_df.loc[agenda_df['Data de Compromisso'] == data, 'Horário de Compromisso'] = new_h_comp
        agenda_df.to_excel(path_file, index = False)
    except:
        print('Erro ao localizar a data.')    
if opcao_escolhida == 3:
    try:
        print(agenda_df_columns)   
        data = input('insira a data que deseja excluir da agenda automática: ')
        agenda_df.loc[agenda_df['Data de Compromisso'] == data, 'Data de Compromisso'] = data
        agenda_df = agenda_df[agenda_df['Data de Compromisso']!= data]
        agenda_df.to_excel(path_file, index = False)
    except:
        print('Data inserida não é existente. Tente com outra existente.')
if opcao_escolhida == 4:
    try:       
        print(agenda_df_columns)
        data = input('Em qual data deseja procurar seu compromisso?: ')
        agenda_df.loc[agenda_df['Data de Compromisso'] == data, 'Data de Compromisso'] = data
        linha = agenda_df[agenda_df['Data de Compromisso'] == data]
        print(linha)
    except:
        print('Data inserida não é existente. Tente com outra existente.')
            