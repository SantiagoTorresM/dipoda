#Dash SIRIES

import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from gsheetsdb import connect

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.

# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(allow_output_mutation=True, max_entries=50, ttl=3600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows


st.set_page_config(layout="wide")
alt.data_transformers.disable_max_rows()

'''
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
'''
# minedu0 = st.image('https://upload.wikimedia.org/wikipedia/commons/2/21/Logo_del_Ministerio_de_Educaci%C3%B3n_del_Per%C3%BA_-_MINEDU.png')
minedu1 = st.sidebar.image('https://upload.wikimedia.org/wikipedia/commons/2/21/Logo_del_Ministerio_de_Educaci%C3%B3n_del_Per%C3%BA_-_MINEDU.png')

st.sidebar.markdown("## Seleccione el fichero y los atributos principales")

periodicidad = st.sidebar.selectbox(
    "Elija la periodicidad",
    ('Anual', 'Semestral')
)

#ruta = 'D:/OneDrive - Universidad Adolfo Ibanez/python learn/streamlit/'
#Matriculados = pd.read_excel(ruta + 'Matriculados_' + periodicidad + '.xlsx', sheet_name='Sheet1')
#Postulantes = pd.read_excel(ruta + 'Postulantes_' + periodicidad + '.xlsx', sheet_name='Sheet1')
#Ingresantes = pd.read_excel(ruta + 'Ingresantes_' + periodicidad + '.xlsx', sheet_name='Sheet1')
#Egresados = pd.read_excel(ruta + 'Egresados_' + periodicidad + '.xlsx', sheet_name='Sheet1')

#Se importa la data vía google sheets
sheet_url_Matriculados = st.secrets["Matriculados_" + periodicidad + "_url"]
Matriculados_rows = run_query(f'SELECT * FROM "{sheet_url_Matriculados}"')
Matriculados = pd.DataFrame(Matriculados_rows)

sheet_url_Postulantes = st.secrets["Postulantes_" + periodicidad + "_url"]
Postulantes_rows = run_query(f'SELECT * FROM "{sheet_url_Postulantes}"')
Postulantes = pd.DataFrame(Postulantes_rows)

sheet_url_Ingresantes = st.secrets["Ingresantes_" + periodicidad + "_url"]
Ingresantes_rows = run_query(f'SELECT * FROM "{sheet_url_Ingresantes}"')
Ingresantes = pd.DataFrame(Ingresantes_rows)

sheet_url_Egresados = st.secrets["Egresados_" + periodicidad + "_url"]
Egresados_rows = run_query(f'SELECT * FROM "{sheet_url_Egresados}"')
Egresados = pd.DataFrame(Egresados_rows)


##
if periodicidad == 'Anual':
    Matriculados.columns = ["Código Modular", "Universidad", "Gestión", "Estatus de licenciamiento", "Modalidad Jurídica", "Departamento" , "Código de Campo de Educación INEI 2014", "Campo de Educación INEI 2014", "Código de Campo Detallado INEI 2014", "Campo Detallado INEI 2014", "Sexo", "2017", "2018", "2019", "2020", "2021"]
    Postulantes.columns = ["Código Modular", "Universidad", "Gestión", "Estatus de licenciamiento", "Modalidad Jurídica", "Departamento" , "Código de Campo de Educación INEI 2014", "Campo de Educación INEI 2014", "Código de Campo Detallado INEI 2014", "Campo Detallado INEI 2014", "Sexo", "2017", "2018", "2019", "2020", "2021"]
    Ingresantes.columns = ["Código Modular", "Universidad", "Gestión", "Estatus de licenciamiento", "Modalidad Jurídica", "Departamento" , "Código de Campo de Educación INEI 2014", "Campo de Educación INEI 2014", "Código de Campo Detallado INEI 2014", "Campo Detallado INEI 2014", "Sexo", "2017", "2018", "2019", "2020", "2021"]
    Egresados.columns = ["Código Modular", "Universidad", "Gestión", "Estatus de licenciamiento", "Modalidad Jurídica", "Departamento" , "Código de Campo de Educación INEI 2014", "Campo de Educación INEI 2014", "Código de Campo Detallado INEI 2014", "Campo Detallado INEI 2014", "Sexo", "2017", "2018", "2019", "2020", "2021"]
if periodicidad == 'Semestral':
    Matriculados.columns = ["Código Modular", "Universidad", "Gestión", "Estatus de licenciamiento", "Modalidad Jurídica", "Departamento" , "Código de Campo de Educación INEI 2014", "Campo de Educación INEI 2014", "Código de Campo Detallado INEI 2014", "Campo Detallado INEI 2014", "Sexo", "2017-1", "2017-2", "2018-1", "2018-2", "2019-1", "2019-2", "2020-1", "2020-2", "2020-3", "2021-1", "2021-2"]
    Postulantes.columns = ["Código Modular", "Universidad", "Gestión", "Estatus de licenciamiento", "Modalidad Jurídica", "Departamento" , "Código de Campo de Educación INEI 2014", "Campo de Educación INEI 2014", "Código de Campo Detallado INEI 2014", "Campo Detallado INEI 2014", "Sexo", "2017-1", "2017-2", "2018-1", "2018-2", "2019-1", "2019-2", "2020-1", "2020-2", "2021-1", "2021-2"]
    Ingresantes.columns = ["Código Modular", "Universidad", "Gestión", "Estatus de licenciamiento", "Modalidad Jurídica", "Departamento" , "Código de Campo de Educación INEI 2014", "Campo de Educación INEI 2014", "Código de Campo Detallado INEI 2014", "Campo Detallado INEI 2014", "Sexo", "2017-1", "2017-2", "2018-1", "2018-2", "2019-1", "2019-2", "2020-1", "2020-2", "2021-1", "2021-2"]
    Egresados.columns = ["Código Modular", "Universidad", "Gestión", "Estatus de licenciamiento", "Modalidad Jurídica", "Departamento" , "Código de Campo de Educación INEI 2014", "Campo de Educación INEI 2014", "Código de Campo Detallado INEI 2014", "Campo Detallado INEI 2014", "Sexo", "2017-1", "2017-2", "2018-1", "2018-2", "2019-1", "2019-2", "2020-1", "2020-2", "2021-1"]
##

llave = ['Código Modular', 'Universidad', 'Gestión', 'Estatus de licenciamiento', 
         'Modalidad Jurídica', 'Departamento', 'Código de Campo de Educación INEI 2014', 
         'Campo de Educación INEI 2014', 'Código de Campo Detallado INEI 2014', 
         'Campo Detallado INEI 2014', 'Sexo']

Matriculados = Matriculados.melt(id_vars=llave, var_name="periodo")
Postulantes = Postulantes.melt(id_vars=llave, var_name="periodo")
Ingresantes = Ingresantes.melt(id_vars=llave, var_name="periodo")
Egresados = Egresados.melt(id_vars=llave, var_name="periodo")

##Crea etiqueta univ y reshape
for x in [Matriculados, Postulantes, Ingresantes, Egresados]:
    x['Universidad'] = x['Universidad'].str.replace('UTEC', 'UNIVERSIDAD DE INGENIERÍA Y TECNOLOGÍA')
    x['Universidad'] = x['Universidad'].str.replace('UNIVERSIDAD NACIONAL', 'U.N.')
    x['Universidad'] = x['Universidad'].str.replace('UNIVERSIDAD', 'U.')
    x['Universidad'] = x['Universidad'].str.replace('PONTIFICIA U.', 'PONTIFICIA UNIVERSIDAD')
    x['value'] = x['value'].astype('int')
    x['Código Modular'] = x['Código Modular'].astype('str')
    x['periodo'] = x['periodo'].astype('str')
    x['periodo'] = np.where(x['periodo'] == '2021', '2021 p/', x['periodo'])
    x['periodo'] = np.where(x['periodo'] == '2021-1', '2021-1 p/', x['periodo'])
    x['periodo'] = np.where(x['periodo'] == '2021-2', '2021-2 p/', x['periodo'])
    x['periodo'] = np.where(x['periodo'] == '2021-A', '2021-A p/', x['periodo'])

##Segunda fase: sidebar
##Tercera fase: widgets
fichero = st.sidebar.selectbox(
    "Elija el tipo de fichero",
    ('Matriculados', 'Postulantes', 'Ingresantes', 'Egresados')
)

dictfichero = {'Matriculados': Matriculados, 'Postulantes': Postulantes, 'Ingresantes': Ingresantes, 'Egresados': Egresados}

data = dictfichero[fichero]

data['Total Nacional'] = 'Total'

year = st.sidebar.selectbox(
    'Elija el periodo', data['periodo'].unique()
    )
data0 = data[data['periodo'] == year]

estatus = st.sidebar.multiselect(
    'Elija el Estatus de licenciamiento', data['Estatus de licenciamiento'].unique(), data['Estatus de licenciamiento'].unique()
    ) 
data1 = data0[(data['Estatus de licenciamiento']).isin(estatus)]

gestion = st.sidebar.multiselect(
    'Elija el tipo de gestión', data1['Gestión'].unique(), data1['Gestión'].unique()
    ) 
data2 = data1[(data1['Gestión']).isin(gestion)]

sexo = st.sidebar.multiselect(
    'Elija el sexo', data2['Sexo'].unique(), data2['Sexo'].unique()
    ) 
data3 = data2[(data2['Sexo']).isin(sexo)]

familia = st.sidebar.multiselect(
    'Elija el campo de educación', data3['Campo de Educación INEI 2014'].unique(), data3['Campo de Educación INEI 2014'].unique()
    ) 
data4 = data3[(data3['Campo de Educación INEI 2014']).isin(familia)]

dpto = st.sidebar.multiselect(
    'Elija el departamento', data4['Departamento'].unique(), data4['Departamento'].unique()
    ) 
data5 = data4[(data4['Departamento']).isin(dpto)]

universidad = st.sidebar.multiselect(
    'Elija la universidad', data5['Universidad'].unique(), data5['Universidad'].unique()  
    ) 
data6 = data5[(data5['Universidad']).isin(universidad)]

##Procesamiento con filtros

#Título del dash
per = {'Anual': 'Año', 'Semestral': 'Semestre'}

st.title('Estadísticas de Educación Superior Universitaria')
st.header('Fichero ' + fichero + ', ' + per[periodicidad] + ' ' + str(year))

st.text('Esta información ha sido procesada a través del Sistema de Recolección de Información para la Educación Superior - SIRIES con fecha de corte al 27 de junio de 2021.')
st.text('Exclusivo para uso interno de la Dirección. Elaborado por el equipo de Estadísticas y Estudios de la DIPODA. Responsable: Santiago Torres Manrique (datorres@minedu.gob.pe)')


st.markdown("<h1 style='text-align: center; color: black;'>--------Nacional--------</h1>", unsafe_allow_html=True)

st.header('Cifras generales ' + str(year))

r0c1, r0c2, r0c3, r0c4, r0c5, r0c6, r0c7 = st.beta_columns((1,1 ,1,1,1,1,1))

with r0c1:
    
    st.markdown(f'''<div class="card text-white bg-primary mb-3" style="width: 18rem">
                <div class="card-body">
                   <h5 class="card-title">NACIONAL</h5>
                   <p class="card-text">{sum(data0['value']):,d}</p>
                </div>
            </div>''', unsafe_allow_html=True)

with r0c2:
    
    st.markdown(f'''<div class="card text-white bg-secondary mb-3" style="width: 18rem">
                <div class="card-body">
                   <h5 class="card-title">PÚBLICAS</h5>
                   <p class="card-text">{sum(data0['value'][data0['Gestión'] == 'Pública']):,d}</p>
                </div>
            </div>''', unsafe_allow_html=True)

with r0c3:
    
    st.markdown(f'''<div class="card text-white bg-success mb-3" style="width: 18rem">
                      <div class="card-body">
                        <h5 class="card-title">PRIVADAS</h5>
                        <p class="card-text">{sum(data0['value'][data0['Gestión'] == 'Privada']):,d}</p>
                      </div>
                    </div>''', unsafe_allow_html=True)

with r0c4:
    
    st.markdown(f'''<div class="card text-white bg-danger mb-3" style="width: 18rem">
                <div class="card-body">
                   <h5 class="card-title">LICENCIADAS</h5>
                   <p class="card-text">{sum(data0['value'][data0['Estatus de licenciamiento'] == 'Licenciada']):,d}</p>
                </div>
            </div>''', unsafe_allow_html=True)

with r0c5:
    
    st.markdown(f'''<div class="card text-white bg-dark mb-3" style="width: 18rem">
                <div class="card-body">
                   <h5 class="card-title">LICENCIA DENEGADA</h5>
                   <p class="card-text">{sum(data0['value'][data0['Estatus de licenciamiento'] == 'Licencia denegada']):,d}</p>
                </div>
            </div>''', unsafe_allow_html=True)

with r0c6:
    
    st.markdown(f'''<div class="card text-white bg-dark mb-3" style="width: 18rem">
                <div class="card-body">
                   <h5 class="card-title">MUJER</h5>
                   <p class="card-text">{sum(data0['value'][data0['Sexo'] == 'FEMENINO']):,d}</p>
                </div>
            </div>''', unsafe_allow_html=True)

with r0c7:
    
    st.markdown(f'''<div class="card text-white bg-dark mb-3" style="width: 18rem">
                <div class="card-body">
                   <h5 class="card-title">HOMBRE</h5>
                   <p class="card-text">{sum(data0['value'][data0['Sexo'] == 'MASCULINO']):,d}</p>
                </div>
            </div>''', unsafe_allow_html=True)

#Paletas de colores para barras
domain_gestion = ['Privada', 'Pública']
range_gestion = ['purple', 'lightblue']

domain_estatus = ['Licencia denegada', 'Licenciada']
range_estatus = ['red', 'green']

domain_sexo = ['FEMENINO', 'MASCULINO']
range_sexo = ['turquoise', 'brown']


st.header('Serie histórica 2017-2021 p/')

r0c1, r0c2 = st.beta_columns((1,1))

with r0c1:
    st.subheader('Total')
    bars = alt.Chart(data[data.periodo != '2020-3']).mark_bar().encode(
        y=alt.Y('sum(value):Q', stack='zero', axis=alt.Axis(title='N° de ' + fichero)), 
        x=alt.X('periodo:N', axis=alt.Axis(title=per[periodicidad]))
        )
    text = bars.mark_text(dx=0, dy=-15, color='black').encode(
        y=alt.Y('sum(value):Q', stack='zero'),
        x=alt.X('periodo:N'),
        # detail='Gestión:N',
        text=alt.Text('sum(value):Q')
    )
    tot = (bars + text).properties().configure_axis(grid=False).configure_view(strokeWidth=0)
    st.altair_chart(tot, use_container_width=True)

with r0c2:
    st.subheader('Según gestión')
    bars = alt.Chart(data[data.periodo != '2020-3']).mark_bar().encode(
        y=alt.Y('sum(value):Q', stack='zero', axis=alt.Axis(title='N° de ' + fichero)), 
        x=alt.X('periodo:N', axis=alt.Axis(title=per[periodicidad])), 
        color=alt.Color('Gestión', scale=alt.Scale(domain=domain_gestion, range=range_gestion))
        )
    text = bars.mark_text(dx=0, dy=-10, color='black').encode(
        y=alt.Y('sum(value):Q', stack='zero'),
        x=alt.X('periodo:N'),
        detail='Gestión:N',
        text=alt.Text('sum(value):Q')
    )
    tot = (bars + text).properties().configure_legend(
        orient='bottom'
        ).configure_axis(grid=False).configure_view(strokeWidth=0)
    st.altair_chart(tot, use_container_width=True)

r0c3, r0c4 = st.beta_columns((1,1))

with r0c3:
    st.subheader('Según Estatus de licenciamiento')
    bars = alt.Chart(data[data.periodo != '2020-3']).mark_bar().encode(
        y=alt.Y('sum(value):Q', stack='zero', axis=alt.Axis(title='N° de ' + fichero)), 
        x=alt.X('periodo:N', axis=alt.Axis(title=per[periodicidad])), 
        color=alt.Color('Estatus de licenciamiento', scale=alt.Scale(domain=domain_estatus, range=range_estatus))
        )
    text = bars.mark_text(dx=0, dy=-10, color='black').encode(
        y=alt.Y('sum(value):Q', stack='zero'),
        x=alt.X('periodo:N'),
        detail='Estatus de licenciamiento:N',
        text=alt.Text('sum(value):Q')
    )
    tot = (bars + text).properties().configure_legend(
        orient='bottom'
        ).configure_axis(grid=False).configure_view(strokeWidth=0)
    st.altair_chart(tot, use_container_width=True)

with r0c4:
    st.subheader('Según sexo')
    bars = alt.Chart(data[data.periodo != '2020-3']).mark_bar().encode(
        y=alt.Y('sum(value):Q', stack='zero', axis=alt.Axis(title='N° de ' + fichero)), 
        x=alt.X('periodo:N', axis=alt.Axis(title=per[periodicidad])), 
        color=alt.Color('Sexo', scale=alt.Scale(domain=domain_sexo, range=range_sexo))
        )
    text = bars.mark_text(dx=0, dy=-10, color='black').encode(
        y=alt.Y('sum(value):Q', stack='zero'),
        x=alt.X('periodo:N'),
        detail='Sexo:N',
        text=alt.Text('sum(value):Q')
    )
    tot = (bars + text).properties().configure_legend(
        orient='bottom'
        ).configure_axis(grid=False).configure_view(strokeWidth=0)
    st.altair_chart(tot, use_container_width=True)

with st.beta_expander("VER TABLAS NACIONALES HISTÓRICAS"):
    peru1 = pd.crosstab(
        index = data['periodo'], 
        columns = data['Gestión'], values=data['value'], aggfunc=np.sum, margins = True, margins_name='Total' )
    peru1=peru1.replace(np.nan, 0).astype('int')
    peru1=peru1.reset_index()
    
    peru2 = pd.crosstab(
        index = data['periodo'], 
        columns = data['Estatus de licenciamiento'], values=data['value'], aggfunc=np.sum, margins = True, margins_name='Total')
    peru2=peru2.replace(np.nan, 0).astype('int')
    peru2=peru2.reset_index()
    
    peru3 = pd.crosstab(
        index = data['periodo'], 
        columns = data['Sexo'], values=data['value'], aggfunc=np.sum, margins = True, margins_name='Total')
    peru3=peru3.replace(np.nan, 0).astype('int')
    peru3=peru3.reset_index()

    
    t0c1, t0c2, t0c3 = st.beta_columns((1,1,1))
    with t0c1: 
        st.subheader('Tabla: ' + fichero + ' por gestión, 2017-2021')
        st.table(peru1)
    with t0c2: 
        st.subheader('Tabla: ' + fichero + ' por estatus de licenciamiento, 2017-2021')
        st.table(peru2)
    with t0c3: 
        st.subheader('Tabla: ' + fichero + ' por sexo, según campo detallado, 2017-2021')
        st.table(peru3)    


st.markdown("<h1 style='text-align: center; color: black;'>--------Según filtros--------</h1>", unsafe_allow_html=True)

st.subheader('1. GENERAL')

r1c1, r1c2 = st.beta_columns((1,1))

with r1c1:
    st.subheader('1A. Total')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y='Total Nacional'
        )
    text = bars.mark_text(
        align='left', 
        baseline='middle', 
        dx=-50, 
        color='white'
        ).encode(
            text='sum(value):Q'
            )
    tot = (bars + text).properties()
    st.altair_chart(tot, use_container_width=True)

with r1c2:
    st.subheader('1B. Según gestión')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y='Total Nacional', 
        color=alt.Color("Gestión:N", scale=alt.Scale(domain=domain_gestion, range=range_gestion))
        ).configure_legend(
        orient='bottom'
        )
    st.altair_chart(bars, use_container_width=True)

r1c3, r1c4 = st.beta_columns((1,1))

with r1c3:
    st.subheader('1C. Según Estatus de licenciamiento')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y='Total Nacional', 
        color=alt.Color("Estatus de licenciamiento:N", scale=alt.Scale(domain=domain_estatus, range=range_estatus))
        ).configure_legend(
        orient='bottom'
        )
    st.altair_chart(bars, use_container_width=True)

with r1c4:
    st.subheader('1D. Según sexo')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y='Total Nacional', 
        color=alt.Color("Sexo:N", scale=alt.Scale(domain=domain_sexo, range=range_sexo))
        ).configure_legend(
        orient='bottom')
    st.altair_chart(bars, use_container_width=True)


with st.beta_expander("VER TABLAS 1"):
    ###
    total1 = pd.crosstab(
        index = data6['Total Nacional'], 
        columns = data6['Gestión'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total general' )
    total1=total1.replace(np.nan, 0).astype('int')
    total1=total1.reset_index()
    total1=total1[0:1]
    
    total2 = pd.crosstab(
        index = data6['Total Nacional'], 
        columns = data6['Estatus de licenciamiento'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total general')
    total2=total2.replace(np.nan, 0).astype('int')
    total2=total2.reset_index()
    total2=total2[0:1]
    
    total3 = pd.crosstab(
        index = data6['Total Nacional'], 
        columns = data6['Sexo'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total general')
    total3=total3.replace(np.nan, 0).astype('int')
    total3=total3.reset_index()
    total3=total3[0:1]

    t1c1, t1c2, t1c3 = st.beta_columns((1,1,1))
    with t1c1: 
        st.subheader('Tabla: ' + fichero + ' por gestión, ' + str(year))
        st.table(total1)
    with t1c2: 
        st.subheader('Tabla: ' + fichero + ' por estatus de licenciamiento, ' + str(year))
        st.table(total2)
    with t1c3: 
        st.subheader('Tabla: ' + fichero + ' por sexo, ' + str(year))
        st.table(total3)

st.subheader('2. POR DEPARTAMENTO')

r2c1, r2c2 = st.beta_columns((1,1))

with r2c1:
    st.subheader('2A. Total')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Departamento', sort = '-x')
        )
    text = bars.mark_text(
        align='left', 
        baseline='middle', 
        dx=3  # Nudges text to right so it doesn't appear on top of the bar
        ).encode(
            text='sum(value):Q'
            )
    tot = (bars + text).properties()
    st.altair_chart(tot, use_container_width=True)

with r2c2:
    st.subheader('2B. Según gestión')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Departamento', sort = '-x'), 
        color=alt.Color("Gestión:N", scale=alt.Scale(domain=domain_gestion, range=range_gestion))
        ).configure_legend(
        orient='bottom'
        )
    st.altair_chart(bars, use_container_width=True)

r2c3, r2c4 = st.beta_columns((1,1))

with r2c3:
    st.subheader('2C. Según Estatus de licenciamiento')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Departamento', sort = '-x'), 
        color=alt.Color("Estatus de licenciamiento:N", scale=alt.Scale(domain=domain_estatus, range=range_estatus))
        ).configure_legend(
        orient='bottom'
        )
    st.altair_chart(bars, use_container_width=True)

with r2c4:
    st.subheader('2D. Según sexo')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Departamento', sort = '-x'), 
        color=alt.Color("Sexo:N", scale=alt.Scale(domain=domain_sexo, range=range_sexo))
        ).configure_legend(
        orient='bottom'
        )
    st.altair_chart(bars, use_container_width=True)

# Botón para desplegar tabla 2
with st.beta_expander("VER TABLAS 2"):
    ###
    departamento1 = pd.crosstab(
        index = data6['Departamento'], 
        columns = data6['Gestión'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total' )
    departamento1=departamento1.replace(np.nan, 0).astype('int')
    departamento1=departamento1.reset_index()
    
    departamento2 = pd.crosstab(
        index = data6['Departamento'], 
        columns = data6['Estatus de licenciamiento'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total')
    departamento2=departamento2.replace(np.nan, 0).astype('int')
    departamento2=departamento2.reset_index()
    
    departamento3 = pd.crosstab(
        index = data6['Departamento'], 
        columns = data6['Sexo'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total')
    departamento3=departamento3.replace(np.nan, 0).astype('int')
    departamento3=departamento3.reset_index()

    t2c1, t2c2, t2c3 = st.beta_columns((1,1,1))
    with t2c1: 
        st.subheader('Tabla: ' + fichero + ' por gestión, según departamento, ' + str(year))
        st.table(departamento1)
    with t2c2: 
        st.subheader('Tabla: ' + fichero + ' por estatus de licenciamiento, según departamento, ' + str(year))
        st.table(departamento2)
    with t2c3: 
        st.subheader('Tabla: ' + fichero + ' por sexo, según departamento, ' + str(year))
        st.table(departamento3)


####
####
st.subheader('3. POR CAMPO DE EDUCACIÓN')

r3c1, r3c2 = st.beta_columns((1,1))

with r3c1:
    st.subheader('3A. Total')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Campo de Educación INEI 2014', sort = '-x')
        )
    text = bars.mark_text(
        align='left', 
        baseline='middle', 
        dx=3  # Nudges text to right so it doesn't appear on top of the bar
        ).encode(
            text='sum(value):Q'
            )
    tot = (bars + text).properties()
    st.altair_chart(tot, use_container_width=True)

with r3c2:
    st.subheader('3B. Según gestión')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Campo de Educación INEI 2014', sort = '-x'), 
        color=alt.Color("Gestión:N", scale=alt.Scale(domain=domain_gestion, range=range_gestion))
        ).configure_legend(
        orient='bottom'
        )
    st.altair_chart(bars, use_container_width=True)

r3c3, r3c4 = st.beta_columns((1,1))

with r3c3:
    st.subheader('3C. Según Estatus de licenciamiento')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Campo de Educación INEI 2014', sort = '-x'), 
        color=alt.Color("Estatus de licenciamiento:N", scale=alt.Scale(domain=domain_estatus, range=range_estatus))
        ).configure_legend(
        orient='bottom'
        )
    st.altair_chart(bars, use_container_width=True)

with r3c4:
    st.subheader('3D. Según sexo')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Campo de Educación INEI 2014', sort = '-x'), 
        color=alt.Color("Sexo:N", scale=alt.Scale(domain=domain_sexo, range=range_sexo))
        ).configure_legend(
        orient='bottom'
        )
    st.altair_chart(bars, use_container_width=True)

# Botón para desplegar tabla 3
with st.beta_expander("VER TABLAS 3"):
    ###
    familia1 = pd.crosstab(
        index = data6['Campo de Educación INEI 2014'], 
        columns = data6['Gestión'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total' )
    familia1=familia1.replace(np.nan, 0).astype('int')
    familia1=familia1.reset_index()
    
    familia2 = pd.crosstab(
        index = data6['Campo de Educación INEI 2014'], 
        columns = data6['Estatus de licenciamiento'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total')
    familia2=familia2.replace(np.nan, 0).astype('int')
    familia2=familia2.reset_index()
    
    familia3 = pd.crosstab(
        index = data6['Campo de Educación INEI 2014'], 
        columns = data6['Sexo'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total')
    familia3=familia3.replace(np.nan, 0).astype('int')
    familia3=familia3.reset_index()

    t3c1, t3c2, t3c3 = st.beta_columns((1,1,1))
    with t3c1: 
        st.subheader('Tabla: ' + fichero + ' por gestión, según campo de educación, ' + str(year))
        st.table(familia1)
    with t3c2: 
        st.subheader('Tabla: ' + fichero + ' por estatus de licenciamiento, según campo de educación, ' + str(year))
        st.table(familia2)
    with t3c3: 
        st.subheader('Tabla: ' + fichero + ' por sexo, según campo de educación, ' + str(year))
        st.table(familia3)


####
####
st.subheader('4. POR CAMPO DETALLADO')

r4c1, r4c2 = st.beta_columns((1,1))

with r4c1:
    st.subheader('4A. Total')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Campo Detallado INEI 2014', sort = '-x')
        ).properties()
    text = bars.mark_text(
        align='left', 
        baseline='middle', 
        dx=3  # Nudges text to right so it doesn't appear on top of the bar
        ).encode(
            text='sum(value):Q'
            )
    tot = (bars + text)
    st.altair_chart(tot, use_container_width=True)

with r4c2:
    st.subheader('4B. Según gestión')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Campo Detallado INEI 2014', sort = '-x'), 
        color=alt.Color("Gestión:N", scale=alt.Scale(domain=domain_gestion, range=range_gestion))
        ).configure_legend(
        orient='bottom'
        ).properties()
    st.altair_chart(bars, use_container_width=True)

r4c3, r4c4 = st.beta_columns((1,1))

with r4c3:
    st.subheader('4C. Según Estatus de licenciamiento')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Campo Detallado INEI 2014', sort = '-x'), 
        color=alt.Color("Estatus de licenciamiento:N", scale=alt.Scale(domain=domain_estatus, range=range_estatus))
        ).configure_legend(
        orient='bottom'
        ).properties()
    st.altair_chart(bars, use_container_width=True)

with r4c4:
    st.subheader('4D. Según sexo')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Campo Detallado INEI 2014', sort = '-x'), 
        color=alt.Color("Sexo:N", scale=alt.Scale(domain=domain_sexo, range=range_sexo))
        ).configure_legend(
        orient='bottom'
        ).properties()
    st.altair_chart(bars, use_container_width=True)

# Botón para desplegar tabla 4
with st.beta_expander("VER TABLAS 4"):
    ####
    carrera1 = pd.crosstab(
        index = [data6['Campo de Educación INEI 2014'], data6['Campo Detallado INEI 2014']], 
        columns = data6['Gestión'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total' )
    carrera1=carrera1.replace(np.nan, 0).astype('int')
    carrera1=carrera1.reset_index()
    
    carrera2 = pd.crosstab(
        index = [data6['Campo de Educación INEI 2014'], data6['Campo Detallado INEI 2014']], 
        columns = data6['Estatus de licenciamiento'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total')
    carrera2=carrera2.replace(np.nan, 0).astype('int')
    carrera2=carrera2.reset_index()
    
    carrera3 = pd.crosstab(
        index = [data6['Campo de Educación INEI 2014'], data6['Campo Detallado INEI 2014']], 
        columns = data6['Sexo'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total')
    carrera3=carrera3.replace(np.nan, 0).astype('int')
    carrera3=carrera3.reset_index()

    
    t4c1, t4c2 = st.beta_columns((1,1))
    with t4c1: 
        st.subheader('Tabla: ' + fichero + ' por gestión, según campo detallado, ' + str(year))
        st.table(carrera1)
    with t4c2: 
        st.subheader('Tabla: ' + fichero + ' por estatus de licenciamiento, según campo detallado, ' + str(year))
        st.table(carrera2)

    t4c3, t4c4 = st.beta_columns((1,1))
    with t4c3: 
        st.subheader('Tabla: ' + fichero + ' por sexo, según campo detallado, ' + str(year))
        st.table(carrera3)
    with t4c4: 
        st.subheader('')



####
####
st.subheader('5. POR UNIVERSIDAD')

r5c1, r5c2 = st.beta_columns((1,1))

with r5c1:
    st.subheader('5A. Total')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Universidad', sort='-x') 
        )
    text = bars.mark_text(
        align='left', 
        baseline='middle', 
        dx=3  # Nudges text to right so it doesn't appear on top of the bar
        ).encode(
            text='sum(value):Q'
            )
    tot = (bars + text).properties()

    st.altair_chart(tot, use_container_width=True)


with r5c2:
    st.subheader('5B. Según gestión')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Universidad', sort='-x'), 
        color = alt.Color('Gestión:N', scale=alt.Scale(domain=domain_gestion, range=range_gestion)) 
        )
    text = bars.mark_text(
        align='left', 
        baseline='middle', 
        dx=3  # Nudges text to right so it doesn't appear on top of the bar
        ).encode(
            text='sum(value):Q'
            )
    tot = (bars + text).configure_legend(
        orient='bottom'
        ).properties()

    st.altair_chart(tot, use_container_width=True)


r5c3, r5c4 = st.beta_columns((1,1))

with r5c3:
    st.subheader('5C. Según Estatus de licenciamiento')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Universidad', sort='-x'), 
        color = alt.Color('Estatus de licenciamiento:N', scale=alt.Scale(domain=domain_estatus, range=range_estatus)) 
        )
    text = bars.mark_text(
        align='left', 
        baseline='middle', 
        dx=3  # Nudges text to right so it doesn't appear on top of the bar
        ).encode(
            text='sum(value):Q'
            )
    tot = (bars + text).configure_legend(
        orient='bottom'
        ).properties()

    st.altair_chart(tot, use_container_width=True)


with r5c4:
    st.subheader('5D. Según sexo')
    bars = alt.Chart(data6).mark_bar().encode(
        x=alt.X("sum(value):Q", axis=alt.Axis(title='N° de ' + fichero)), y=alt.Y('Universidad', sort = '-x'), 
        color=alt.Color("Sexo:N", scale=alt.Scale(domain=domain_sexo, range=range_sexo))
        ).configure_legend(
        orient='bottom'
        ).properties()
    st.altair_chart(bars, use_container_width=True)

# Botón para desplegar tabla 5
with st.beta_expander("VER TABLAS 5"):
    ###
    universidad = pd.crosstab(
        index = [data6['Código Modular'], data6['Universidad'], data6['Gestión'], data6['Estatus de licenciamiento'], data6['Departamento']], 
        columns = data6['Sexo'], values=data6['value'], aggfunc=np.sum, margins = True, margins_name='Total')
    universidad=universidad.replace(np.nan,0).astype('int')
    universidad=universidad.reset_index()
    
    st.subheader('Tabla: ' + fichero + ' por sexo, según universidad y departamento, ' + str(year))
    st.table(universidad)
