import streamlit as st

def main():
    genres = ["Animation/Animé","Aventure","Romantique","Comédie","Action","Familial","Dramatique","Crimes","Fantaisie","Science fiction","Thriller","Musical","Horreur","Documentaire","Mystère","Western","Guerre","Film de télévision"]
    # Define the checkboxes in two columns
    col1, col2 = st.beta_columns(2)
    with col1:
        option1 = st.checkbox(genre[0])
        option2 = st.checkbox(genre[1])
        option3 = st.checkbox(genre[2])
        option4 = st.checkbox(genre[3])
        option5 = st.checkbox(genre[4])
        option6 = st.checkbox(genre[5])
        option7 = st.checkbox(genre[6])
        option8 = st.checkbox(genre[7])          
    with col2:
        option9 = st.checkbox(genre[8])
        option10 = st.checkbox(genre[9])
        option11 = st.checkbox(genre[10])
        option12 = st.checkbox(genre[11])
        option13 = st.checkbox(genre[12])
        option14 = st.checkbox(genre[13])
        option15 = st.checkbox(genre[14])
        option16 = st.checkbox(genre[15]) 

    # Define a validation button to write the selected options into a variable
    if st.button('Validate'):
        selected_options = []
        if option1:
            selected_options.append(genres[0])
        if option2:
            selected_options.append(genres[1])
        if option3:
            selected_options.append(genres[2])
        if option4:
            selected_options.append(genres[3])
        if option5:
            selected_options.append(genres[4])
        if option6:
            selected_options.append(genres[5])
        if option7:
            selected_options.append(genres[6])
        if option8:
            selected_options.append(genres[7])
        if option9:
            selected_options.append(genres[8])
        if option10:
            selected_options.append(genres[9])
        if option11:
            selected_options.append(genres[10])
        if option12:
            selected_options.append(genres[11])
        if option13:
            selected_options.append(genres[12])
        if option14:
            selected_options.append(genres[13])   
        if option15:
            selected_options.append(genres[14])
        if option16:
            selected_options.append(genres[15])               
        st.write(f'Selected options: {selected_options}')

if __name__ == '__main__':
    main()
