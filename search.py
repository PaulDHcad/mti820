import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Movie Talks Search Engine", page_icon="🐍", layout="wide")
st.title("Movie List Search Engine")

film_path = "C:/Users/Admin/Dropbox/PC/Documents/Python Scripts/projet_data/film_cl.csv"
genre_path = "C:/Users/Admin/Dropbox/PC/Documents/Python Scripts/projet_data/genre_cl.csv"
casting_path = "C:/Users/Admin/Dropbox/PC/Documents/Python Scripts/projet_data/casting_cl.csv"
real_path = "C:/Users/Admin/Dropbox/PC/Documents/Python Scripts/projet_data/realisateur_cl.csv"
pop_path = "C:/Users/Admin/Dropbox/PC/Documents/Python Scripts/projet_data/popularite_cl.csv"
date_path = "C:/Users/Admin/Dropbox/PC/Documents/Python Scripts/projet_data/date_cl.csv"
periode_path = "C:/Users/Admin/Dropbox/PC/Documents/Python Scripts/projet_data/periode_cl.csv"
df_film = pd.read_csv(film_path, dtype=str, header=0,delimiter=",").fillna(0)
df_genre = pd.read_csv(genre_path, header=0, delimiter=",")
df_casting = pd.read_csv(casting_path,header=0,delimiter=",")
df_real = pd.read_csv(real_path, header=0, delimiter=",")
df_pop = pd.read_csv(pop_path, header=0, delimiter=",")
df_date = pd.read_csv(date_path, header=0, delimiter=",")
df_perd = pd.read_csv(periode_path, header=0, delimiter=",")


#merging film and genre dataframe
df_film['IdGenre'] = df_film['IdGenre'].astype(int)
film_genre = df_genre.join(df_film.set_index('IdGenre'), how='inner', on="Id",  lsuffix='_left', rsuffix='_right')

film_genre['IdActeur'] = film_genre['IdActeur'].astype(int)
film_genre_cast = df_casting.join(film_genre.set_index('IdActeur'), how='inner', on="Id",
                               lsuffix='_casting', rsuffix='_genre')

result_join = df_real.join(film_genre_cast.set_index('IdRealisateur'),
                                    how='inner', on="Id",
                                    lsuffix='_real', rsuffix='_film_genre_cast')


result_join['IdPopularite'] = result_join['IdPopularite'].astype(int)
result = df_pop.join(result_join.set_index('IdPopularite'),
                                    how='inner', on="Id",
                                    lsuffix='_pop', rsuffix='_result_join')
result['IdDateSortie'] = result['IdDateSortie'].astype(int)
result_date = df_date.join(result.set_index('IdDateSortie'),
                                    how='inner', on="Id",
                                    lsuffix='_date', rsuffix='_result')
result_date['IdPeriode'] = result_date['IdPeriode'].astype(int)
result_final = df_perd.join(result_date.set_index('IdPeriode'),
                                    how='inner', on="Id",
                                    lsuffix='_perd', rsuffix='_result_date')



#  search bar
col1, col2, col3 = st.columns(3)
with col2:
    add_checkbox2 = st.checkbox('Filtrage Avancé', label_visibility="collapsed", disabled=True)
    add_checkbox = st.checkbox('Filtrage Avancé', key='advance')
with col1:
    if add_checkbox:
        text_search = st.text_input("Search", value="", disabled=True)
    else:
        text_search = st.text_input("Search movie by title ", value="")




# Filter the dataframe using masks
m1 = result_final["Pays"].str.contains(text_search)
m2 = result_final["Title"].str.contains(text_search)
m3 = result_final["Genre1"].str.contains(text_search)
df_search = result_final[m1 | m2 | m3]



N_cards_per_row = 5
def display_search(data_frame,page_size):
    # Calculate the number of pages
    num_pages = int(np.ceil(len(data_frame) / page_size))
    # Add a selectbox to the sidebar for page navigation
    page_num = st.sidebar.selectbox("Page", range(num_pages))
    # Calculate the start and end index of the current page
    start_idx = page_num * page_size
    end_idx = min((page_num + 1) * page_size, len(data_frame))
    # Display the results for the current page
    data_frame2 = data_frame.iloc[start_idx:end_idx]
    for n_row, row in data_frame2.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="medium")
        # draw the card
        with cols[n_row%N_cards_per_row]:
            st.caption(f"{str(row['MoyenneVote']).strip()} - {str(row['TotalVote']).strip()} - {str(row['Adult']).strip()} ")
            st.markdown(f"**{row['Pays'].strip()}-{int(row['Annee'])}**")
            st.markdown(f"*{row['Title'].strip()}*")
            try:
                st.image(row['Poster_right'])
            except AttributeError as e:
                st.warning(f"Could not display image: {e}")
        # Add a pagination widget to the bottom of the page
    st.sidebar.write("Page", page_num + 1, "of", num_pages)
if text_search:
    display_search(df_search.head(100),20)
elif add_checkbox:
        # Add a selectbox to the sidebar:
        add_selectbox = st.sidebar.multiselect(
            'Choisissez votre genre de Film',
            result_final['Genre1'].unique()
        )
        add_selectbox2 = st.sidebar.selectbox(
            'Choisissez le realisateur',
            result_final['Nom'].unique()
        )
        # Add a slider to the sidebar:
        start, end = st.sidebar.slider(
            'Select a range of values',
            0.0, 10.0, (5.0, 7.0)
        )
        start2, end2 = st.sidebar.slider(
            'Select a range of years',
            1990, 2023, (1995, 2000)
        )
        add_button = st.sidebar.button('Appliquer')
        if add_button:
            # convert 'MoyenneVote' column to numeric type
            result_final['MoyenneVote'] = pd.to_numeric(result_final['MoyenneVote'], errors='coerce')
            result_list = result_final.loc[(result_final['MoyenneVote'].between(start, end, inclusive=True)&
                                            result_final['Annee'].between(start2, end2, inclusive=True)), :]
            if not add_selectbox:
                final_result = result_list.loc[result_list['Nom'] == add_selectbox2, :]
            else:
                final_result = result_list.loc[
                               result_list['Genre1'].isin(add_selectbox) & (result_list['Nom'] == add_selectbox2), :]

            for n_row, row in final_result.reset_index().iterrows():
                i = n_row % N_cards_per_row
                if i == 0:
                    st.write("---")
                    cols = st.columns(N_cards_per_row, gap="medium")
                # draw the card
                with cols[n_row % N_cards_per_row]:
                    st.caption(f"{str(row['MoyenneVote']).strip()} - {str(row['TotalVote']).strip()} - {str(row['Adult']).strip()} ")
                    st.markdown(f"**{row['Pays'].strip()}-{int(row['Annee'])}**")
                    st.markdown(f"*{row['Title'].strip()}*")
                    st.image(row['Poster_right'])


