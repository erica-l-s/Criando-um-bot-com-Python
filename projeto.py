import requests

def coletando_frases():    
    r = requests.get('https://quotes.toscrape.com/')
    # print(r.text)

    html = r.text.split('\n')
    # print(html)

    frases = []

    for linha in html:
        if '<span class="text" itemprop="text">' in linha:
            linha_editada = linha.replace('<span class="text" itemprop="text">', '')
            linha_editada = linha_editada.replace('</span>', '')
            linha_editada = linha_editada.strip()
            frases.append(linha_editada)
    
    return frases
        

def coletando_primeira_frase():
    frases = coletando_frases()
    return(frases[0])

coletando_primeira_frase()





