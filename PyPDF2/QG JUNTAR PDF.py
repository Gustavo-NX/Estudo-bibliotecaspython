import PyPDF2 #PARA O PYTHON IDENTIFICAR OS PDFS E USAR BIBLIOTECA
import os #BIBLIOTECA PARA USAR ARQUIVSO LOCAIS

merger = PyPDF2.PdfMerger() #CRIANDO VARIAVEL "merger" PARA JUNTAR PDF

lista_arquivos = os.listdir("MaquinaJuncaoPDF") # variavel lista_arquivos vai listalos e lê-los
lista_arquivos.sort() #para ordenar lista
print(lista_arquivos) #aqui era só pra ver os arquivis que estava achando

for arquivo in lista_arquivos: #Se "arquivo" criada aqui em lista_arquivos criando repetição para o programa ler
    if ".pdf" in arquivo: #Se tiver escrito ".pdf" in arquivo(puxando variavel criada na repetição)
        merger.append(f"MaquinaJuncaoPDF/{arquivo}") #append está adicionando arquivo que está sendo lido ao mesclador merge

merger.write("PDF FINAL.pdf") #merge.write para escrever o novo arquivo lido como "PDF FINAL.pdf" para criar arquivo