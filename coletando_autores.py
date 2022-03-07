import requests

def coletando_autor():    
    r = requests.get('https://quotes.toscrape.com/')
    # print(r.text)

    html = r.text.split('\n')
    # print(html)

    autor = []

    for linha in html:
        if '<span>by <small class="author" itemprop="author">' in linha:
            linha_editada = linha.replace('<span>by <small class="author" itemprop="author">', '')
            linha_editada = linha_editada.replace('</small>', '')
            linha_editada = linha_editada.strip()
            autor.append(linha_editada)
    
    return autor
        

def coletando_primeiro_autor():
    autor = coletando_autor()
    print(autor[0])

coletando_primeiro_autor()
