from nltk .corpus import stopwords 
from nltk.tokenize import word_tokenize, RegexpTokenizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
import operator



class Analisador():

	def __init__(self, path):

		self.dados = pd.read_csv(path, encoding='unicode_escape')
		self.dados["Date"] = pd.to_datetime(self.dados["Date"], format='%Y-%m-%d %H:%M:%S')
		self.full_text = self.dados.Full_Text.str.cat(sep=' ').lower()


	def remove_SW(self):

	    text = " "+self.full_text.lower()

	    text = text.replace(" ur "," you are ").replace(" u "," you ").replace("&lt;", "<").replace("&gt;", ">")    	    
	    tokenizer = nltk.RegexpTokenizer(r"\w+")
	    stop_words = set(stopwords.words('english')) 	    
	    new_words = tokenizer.tokenize(text)
	    filtered_tokens = [w for w in new_words if not w in stop_words if w.isalpha()] 
	    filtered_sentence = (" ").join(filtered_tokens)

	    self.full_text = filtered_sentence


	def word_count(self):

	    texto = self.full_text
	    counts = dict()
	    words = texto.split()

	    for word in words:
	        if word in counts:
	            counts[word] += 1
	        else:
	            counts[word] = 1

	    self.counts = counts


	def cria_WC(self):

	    wordcloud = WordCloud().generate(self.full_text)
	    fig = plt.figure()
	    plt.imshow(wordcloud, interpolation="bilinear")
	    plt.axis("off")
	    plt.show()

	    self.wordcloud = fig


	def cria_grafico_contagem_palavras(self, num):
		contagem = self.counts
		contagem = sorted(contagem.items(), key = operator.itemgetter(1), reverse = True)

		top_words = contagem[0:num] 

		x = [item[0] for item in top_words]
		y = [item[1] for item in top_words]

		fig = plt.figure()
		plt.bar(x,y)
		plt.title("top palavras")
		plt.xticks(rotation  = "vertical")

		self.grafico_principais_palavras = fig


	def cria_colunas(self):

		self.dados["mes"] = [data.month for data in self.dados.Date]
		self.dados["dia"] = [data.day for data in self.dados.Date]


	def salva_info_meses(self):

		dados_mensais = []
		meses = {1: 'janeiro', 2:'fevereiro',3:'marco'}

		dados = self.dados

		for mes in set(dados.mes):
		    palavras_mes = dados.Word_Count.loc[dados.mes == mes]
		    
		    dias_spam = dados.dia.loc[(dados.mes == mes) & (dados.IsSpam=='yes')]
		    dias_nao_spam = dados.dia.loc[(dados.mes == mes) & (dados.IsSpam=='no')]
		    
		    qtd_spam = len(dias_spam)
		    qtd_nao_spam =  len(dias_nao_spam)
		    
		    cont_spam_dia = dias_spam.value_counts()
		    cont_n_spam_dia = dias_nao_spam.value_counts()
		    
		    dados_mensais.append([meses[mes], qtd_nao_spam, qtd_spam, max(palavras_mes),min(palavras_mes), palavras_mes.mean(), palavras_mes.median(),palavras_mes.std(),palavras_mes.var(), cont_spam_dia, cont_n_spam_dia])
		
		self.dados_mensais = dados_mensais		    


	def spam_mensal(self):


		x = [dado[0] for dado in self.dados_mensais]
		y1 = [dado[1]  for dado in self.dados_mensais]
		y2 = [dado[2]  for dado in self.dados_mensais]

		fig = plt.figure()
		ax = plt.bar(x,y1)
		plt.title("Quantidade de mensagens sem spam por mes")
		self.grafico_spam_mes = fig

		fig = plt.figure()
		plt.bar(x,y2)
		plt.title("Quantidade de mensagens com spam por mes")
		self.grafico_nao_spam_mes = fig

		fig = plt.figure()
		plt.pie(y1, labels=x, autopct='%1.1f%%')
		plt.title("total de mensagens sem spam por mes")
		self.pie_nao_spam_mes = fig

		fig = plt.figure()
		plt.pie(y2, labels=x, autopct='%1.1f%%')
		plt.title("total de mensagens com spam por mes")
		self.pie_spam_mes = fig


	def conta_palavras_mensal(self):

		dados_mensais = self.dados_mensais
		df_word_month = pd.DataFrame()
		x = [dado[0] for dado in dados_mensais]
		df_word_month["maximo de palavras"] = [dado[3]  for dado in dados_mensais]
		df_word_month["minimo palavras"] = [dado[4]  for dado in dados_mensais]
		df_word_month["media palavras"] = [dado[5]  for dado in dados_mensais]
		df_word_month["mediana palavras"] = [dado[6]  for dado in dados_mensais]
		df_word_month["desvio padrao"] = [dado[7]  for dado in dados_mensais]
		df_word_month["variancia"] = [dado[8]  for dado in dados_mensais]
		df_word_month.index = x

		self.df_palavras_mes = df_word_month


	def conta_spam_dia(self):

		self.contagem_dia = []

		contagem_dia = [[dado[0],dado[10]] for dado in self.dados_mensais]

		for i in range(len(contagem_dia)):
			fig = plt.figure()
			top_dias = contagem_dia[i][1].index[0:10]
			total_msg = contagem_dia[i][1].values[0:10]
			plt.bar(top_dias, total_msg)
			plt.title(contagem_dia[i][0])
			plt.xlabel("\n dia do mes")
			plt.xticks(top_dias, rotation = 'vertical')
			plt.ylabel("total de msg nao spam")


			self.contagem_dia.append(fig)


