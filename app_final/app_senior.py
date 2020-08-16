import streamlit as st
from Analisador import Analisador
from Classificador import Classificador
from PIL import Image


if __name__ == '__main__':

	path = "sms_senior.csv"


	analise = st.sidebar.selectbox("Selecione o que deseja visualizar", ["< selecionar analise >","questao 1 - analise exploratoria", "questao 2 - modelo preditivo"])
	image = Image.open('logo.png')
	st.image(image, output_format = 'png')
	st.title("TESTE TECNICO - PESQUISADOR SENIOR LABS")

	if analise == 'questao 1 - analise exploratoria':
		analisador = Analisador(path)

		princ_palavras = st.sidebar.checkbox("Topico 1 - Visualizar principais palavras")
		contagem_tipo_mes = st.sidebar.checkbox("Topicos 2, 3 e 4 - Analises mensais")

		if princ_palavras:

			num = st.slider("", min_value=1, max_value=50, value = 10)
			remove = st.checkbox("Remover stopwords da analise")

			if remove:
				analisador.remove_SW()

			analisador.word_count()
			analisador.cria_WC()
			analisador.cria_grafico_contagem_palavras(num)

			st.write(analisador.grafico_principais_palavras)
			st.write(analisador.wordcloud)

		if contagem_tipo_mes:
			analisador.cria_colunas()
			analisador.salva_info_meses()

			spam_ou_nao = st.checkbox("Topico 2 - Mensagem comum e spam por mes")
			conta_palavras = st.checkbox("Topico 3 - Dados estatisticos de contagem de palavras por mes")
			cont_dia = st.checkbox("Topico 4 - Quantidade de mensagem comum por dia do mes")


			if spam_ou_nao:
				analisador.spam_mensal()

				st.write(analisador.grafico_spam_mes)
				st.write(analisador.grafico_nao_spam_mes)
				st.write(analisador.pie_spam_mes)
				st.write(analisador.pie_nao_spam_mes)


			if conta_palavras:
				analisador.conta_palavras_mensal()

				st.dataframe(analisador.df_palavras_mes)

			if cont_dia:
				analisador.conta_spam_dia()
				
				for imagem in analisador.contagem_dia:
					st.write(imagem)

	if analise == "questao 2 - modelo preditivo":
		classificador = Classificador(path)
		modelo_select = st.selectbox("selecione modelo", ["< selecionar >","random forest","decision tree","support vector classifier","kNeighbors classifier","adaboost classifier"])

		if modelo_select != "< selecionar >":
			botao =	st.button("treinar")

			if botao:
				classificador.preprocessing()
				classificador.treina_modelo(modelo_select)
				classificador.preve_modelo()
				st.write("CLASSIFICATION REPORT:")
				st.write(classificador.class_rep)
				st.write("\n\n SCORE TOTAL:")
				st.write(classificador.acc_score)
				st.write("MATRIZ DE CONFUSAO:")
				st.write(classificador.conf_mat)
