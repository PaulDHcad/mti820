import streamlit as st

def main():
    #genres = ["Animation/Animé","Aventure","Romantique","Comédie","Action","Familial","Dramatique","Crimes","Fantaisie","Science fiction","Thriller","Musical","Horreur","Documentaire","Mystère","Western","Guerre","Film de télévision"]
    # Define the checkboxes in two columns
    col1, col2 = st.columns(2)
    with col1:
        option1 = st.checkbox("Animation/Animé")
        option2 = st.checkbox("Aventure")
        option3 = st.checkbox("Romantique")
        option4 = st.checkbox("Comédie")
        option5 = st.checkbox("Action")
        option6 = st.checkbox("Familial")
        option7 = st.checkbox("Dramatique")
        option8 = st.checkbox("Crimes")       
        option9 = st.checkbox("Fantaisie")        
    with col2:
        option10 = st.checkbox("Science fiction")
        option11 = st.checkbox("Thriller")
        option12 = st.checkbox("Musical")
        option13 = st.checkbox("Horreur")
        option14 = st.checkbox("Documentaire")
        option15 = st.checkbox("Mystère")
        option16 = st.checkbox("Western") 
        option17 = st.checkbox("Guerre")        
        option18 = st.checkbox("Film de télévision")   
        
    # Define a validation button to write the selected options into a variable
    if st.button('Validate'):
        selected_options = []
        if option1:
            selected_options.append("Animation/Animé")
        if option2:
            selected_options.append("Aventure")
        if option3:
            selected_options.append("Romantique")
        if option4:
            selected_options.append("Comédie")
        if option5:
            selected_options.append("Action")
        if option6:
            selected_options.append("Familial")
        if option7:
            selected_options.append("Dramatique")
        if option8:
            selected_options.append("Crimes")
        if option9:
            selected_options.append("Fantaisie")
        if option10:
            selected_options.append("Science fiction")
        if option11:
            selected_options.append("Thriller")
        if option12:
            selected_options.append("Musical")
        if option13:
            selected_options.append("Horreur")
        if option14:
            selected_options.append("Documentaire")   
        if option15:
            selected_options.append("Mystère")
        if option16:
            selected_options.append("Western") 
        if option17:
            selected_options.append("Guerre")   
        if option18:
            selected_options.append("Film de télévision")              
        st.write(f'Selected options: {selected_options}')

if __name__ == '__main__':
    main()
