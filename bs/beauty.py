import bs4
import requests

def extrair_frases():
    r = requests.get('https://quotes.toscrape.com/')  #biblioteca para puxar sites
    html = r.text                                     #ira puxar o texto desse site 
    soup = bs4.BeautifulSoup(html, 'html.parser')     #manipulaçao de strings 
    frases = soup.findAll('span',{'class':'text'})    #para poder pegar tudo que eu qro de uma determinada parte do site
    frases_sem_tag = [] 
    for frase in frases:
        frases_sem_tag.append(frase.string)
    

    return frases_sem_tag

def extrair_primeira_frase():
    todas_frases = extrair_frases()
    
    return todas_frases[0]

def extrair_autores():
    r = requests.get('https://quotes.toscrape.com/') 
    html = r.text                                     
    soup = bs4.BeautifulSoup(html, 'html.parser')     
    autores = soup.findAll('small')
    autores_sem_tag = []
    
    for autor in autores:
        autores_sem_tag.append(autor.string)
    
    return(autores_sem_tag)

def extrair_primeiro_autor():
    todos_autores = extrair_autores()
    
    return todos_autores[0]

print(extrair_primeiro_autor())


    



  





