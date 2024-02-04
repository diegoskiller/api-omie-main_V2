import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from sqlalchemy import create_engine
import pandas as pd

# CONEXÃO COM O BANCO
db_url = "mysql+pymysql://root:HAb3c4gFCF2GdDbGaf11C5GC5E2E15Cf@viaduct.proxy.rlwy.net:47783/railway"
engine = create_engine(db_url)

# FAZ A CONSULTA NO BANCO PARA A TABELA estrutura_op
sql_query_estrutura_op = "SELECT * FROM estrutura_op"
df_estrutura_op = pd.read_sql(sql_query_estrutura_op, engine)


# FAZ A CONSULTA NO BANCO PARA A TABELA Movimentos_estoque
sql_query_movimentos_estoque = "SELECT * FROM Movimentos_estoque"
df_movimentos_estoque = pd.read_sql(sql_query_movimentos_estoque, engine)

# FAZ A CONSULTA NO BANCO PARA A TABELA ops_visual
sql_query_ops_visual = "SELECT * FROM ops_visual"
df_ops_visual = pd.read_sql(sql_query_ops_visual, engine)

# AS COLUNAS TEM QUE EXISTIR
if 'tipo_mov' in df_estrutura_op.columns and 'quantidade_item' in df_estrutura_op.columns and \
        'item' in df_movimentos_estoque.columns and 'quantidade' in df_movimentos_estoque.columns and \
        'situação' in df_ops_visual.columns:

    # DADOS RETIRADOS DA TABELA estrutura_op NO BANCO
    fig_estrutura_op = px.bar(df_estrutura_op, x='tipo_mov', y='quantidade_item', title='Estrutura OP',
                               labels={'quantidade_item': 'Quantidade'},
                               color_discrete_sequence=px.colors.qualitative.Set1
                               )
    # CONFIGURA A LARGURA DO GRAFICO
    fig_estrutura_op.update_layout(bargap=0.1)

    # DADOS RETIRADOS DA TABELA Movimentos_estoque NO BANCO
    fig_movimentos_estoque = px.bar(df_movimentos_estoque, x='item', y='quantidade',
                                     title='Movimentos Estoque',
                                     labels={'quantidade': 'Quantidade'},
                                     color_discrete_sequence=px.colors.qualitative.Set2
                                     )
    # CONFIGURA A LARGURA DO GRAFICO
    fig_movimentos_estoque.update_layout(bargap=0.1)

    # DADOS RETIRADOS DA TABELA ops_visual NO BANCO
    fig_ops_visual = px.pie(df_ops_visual, names='situação', title='Ops Visual - Situação',
                             labels={'situação': 'situação'},
                             color_discrete_sequence=px.colors.qualitative.Pastel1
                             )

    app = dash.Dash(__name__)

    # LAYOUT HTML QUE APARECERÀ NO NAVEGADOR
    app.layout = html.Div(children=[
        html.Div(
            html.H1(children='Kels - Indicadores', style={'color': 'white', 'background-color': 'gray', 'padding': '20px', 'margin-bottom': '0', 'margin-top': '0'}),
        ),

        # PRIMEIRO GRÁFICO
        dcc.Graph(
            id='grafico-estrutura-op',
            figure=fig_estrutura_op,
            style={'width': '48%', 'display': 'inline-block'}  
        ),

        # SEGUNDO GRÁFICO
        dcc.Graph(
            id='grafico-movimentos-estoque',
            figure=fig_movimentos_estoque,
            style={'width': '48%', 'display': 'inline-block'} 
        ),

        # TERCEIRO GRÁFICO
        dcc.Graph(
            id='grafico-ops-visual',
            figure=fig_ops_visual,
            style={'width': '48%', 'display': 'inline-block', 'margin-top': '20px'} 
        )
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)
else:
    print("Certifique-se de que os nomes das colunas existem nas tabelas do banco.")