import streamlit as st
import json
import pandas as pd

# Navbar
st.sidebar.title('Airdrop Reminder')
selected = st.sidebar.selectbox(
    'Nagivasi', ('Add new data', 'List Airdrop', 'Change Progress', 'Data Wallet'), index=0)


if selected == "Add new data":
    # Input Airdrop Name
    st.header('')  # New Line
    st.markdown('#### Airdrop Name')
    A_Name = st.text_input('0', placeholder='Name',
                           label_visibility='collapsed')

    # Input Post Link
    st.markdown('#### Link Post')
    A_Link = st.text_input('0', placeholder='Link',
                           label_visibility='collapsed')

    # Progress
    st.write('')  # New Line
    st.markdown('#### Progress')
    Progress = st.radio('Progress', ('Finished', 'Need to be Done',
                        'Testnet', 'Other'), label_visibility='collapsed', index=0)

    if Progress == 'Need to be Done' or Progress == 'Other':
        Note = st.text_area('Note')
        data_note = Note
    else:
        data_note = ""

    # Save
    st.write('')  # New Line
    Save = st.button('Save')

    if Save:
        try:
            Data = {
                'Nama': A_Name,
                'Link': A_Link,
                'Progress': Progress,
                'Note': data_note
            }

            with open('Data Airdrop.txt', 'a') as f:
                json.dump(Data, f)
                f.write('\n')

            st.success('Data has been added to the database!')

        except:
            st.error('There seems to be an error!')

elif selected == "List Airdrop":
    st.header('')
    st.markdown('#### Data Airdrop')
    with open('Data Airdrop.txt', 'r') as f:
        data = f.read()

    data_list = []
    data = data.splitlines()
    for line in data:
        data_list.append(json.loads(line))

    df = pd.DataFrame(data_list)
    st.dataframe(df)

elif selected == 'Change Progress':
    st.header('')
    st.markdown('#### Change Progress')

    st.markdown('#### Airdrop Name')
    A_Name = st.text_input('0', placeholder='Name',
                           label_visibility='collapsed')

    st.markdown('#### Progress')
    Progress = st.radio('Progress', ('Finished', 'Need to be Done', 'Distributed',
                        'Not Distributed', 'Other'), label_visibility='collapsed', index=0)

    if Progress == 'Need to be Done' or Progress == 'Other':
        Note = st.text_area('Note')
        data_note = Note
    else:
        data_note = ""

    Save = st.button('Save')
    Delete = st.button('Delete')

    if Save:
        with open('Data Airdrop.txt', 'r') as f:
            data = f.read()

        data_list = []
        data = data.splitlines()
        for line in data:
            data_list.append(json.loads(line))

        for i, airdrop_dict in enumerate(data_list):
            if airdrop_dict['Nama'] == A_Name:
                # Modify the dictionary
                data_list[i]['Progress'] = Progress
                if Progress == "Finished":
                    data_list[i]['Note'] = ''
                elif Progress == 'Need to be Done' or Progress == 'Other':
                    data_list[i]['Note'] = Note
                break
        with open('Data Airdrop.txt', 'w') as f:
            for airdrop_dict in data_list:
                json.dump(airdrop_dict, f)
                f.write('\n')

        st.success('Data has been Changed!')

    if Delete:
        with open('Data Airdrop.txt', 'r') as f:
            data = f.read()

        data_list = []
        data = data.splitlines()
        for line in data:
            data_list.append(json.loads(line))

        for i, airdrop_dict in enumerate(data_list):
            if airdrop_dict['Nama'] == A_Name:
                # Delete the dictionary
                data_list.pop(i)
                break
        with open('Data Airdrop.txt', 'w') as f:
            for airdrop_dict in data_list:
                json.dump(airdrop_dict, f)
                f.write('\n')

        st.error('Data successfully deleted')

else:
    st.title('Save Your Wallet')

    # Input Wallet Provider
    st.header('')  # New Line
    st.markdown('#### Wallet Provider')
    WalletPr = st.text_input('0', placeholder='Name',
                             label_visibility='collapsed')

    # Input Wallet Address
    st.markdown('#### Wallet Address')
    WalletA = st.text_input('0', placeholder='Address',
                            label_visibility='collapsed')

    # Input Wallet Secret Pharse
    st.markdown('#### Secret Pharse')
    WalletPh = st.text_area('0', placeholder='Pharse',
                            label_visibility='collapsed')

    # Input Private Key
    st.markdown('#### Private Key')
    WalletK = st.text_input('0', placeholder='Key',
                            label_visibility='collapsed')

    # Input Note
    AddNote = st.checkbox('Add Note')
    if AddNote:
        st.markdown('#### Note')
        WalletN = st.text_area('0', placeholder='Note',
                               label_visibility='collapsed')
    else:
        WalletN = ''

# Save
    st.write('')  # New Line
    Save = st.button('Save')

    if Save:
        try:
            Data = {
                'Provider': WalletPr,
                'Address': WalletA,
                'Pharse': WalletPh,
                'Key': WalletK,
                'Note': WalletN
            }

            with open('Data Wallet.txt', 'a') as f:
                json.dump(Data, f)
                f.write('\n')

            st.success('Data has been added to the database!')

        except:
            st.error('There seems to be an error!')

    st.header('')
    st.markdown('#### Data Wallet')
    with open('Data Wallet.txt', 'r') as f:
        data = f.read()

    data_list = []
    data = data.splitlines()
    for line in data:
        data_list.append(json.loads(line))

    df = pd.DataFrame(data_list)
    st.dataframe(df)
