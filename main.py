import streamlit as st

#Cria a barra lateral
with st.sidebar:
    st.title("Calculadora IMC")

    st.header("O que é IMC?")
    st.markdown("""
                A classificação do índice de massa corporal (IMC) pode ajudar a identificar problemas de obesidade ou desnutrição, em crianças, adolescentes, adultos e idosos
                """)
    #Linha com texto
    st.write("""
    - **Menor que 18,5**:	    Magreza
    - **18,5 a 24,9**:	        Normal
    - **25 a 29,9**:	        Sobrepeso
    - **30 a 34,9**:	        Obesidade grau I
    - **35 a 39,9**:	        Obesidade grau II
    - **Maior que 40**:	        Obesidade grau III
             """)


st.title("Calculadora IMC")

#Entrada de dados - peso
peso = st.number_input(label="Digite o seu peso (Em Kg)", min_value = 0.0, step = 0.10, format= "%.1f")

altura = st.number_input(label="Digite a sua altura (Em Metros)", min_value = 0.0, step = 0.10, format= "%.2f")

if st.button("Calcular"):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        imc_ideal = 21.7
        imc_delta = imc - imc_ideal
         
        if imc < 18.5:
             classe = "Abaixo do peso"
        elif imc < 24.9:
            classe = "Peso ideal"
        elif imc < 29.9:
            classe = "Sobre peso"
        elif imc < 34.9:
            classe = "Obesidade grau I"
        elif imc < 39.9:
            classe = "Obesidade grau II"
        else:
            classe = "Obesidade grau III"
        st.success("Calculo realizado com sucesso!!")

        #Escrever valores
        st.write(f"Seu *IMC* é: {imc:.2f} ")
        st.write(f"Sua Classificação é: {classe} ")
        st.write(f"Comparação com IMC ideal (21.7): **{imc_delta:.2f}** ")


        #Dividir uma linha em duas colunas 
        col1, col2 = st.columns(2)

        col1.metric("Classificação", classe, f"{imc_delta:.2f}", delta_color="inverse")        
        col2.metric("IMC", f"{imc:.2f}", f"{imc_delta:.2f}", delta_color="off")   

        #Criar uma linha
        st.divider()
        st.image("./IMC.png")     
        
    
    
    else:
        #Mostrar mensagem de erro
        st.error("Por favor, insira os valores válidos para peso e altura.")
          
            


