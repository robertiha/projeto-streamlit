import streamlit as st
import pandas as pd
import datetime
from datetime import date, datetime

def gravar_dados(nome, dt_nasc, sexo, est_civil, cpf, data_cadastro):
    if nome and dt_nasc <= date.today():
        with open('clientes.csv', 'a', encoding='utf-8') as file:
            file.write(f'{nome}, {dt_nasc}, {sexo}, {est_civil}, {cpf}, {data_cadastro}\n')
        st.session_state['Sucesso'] = True
    else:
        st.session_state['Sucesso'] = False

st.set_page_config(
    page_title='Cadastro de clientes',
    page_icon='🪶'
)

st.title('Cadastro de clientes')
st.divider()

# nome
nome = st.text_input('Digite o nome do cliente',
                     key='nome_cliente')

# data minima e maxima
min_date = date(1900, 1, 1)  # usando apenas date, não datetime.date
max_date = date(2100, 12, 31)  # mesmo aqui

# data de nascimento
dt_nasc = st.date_input('Data de nascimento',
                        value=date(2023,1,1),
                        min_value=min_date,
                        max_value=max_date
                        )

# sexo
sexo = st.selectbox('Sexo:',
                    ['F', 'M'])

# estado civil
est_civil = st.selectbox('Estado civil:',
                         ['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)'])

# cpf
cpf = st.text_input('CPF', key='cpf')

# data atual
data_cadastro = datetime.today().date()

# adicionar um input com a data atual como padrão:
data_selecionada = st.date_input('Data de cadastro:', data_cadastro)

# botao para salvar dados
btn_cadastrar = st.button('Cadastrar',
                          on_click=gravar_dados,
                          args=[nome,dt_nasc,sexo,est_civil,cpf,data_cadastro])

# Botão de cadastro
if btn_cadastrar:
    # Verifica se todos os campos foram preenchidos
    if not nome or not cpf:
        st.error("Por favor, preencha todos os campos obrigatórios.")
    else:
        # Mostra a mensagem de sucesso com os dados cadastrados
        st.success(f"Usuário cadastrado com sucesso!")
        st.write("### Dados do Usuário:")
        st.write(f"**Nome:** {nome}")
        st.write(f"**Sexo:** {sexo}")
        st.write(f"**Estado Civil:** {est_civil}")
        st.write(f"**CPF:** {cpf}")
        st.write(f"**Data de Nascimento:** {dt_nasc}")
        st.write(f"**Data de Cadastro:** {data_cadastro}")