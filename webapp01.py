# myFirstStreamlitApp.py
#import the libraries
import streamlit as st
from PIL import Image

image01 = Image.open('logo.jpg')
image02 = Image.open('Diferenciais.PNG')

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Sascar Tecnologia e Segurança Automotiva S/A")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
#st.header("Empresa do Grupo Michelin especializada em gestão de frotas e com foco total nos clientes")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
#st.subheader("Sub Cabeçalho")

# Use st.write("") para adicionar um texto ao seu Web app
#st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

#st.subheader("------ **Desenvolvido por: Massaki de O. Igarashi** -----")

menu = [#"Texto_Colunas",
        #"Texto_Markdown",
        "Empresa_Sascar"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.write("ADRIANA PEREIRA KORNREUTER")
st.sidebar.write("BRUNO RAMOS ALVES")
    
#if choice == "Texto_Colunas":       
    #st.subheader("Texto formatado em colunas")
    #st.write("Veja a seguir uma opção de formatação em colunas")    
    #cols01 = st.columns(2)    
    #cols01[0].write('Texto da Coluna 01')
    #cols01[1].write('Texto da Coluna 02')
#elif choice == "Texto_Markdown":
    #st.subheader("Texto Markdown")
    #st.write("Veja a seguir opção de formatação de texto Markdown")
    #st.markdown(
    #"""
    ## *Alguns sites referências*:    
  #  - [Streamlit: hello world](https://calmcode.io/streamlit/hello-world.html)
   # - [:star: Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlitapp.com/)
   # - [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
   
    ##### CRONOGRAMA
    #DIA | CH HORÁRIA | CONTEÚDO
  #  :---------: | :------: | :-------:
    #Dia 1 de 2 | ?h | ? a ?
   # Dia 2 de 2 | ?h | ? a ?
   # """
   # )
    
if choice == "Empresa_Sascar":
    st.image(image01, width=500) 
  # Use st.header("") para adicionar um CABEÇALHO ao seu Web app
    st.header("Sobre a Empresa")
  # Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
    st.subheader("Empresa do Grupo Michelin especializada em gestão de frotas e com foco total nos clientes, líder na América Latina e com presença na América do Sul, México e Europa. Auxilia 54 mil clientes, com mais de 270 mil veículos conectados, a irem cada vez mais longe através de soluções tecnológicas e contribuímos para uma mobilidade mais segura, eficiente e sustentável.")
 # Use st.header("") para adicionar um CABEÇALHO ao seu Web app
    st.header("Diferenciais")
    st.image(image02, width=800)
        
        
