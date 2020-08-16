# SpamAnalysis

Execucao

## 1 - aplicativo streamlit

### 1.1 - com docker (utilizacao recomendada)

baixar o diretório app_final completo

dentro do diretório app_final, no terminal, rodar sudo docker build -t seniorapp .

após montar, sudo docker run -p 8501:8501 seniorapp:latest

Usar o network URL que aparecerá para abrir o aplicativo no seu browser

### 1.2 - com ambiente conda

baixar o diretório app_final completo

criar ambiente conda utilizando o arquivo senior.yml, através do comando

conda env create -f senior.yml

dentro do diretório app_final, no terminal, rodar o comando streamlit run app_senior.py

## 2 -  Jupyter notebook

Todas as analises tambem estao disponiveis em arquivos ipynb. 

Criar o ambiente conforme descrito em 1.2 e em seguida, dentro do diretorio notebook pelo terminal executar o comando jupyter notebook.

No navegador aparecera a pasta com os arquivos, clicar no arquivo "desafio.ipynb" e executar as celulas.
