#!pip install streamlit

import streamlit as st
import pandas as pd

db_all = pd.read_csv('./all_movies.csv', sep=';')
db_all = db_all.sort_values(by=['rating'], ascending=False)
db_all = db_all.reset_index(drop=True)

db_bilheteria = pd.read_csv('./top10_bilheterias.csv', sep=';')

db_acao = db_all.copy()
db_acao = db_acao.query("genre == 'Ação'")
db_acao = db_acao.reset_index(drop=True)

db_aventura = db_all.copy()
db_aventura = db_aventura.query("genre == 'Aventura'")
db_aventura = db_aventura.reset_index(drop=True)

db_animacao = db_all.copy()
db_animacao = db_animacao.query("genre == 'Animação'")
db_animacao = db_animacao.reset_index(drop=True)

db_comedia = db_all.copy()
db_comedia = db_comedia.query("genre == 'Comédia'")
db_comedia = db_comedia.reset_index(drop=True)

db_drama = db_all.copy()
db_drama = db_drama.query("genre == 'Drama'")
db_drama = db_drama.reset_index(drop=True)

db_misterio = db_all.copy()
db_misterio = db_misterio.query("genre == 'Mistério'")
db_misterio = db_misterio.reset_index(drop=True)

db_terror = db_all.copy()
db_terror = db_terror.query("genre == 'Terror'")
db_terror = db_terror.reset_index(drop=True)

st.set_page_config( page_title = 'CK 2 - Auto ML',
                    layout = 'wide',
                    initial_sidebar_state = 'expanded')

st.title('Filmes')

st.divider()

st.header('Top 5 Avaliados')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.subheader(f'{db_all["title_pt"][0]} ({db_all["year"][0]})')
  st.caption(f'Gênero: {db_all["genre"][0]}')
  st.caption(f'Nota: {db_all["rating"][0]}')
  st.image(db_all['imagens'][0], width=240)
  st.write(f'Sinopse: {db_all["sinopse"][0]}')

with col2:
  st.subheader(f'{db_all["title_pt"][1]} ({db_all["year"][1]})')
  st.caption(f'Gênero: {db_all["genre"][1]}')
  st.caption(f'Nota: {db_all["rating"][1]}')
  st.image(db_all['imagens'][1], width=240)
  st.write(f'Sinopse: {db_all["sinopse"][1]}')

with col3:
  st.subheader(f'{db_all["title_pt"][2]} ({db_all["year"][2]})')
  st.caption(f'Gênero: {db_all["genre"][2]}')
  st.caption(f'Nota: {db_all["rating"][2]}')
  st.image(db_all['imagens'][2], width=240)
  st.write(f'Sinopse: {db_all["sinopse"][2]}')

with col4:
  st.subheader(f'{db_all["title_pt"][3]} ({db_all["year"][3]})')
  st.caption(f'Gênero: {db_all["genre"][3]}')
  st.caption(f'Nota: {db_all["rating"][3]}')
  st.image(db_all['imagens'][3], width=240)
  st.write(f'Sinopse: {db_all["sinopse"][3]}')

with col5:
  st.subheader(f'{db_all["title_pt"][4]} ({db_all["year"][4]})')
  st.caption(f'Gênero: {db_all["genre"][4]}')
  st.caption(f'Nota: {db_all["rating"][4]}')
  st.image(db_all['imagens'][4], width=240)
  st.write(f'Sinopse: {db_all["sinopse"][4]}')

st.divider()

st.header('Top 5 Bilheterias')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.subheader(f'{db_bilheteria["title_pt"][0]} ({db_bilheteria["year"][0]})')
  st.caption(f'Gênero: {db_bilheteria["genre"][0]}')
  st.caption(f'Nota: {db_bilheteria["rating"][0]}')
  st.image(db_bilheteria['imagens'][0], width=240)
  st.write(f'Sinopse: {db_bilheteria["sinopse"][0]}')

with col2:
  st.subheader(f'{db_bilheteria["title_pt"][1]} ({db_bilheteria["year"][1]})')
  st.caption(f'Gênero: {db_bilheteria["genre"][1]}')
  st.caption(f'Nota: {db_bilheteria["rating"][1]}')
  st.image(db_bilheteria['imagens'][1], width=240)
  st.write(f'Sinopse: {db_bilheteria["sinopse"][1]}')

with col3:
  st.subheader(f'{db_bilheteria["title_pt"][2]} ({db_bilheteria["year"][2]})')
  st.caption(f'Gênero: {db_bilheteria["genre"][2]}')
  st.caption(f'Nota: {db_bilheteria["rating"][2]}')
  st.image(db_bilheteria['imagens'][2], width=240)
  st.write(f'Sinopse: {db_bilheteria["sinopse"][2]}')

with col4:
  st.subheader(f'{db_bilheteria["title_pt"][3]} ({db_bilheteria["year"][3]})')
  st.caption(f'Gênero: {db_bilheteria["genre"][3]}')
  st.caption(f'Nota: {db_bilheteria["rating"][3]}')
  st.image(db_bilheteria['imagens'][3], width=240)
  st.write(f'Sinopse: {db_bilheteria["sinopse"][3]}')

with col5:
  st.subheader(f'{db_bilheteria["title_pt"][4]} ({db_bilheteria["year"][4]})')
  st.caption(f'Gênero: {db_bilheteria["genre"][4]}')
  st.caption(f'Nota: {db_bilheteria["rating"][4]}')
  st.image(db_bilheteria['imagens'][4], width=240)
  st.write(f'Sinopse: {db_bilheteria["sinopse"][4]}')

st.divider()

st.header('Top 5 Ação')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.subheader(f'{db_acao["title_pt"][0]} ({db_acao["year"][0]})')
  st.caption(f'Gênero: {db_acao["genre"][0]}')
  st.caption(f'Nota: {db_acao["rating"][0]}')
  st.image(db_acao['imagens'][0], width=240)
  st.write(f'Sinopse: {db_acao["sinopse"][0]}')

with col2:
  st.subheader(f'{db_acao["title_pt"][1]} ({db_acao["year"][1]})')
  st.caption(f'Gênero: {db_acao["genre"][1]}')
  st.caption(f'Nota: {db_acao["rating"][1]}')
  st.image(db_acao['imagens'][1], width=240)
  st.write(f'Sinopse: {db_acao["sinopse"][1]}')

with col3:
  st.subheader(f'{db_acao["title_pt"][2]} ({db_acao["year"][2]})')
  st.caption(f'Gênero: {db_acao["genre"][2]}')
  st.caption(f'Nota: {db_acao["rating"][2]}')
  st.image(db_acao['imagens'][2], width=240)
  st.write(f'Sinopse: {db_acao["sinopse"][2]}')

with col4:
  st.subheader(f'{db_acao["title_pt"][3]} ({db_acao["year"][3]})')
  st.caption(f'Gênero: {db_acao["genre"][3]}')
  st.caption(f'Nota: {db_acao["rating"][3]}')
  st.image(db_acao['imagens'][3], width=240)
  st.write(f'Sinopse: {db_acao["sinopse"][3]}')

with col5:
  st.subheader(f'{db_acao["title_pt"][4]} ({db_acao["year"][4]})')
  st.caption(f'Gênero: {db_acao["genre"][4]}')
  st.caption(f'Nota: {db_acao["rating"][4]}')
  st.image(db_acao['imagens'][4], width=240)
  st.write(f'Sinopse: {db_acao["sinopse"][4]}')

st.divider()

st.header('Top 5 Aventura')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.subheader(f'{db_aventura["title_pt"][0]} ({db_aventura["year"][0]})')
  st.caption(f'Gênero: {db_aventura["genre"][0]}')
  st.caption(f'Nota: {db_aventura["rating"][0]}')
  st.image(db_aventura['imagens'][0], width=240)
  st.write(f'Sinopse: {db_aventura["sinopse"][0]}')

with col2:
  st.subheader(f'{db_aventura["title_pt"][1]} ({db_aventura["year"][1]})')
  st.caption(f'Gênero: {db_aventura["genre"][1]}')
  st.caption(f'Nota: {db_aventura["rating"][1]}')
  st.image(db_aventura['imagens'][1], width=240)
  st.write(f'Sinopse: {db_aventura["sinopse"][1]}')

with col3:
  st.subheader(f'{db_aventura["title_pt"][2]} ({db_aventura["year"][2]})')
  st.caption(f'Gênero: {db_aventura["genre"][2]}')
  st.caption(f'Nota: {db_aventura["rating"][2]}')
  st.image(db_aventura['imagens'][2], width=240)
  st.write(f'Sinopse: {db_aventura["sinopse"][2]}')

with col4:
  st.subheader(f'{db_aventura["title_pt"][3]} ({db_aventura["year"][3]})')
  st.caption(f'Gênero: {db_aventura["genre"][3]}')
  st.caption(f'Nota: {db_aventura["rating"][3]}')
  st.image(db_aventura['imagens'][3], width=240)
  st.write(f'Sinopse: {db_aventura["sinopse"][3]}')

with col5:
  st.subheader(f'{db_aventura["title_pt"][4]} ({db_aventura["year"][4]})')
  st.caption(f'Gênero: {db_aventura["genre"][4]}')
  st.caption(f'Nota: {db_aventura["rating"][4]}')
  st.image(db_aventura['imagens'][4], width=240)
  st.write(f'Sinopse: {db_aventura["sinopse"][4]}')

st.divider()

st.header('Top 5 Animação')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.subheader(f'{db_animacao["title_pt"][0]} ({db_animacao["year"][0]})')
  st.caption(f'Gênero: {db_animacao["genre"][0]}')
  st.caption(f'Nota: {db_animacao["rating"][0]}')
  st.image(db_animacao['imagens'][0], width=240)
  st.write(f'Sinopse: {db_animacao["sinopse"][0]}')

with col2:
  st.subheader(f'{db_animacao["title_pt"][1]} ({db_animacao["year"][1]})')
  st.caption(f'Gênero: {db_animacao["genre"][1]}')
  st.caption(f'Nota: {db_animacao["rating"][1]}')
  st.image(db_animacao['imagens'][1], width=240)
  st.write(f'Sinopse: {db_animacao["sinopse"][1]}')

with col3:
  st.subheader(f'{db_animacao["title_pt"][2]} ({db_animacao["year"][2]})')
  st.caption(f'Gênero: {db_animacao["genre"][2]}')
  st.caption(f'Nota: {db_animacao["rating"][2]}')
  st.image(db_animacao['imagens'][2], width=240)
  st.write(f'Sinopse: {db_animacao["sinopse"][2]}')

with col4:
  st.subheader(f'{db_animacao["title_pt"][3]} ({db_animacao["year"][3]})')
  st.caption(f'Gênero: {db_animacao["genre"][3]}')
  st.caption(f'Nota: {db_animacao["rating"][3]}')
  st.image(db_animacao['imagens'][3], width=240)
  st.write(f'Sinopse: {db_animacao["sinopse"][3]}')

with col5:
  st.subheader(f'{db_animacao["title_pt"][4]} ({db_animacao["year"][4]})')
  st.caption(f'Gênero: {db_animacao["genre"][4]}')
  st.caption(f'Nota: {db_animacao["rating"][4]}')
  st.image(db_animacao['imagens'][4], width=240)
  st.write(f'Sinopse: {db_animacao["sinopse"][4]}')

st.divider()

st.header('Top 5 Comédia')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.subheader(f'{db_comedia["title_pt"][0]} ({db_comedia["year"][0]})')
  st.caption(f'Gênero: {db_comedia["genre"][0]}')
  st.caption(f'Nota: {db_comedia["rating"][0]}')
  st.image(db_comedia['imagens'][0], width=240)
  st.write(f'Sinopse: {db_comedia["sinopse"][0]}')

with col2:
  st.subheader(f'{db_comedia["title_pt"][1]} ({db_comedia["year"][1]})')
  st.caption(f'Gênero: {db_comedia["genre"][1]}')
  st.caption(f'Nota: {db_comedia["rating"][1]}')
  st.image(db_comedia['imagens'][1], width=240)
  st.write(f'Sinopse: {db_comedia["sinopse"][1]}')

with col3:
  st.subheader(f'{db_comedia["title_pt"][2]} ({db_comedia["year"][2]})')
  st.caption(f'Gênero: {db_comedia["genre"][2]}')
  st.caption(f'Nota: {db_comedia["rating"][2]}')
  st.image(db_comedia['imagens'][2], width=240)
  st.write(f'Sinopse: {db_comedia["sinopse"][2]}')

with col4:
  st.subheader(f'{db_comedia["title_pt"][3]} ({db_comedia["year"][3]})')
  st.caption(f'Gênero: {db_comedia["genre"][3]}')
  st.caption(f'Nota: {db_comedia["rating"][3]}')
  st.image(db_comedia['imagens'][3], width=240)
  st.write(f'Sinopse: {db_comedia["sinopse"][3]}')

with col5:
  st.subheader(f'{db_comedia["title_pt"][4]} ({db_comedia["year"][4]})')
  st.caption(f'Gênero: {db_comedia["genre"][4]}')
  st.caption(f'Nota: {db_comedia["rating"][4]}')
  st.image(db_comedia['imagens'][4], width=240)
  st.write(f'Sinopse: {db_comedia["sinopse"][4]}')

st.divider()

st.header('Top 5 Drama')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.subheader(f'{db_drama["title_pt"][0]} ({db_drama["year"][0]})')
  st.caption(f'Gênero: {db_drama["genre"][0]}')
  st.caption(f'Nota: {db_drama["rating"][0]}')
  st.image(db_drama['imagens'][0], width=240)
  st.write(f'Sinopse: {db_drama["sinopse"][0]}')

with col2:
  st.subheader(f'{db_drama["title_pt"][1]} ({db_drama["year"][1]})')
  st.caption(f'Gênero: {db_drama["genre"][1]}')
  st.caption(f'Nota: {db_drama["rating"][1]}')
  st.image(db_drama['imagens'][1], width=240)
  st.write(f'Sinopse: {db_drama["sinopse"][1]}')

with col3:
  st.subheader(f'{db_drama["title_pt"][2]} ({db_drama["year"][2]})')
  st.caption(f'Gênero: {db_drama["genre"][2]}')
  st.caption(f'Nota: {db_drama["rating"][2]}')
  st.image(db_drama['imagens'][2], width=240)
  st.write(f'Sinopse: {db_drama["sinopse"][2]}')

with col4:
  st.subheader(f'{db_drama["title_pt"][3]} ({db_drama["year"][3]})')
  st.caption(f'Gênero: {db_drama["genre"][3]}')
  st.caption(f'Nota: {db_drama["rating"][3]}')
  st.image(db_drama['imagens'][3], width=240)
  st.write(f'Sinopse: {db_drama["sinopse"][3]}')

with col5:
  st.subheader(f'{db_drama["title_pt"][4]} ({db_drama["year"][4]})')
  st.caption(f'Gênero: {db_drama["genre"][4]}')
  st.caption(f'Nota: {db_drama["rating"][4]}')
  st.image(db_drama['imagens'][4], width=240)
  st.write(f'Sinopse: {db_drama["sinopse"][4]}')

st.divider()

st.header('Top 5 Mistério')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.subheader(f'{db_misterio["title_pt"][0]} ({db_misterio["year"][0]})')
  st.caption(f'Gênero: {db_misterio["genre"][0]}')
  st.caption(f'Nota: {db_misterio["rating"][0]}')
  st.image(db_misterio['imagens'][0], width=240)
  st.write(f'Sinopse: {db_misterio["sinopse"][0]}')

with col2:
  st.subheader(f'{db_misterio["title_pt"][1]} ({db_misterio["year"][1]})')
  st.caption(f'Gênero: {db_misterio["genre"][1]}')
  st.caption(f'Nota: {db_misterio["rating"][1]}')
  st.image(db_misterio['imagens'][1], width=240)
  st.write(f'Sinopse: {db_misterio["sinopse"][1]}')

with col3:
  st.subheader(f'{db_misterio["title_pt"][2]} ({db_misterio["year"][2]})')
  st.caption(f'Gênero: {db_misterio["genre"][2]}')
  st.caption(f'Nota: {db_misterio["rating"][2]}')
  st.image(db_misterio['imagens'][2], width=240)
  st.write(f'Sinopse: {db_misterio["sinopse"][2]}')

with col4:
  st.subheader(f'{db_misterio["title_pt"][3]} ({db_misterio["year"][3]})')
  st.caption(f'Gênero: {db_misterio["genre"][3]}')
  st.caption(f'Nota: {db_misterio["rating"][3]}')
  st.image(db_misterio['imagens'][3], width=240)
  st.write(f'Sinopse: {db_misterio["sinopse"][3]}')

st.divider()

st.header('Top 5 Terror')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.subheader(f'{db_terror["title_pt"][0]} ({db_terror["year"][0]})')
  st.caption(f'Gênero: {db_terror["genre"][0]}')
  st.caption(f'Nota: {db_terror["rating"][0]}')
  st.image(db_terror['imagens'][0], width=240)
  st.write(f'Sinopse: {db_terror["sinopse"][0]}')

with col2:
  st.subheader(f'{db_terror["title_pt"][1]} ({db_terror["year"][1]})')
  st.caption(f'Gênero: {db_terror["genre"][1]}')
  st.caption(f'Nota: {db_terror["rating"][1]}')
  st.image(db_terror['imagens'][1], width=240)
  st.write(f'Sinopse: {db_terror["sinopse"][1]}')

with col3:
  st.subheader(f'{db_terror["title_pt"][2]} ({db_terror["year"][2]})')
  st.caption(f'Gênero: {db_terror["genre"][2]}')
  st.caption(f'Nota: {db_terror["rating"][2]}')
  st.image(db_terror['imagens'][2], width=240)
  st.write(f'Sinopse: {db_terror["sinopse"][2]}')

with col4:
  st.subheader(f'{db_terror["title_pt"][3]} ({db_terror["year"][3]})')
  st.caption(f'Gênero: {db_terror["genre"][3]}')
  st.caption(f'Nota: {db_terror["rating"][3]}')
  st.image(db_terror['imagens'][3], width=240)
  st.write(f'Sinopse: {db_terror["sinopse"][3]}')

with col5:
  st.subheader(f'{db_terror["title_pt"][4]} ({db_terror["year"][4]})')
  st.caption(f'Gênero: {db_terror["genre"][4]}')
  st.caption(f'Nota: {db_terror["rating"][4]}')
  st.image(db_terror['imagens'][4], width=240)
  st.write(f'Sinopse: {db_terror["sinopse"][4]}')
