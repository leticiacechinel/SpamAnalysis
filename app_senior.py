import streamlit as st
from Analisador import Analisador

if __name__ == '__main__':

	path = "/home/leticia/Documentos/PS/SENIOR/Desafio -Senior Labs - 2020/sms_senior.csv"
	analisador = Analisador(path)
	analisador.remove_SW()
	analisador.word_count()
	analisador.cria_WC()
	analisador.cria_grafico_contagem_palavras()

	st.write(analisador.grafico_principais_palavras)
	st.write(analisador.wordcloud)