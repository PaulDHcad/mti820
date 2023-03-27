import streamlit as st

def main():
    # Define the checkboxes in two columns
    col1, col2 = st.beta_columns(2)
    with col1:
        option1 = st.checkbox('Option 1')
        option2 = st.checkbox('Option 2')
        option3 = st.checkbox('Option 3')
    with col2:
        option4 = st.checkbox('Option 4')
        option5 = st.checkbox('Option 5')
        option6 = st.checkbox('Option 6')

    # Define a validation button to write the selected options into a variable
    if st.button('Validate'):
        selected_options = []
        if option1:
            selected_options.append('Option 1')
        if option2:
            selected_options.append('Option 2')
        if option3:
            selected_options.append('Option 3')
        if option4:
            selected_options.append('Option 4')
        if option5:
            selected_options.append('Option 5')
        if option6:
            selected_options.append('Option 6')
        st.write(f'Selected options: {selected_options}')

if __name__ == '__main__':
    main()
