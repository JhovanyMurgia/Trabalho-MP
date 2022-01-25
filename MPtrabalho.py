import PyPDF2
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

termos = [ "RDF", "Protege","OWL", "ITU", "ISO","TMFORUM", "DMTF", "IETF",
                      "F-LOGIC", "RDFS", "CIM", "Accounting", "fault", "performance",
                      "Security", "configuration"]
arquivo_por_termos = {"RDF":[], "Protege":[],"OWL":[], "ITU":[], "ISO":[],"TMFORUM":[], "DMTF":[], "IETF":[],
                      "F-LOGIC":[], "RDFS":[], "CIM":[], "Accounting":[], "fault":[], "performance":[],
                      "Security":[], "configuration":[]}

for k in range(20):

    nome = (f'Arquivo {k+1}')
    print(f'Analisando {nome}...')
    caminho = str(f"C:/Users/schel/PycharmProjects/2021/arquivo{k+1}.pdf")
    pdf_file = open(caminho, 'rb')
    object = PyPDF2.PdfFileReader(pdf_file)
    NumPages = object.getNumPages()

    for j in range(len(termos)):
        substring = termos[j]
        freq = 0

        for i in range(NumPages):
            PageObj = object.getPage(i)
            Text = PageObj.extractText()
            freq += Text.count(substring)
        if freq > 0:
            arquivo_por_termos[substring].append(nome)
        else:
            arquivo_por_termos[substring].append("NULL")


for k in range(12):

    nome = (f'Arquivo {k+21}')
    print(f'Analisando {nome}...')
    caminho = str(f"C:/Users/schel/PycharmProjects/2021/arquivo{k+1}.pdf")
    pdf_file = open(caminho, 'rb')
    object = PyPDF2.PdfFileReader(pdf_file)
    NumPages = object.getNumPages()

    for j in range(len(termos)):
        substring = termos[j]
        freq = 0

        for i in range(NumPages):
            PageObj = object.getPage(i)
            Text = PageObj.extractText()
            freq += Text.count(substring)
        if freq > 0:
            arquivo_por_termos[substring].append(nome)
        else:
            arquivo_por_termos[substring].append("NULL")


dados = pd.DataFrame(data=arquivo_por_termos)
dados.to_excel('dados.xlsx', index= False)

percentual = []
aux = []
cont = 0
for j in range(16):
    substring = termos[j]
    aux = arquivo_por_termos[substring]
    for i in range(32):
        if (aux[i] != 'NULL'):
            cont += 1
    percentual.append((cont/10)*100)
    cont = 0

plt.pie(x=percentual,labels=termos)
plt.show()


