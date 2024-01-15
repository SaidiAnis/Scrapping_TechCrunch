#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#----------import nécessaires
import requests
from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


# Extraire liens et nom de catégories pour les mettre dans un dictionnaire

# In[114]:


#création du dictionnaire de catégories et du driver chrome
categories = {}
driver = webdriver.Chrome()
# Ouvrir une page web
driver.get("https://techcrunch.com/category/")
d
#attente 3s le temps que le popup cookies se charge
wait = WebDriverWait(driver, 3)
scroll_button = wait.until(EC.element_to_be_clickable((By.ID, 'scroll-down-btn')))

# Cliquer sur le bouton pour accepter les cookies/fermer le popup
scroll_button.click()

cookie_button = wait.until(EC.element_to_be_clickable((By.NAME, 'reject')))

# Cliquer sur le bouton pour accepter les cookies/fermer le popup
cookie_button.click()

# Attendre que la page soit entièrement chargée
WebDriverWait(driver, 60).until(lambda d: d.execute_script('return document.readyState') == 'complete')

# Obtenez le code source de la page
html = driver.page_source

# Fermer le navigateur une fois que terminé
driver.quit()

#utilisation de beautifulSoup pour extraire les liens et noms des catégories et faire un premier remplissage du dictionnaire
soup = BeautifulSoup(html, 'html')
ul = soup.find('ul',class_='menu not-found__menu')
lis = ul.find_all('li',class_='menu__item')
for li in lis:
    a = li.find('a')
    url = 'https://techcrunch.com'+a['href']
    category = a.text
    categories[category] = {'url': url, 'desc': None, 'articles':[]}


# In[115]:


print(categories)


# In[200]:


def get_article_attributes(url_page,current_driver):
    """
    créé un dictionnaire article, le remplie et le retourne
    Retourne un dictionnaire article.
    """
    current_driver.get(url_article)
    WebDriverWait(current_driver, 60).until(lambda d: d.execute_script('return document.readyState') == 'complete')
    # Obtenir le code source de la page
    html_article = current_driver.page_source
    soup_article = BeautifulSoup(html_article, 'html')
#-----------------------création du dictionnaire d'article avec ses attributs
    article = {
        'title' : soup_article.find('h1',class_='article__title').text,
        'author' : soup_article.find('a', href=lambda href: href and "author" in href).text,
        'creation_date' : soup_article.find('time',class_='full-date-time').text,
        'content' : soup_article.find('div',class_='article-content').get_text(separator=' ', strip=True),
        'url' : url_page,
        'tags' : soup_article.find('ul',class_='menu article__tags__menu').get_text(separator=', ', strip=True),
        'comments': ['No one seems to have shared their thoughts on this topic yet']
    }
    
    return article

Extraire les attributs des articles
# In[130]:


driver = webdriver.Chrome()

#variable pour ne cliquer sur le popup des cookies une seule fois
handle_popup_cookies = True
for category in categories:
    url_current = categories[category]['url']
    # Ouvrir une page web
    driver.get(url_current)
#----------------------------------------Gestion popup cookies (1 seul fois)
    if(handle_popup_cookies):
        wait = WebDriverWait(driver, 3)
        scroll_button = wait.until(EC.element_to_be_clickable((By.ID, 'scroll-down-btn')))
        
        # Cliquer sur le bouton pour accepter les cookies/fermer le popup
        scroll_button.click()
        
        cookie_button = wait.until(EC.element_to_be_clickable((By.NAME, 'reject')))
        
        # Cliquer sur le bouton pour accepter les cookies/fermer le popup
        cookie_button.click()
    
        handle_popup_cookies = False
        
#--------------------------------------------------------------------------Scrapping des données des articles    
    # Attendre que la page soit entièrement chargée
    WebDriverWait(driver, 60).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    for i in range(3):
        load_more = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'load-more ')))
        
        # Cliquer sur le bouton pour accepter les cookies/fermer le popup
        load_more.click()

    # Obtenir le code source de la page
    html_category = driver.page_source
#------------------------------------------------traitement avec beautifulSoup
    soup = BeautifulSoup(html_category, 'html')
    test_None = soup.find('div',class_='river__description')
#----------------------certaines catégories n'ont pas de description comme tcl
    if test_None is not None:
        category_description = test_None.text
        categories[category]['desc'] = category_description
#----------------------extraire les champs des articles
    articles = soup.find_all('article')
    for article in articles:
        url_article = 'https://techcrunch.com'+article.find('a',class_ = 'post-block__title__link')['href']
#---------------------fonction définie plus haut
        X = get_article_attributes(url_article,driver)
        categories[category]['articles'].append(X)
# Fermer le navigateur une fois terminé
driver.quit()
    


# In[131]:


#transformation du dictionnaire en fichiers json pour un stockage plus efficace
with open('articles.json','w') as fichier_json:
    json.dump(categories,fichier_json,indent = 4)


# In[205]:


def divide_time_date(chaine_date_heure):
    """
    Faute de temps, j'ai eu quelques problèmes pour supprimer les caractères \u2022 donc j'ai utilisé une méthode (CTRL+F) pour remplacer tous les caractères 
    \u2022 par --- ce qui est beaucoup plus simple à traiter.
    
    la fonction prend en entrée une chaine date et heure et divise en deux attributs date et heure.
    retourne deux chaines date_sql et heure_sql
    """
    try:

        # diviser le string en utilisant '---' 
        time_str, date_str = chaine_date_heure.split("---", 1)

        time_parts = time_str.split(" ")
        if len(time_parts) != 3:
            raise ValueError("Time format is not valid.")

        hour_min, am_pm, timezone = time_parts

        time_24hr = datetime.strptime(hour_min + ' ' + am_pm, '%I:%M %p').strftime('%H:%M')
        heure_sql = time_24hr + " " + timezone

        date_str_cleaned = re.sub(r'^\d+', '', date_str).strip()
        
        date_obj = datetime.strptime(date_str_cleaned, "%B %d, %Y")

        # Formate la date en "YYYY-MM-DD"
        date_sql = date_obj.strftime("%Y-%m-%d")

        return date_sql, heure_sql
    except ValueError as e:
        print("Error:", e)
        raise ValueError(f"The format of the date and time string is not valid: {e}")



# In[206]:


def diviser_texte_dynamiquement(texte, taille_max_par_partie=3500):
    """
    Divise un texte en plusieurs parties, chaque partie ayant une taille maximale spécifiée.
    Retourne une liste des parties.
    Cette fonction a été créé car dans oracle, une commande a une taille maximal de 4000 caractères
    """
    parties = []
    debut = 0

    while debut < len(texte):
        fin = debut + taille_max_par_partie

        # Ajuster le point de division pour ne pas couper en plein milieu d'un mot
        while fin < len(texte) and texte[fin] not in " \t\n":
            fin += 1

        parties.append(texte[debut:fin])
        debut = fin

    return parties

# Exemple d'utilisation
texte_long = "très long texte qui pourrait être un grand paragraphe ou un document étendu, utilisé pour des tests de division."
parties_dynamiques = diviser_texte_dynamiquement(texte_long)

parties_dynamiques


# création des fichiers insertions et csv

# In[198]:


# Noms des fichiers
input_json_filename = 'articles.json'  # Nom de votre fichier JSON
output_sql_categories_filename = 'insert_categories.sql'
output_sql_articles_filename = 'insert_articles.sql'
output_csv_categories_filename = 'insert_categories.csv'
output_csv_articles_filename = 'insert_articles.csv'

# Ouvrir le fichier JSON pour lecture
with open(input_json_filename, 'r', encoding='utf-8') as json_file:
    categories = json.load(json_file)

# Ouvrir les fichiers SQL et CSV pour écriture
with open(output_sql_categories_filename, 'w', encoding='utf-8') as sql_categories_file, \
     open(output_sql_articles_filename, 'w', encoding='utf-8') as sql_articles_file, \
     open(output_csv_categories_filename, 'w', newline='', encoding='utf-8') as csv_categories_file, \
     open(output_csv_articles_filename, 'w', newline='', encoding='utf-8') as csv_articles_file:

    # CSV Writers
    csv_categories_writer = csv.writer(csv_categories_file)
    csv_articles_writer = csv.writer(csv_articles_file)

    # Écrire les en-têtes pour chaque fichier CSV
    csv_categories_writer.writerow(['ID_Category', 'Name_Category','URL_Category','Description'])
    csv_articles_writer.writerow(['ID_article', 'ID_Category', 'Title','Author', 'CreationDate','Creation_Time', 'Content_Article','URL_Article','Tags'])

#------------initialiser compteurs de catégorie et articles pour faire les références par la suite
    num_cat = 0
    numéro_article = 0
    for category, item in categories.items():
        num_cat += 1
        
        # Referance et description corrigé
        ref_category = f"Cat-{num_cat:02}"
        if categories[category]['desc'] is not None:
            Description_corrected = categories[category]['desc'].replace("'", "''").replace("&","and")
            category_corrected = category.replace("&","and")

        # SQL Insert
        insert_categories = f"INSERT INTO Article_Category (ID_Category,Name_Category,URL_Category,Description_) VALUES ('{ref_category}', '{category_corrected}','{categories[category]['url']}','{Description_corrected}');\n"
        sql_categories_file.write(insert_categories)

        # CSV Insert
        csv_categories_writer.writerow([ref_category, category,categories[category]['url'],categories[category]['desc']])
#--------------------------boucler sur les articles pour traitement       
        for article in categories[category]['articles']:
            numéro_article += 1

#-------------------------diviser le champs date_temps en deux champs date et temps
            date, time = divide_time_date(article['creation_date'])
#-------------------------remplacer les & par and pour oracle, et ' par '' pour oracle également.
            for key in article:
                if key != 'comments':
                    article[key] = article[key].replace("---"," ").replace("'", "''").replace("&","and")
            # Ref et text corrigé
            ref_article = f"Art-{numéro_article:02}"
            text_corrected = article['content']

            # SQL Insert
            insert_articles = f"INSERT INTO Article (ID_Article, ID_Category, Title, Author,Creation_Date,Creation_Time,URL_Article,Tags)VALUES ('{ref_article}', '{ref_category}', '{article['title']}', '{article['author']}', TO_DATE('{date}', 'YYYY-MM-DD'), '{time}', '{article['url']}','{article['tags']}');\n"
            sql_articles_file.write(insert_articles)
            text_parts = diviser_texte_dynamiquement(text_corrected)
#-----------------------diviser le champ texte en plusieurs parties dynamiquement tel que chaque partie à nombre_char < 3500 car en oracle la limite
#-----------------------de caractères par commande est 4000
            for i in range(len(text_parts)):
                if i == 0:
                    insert_articles = f"UPDATE Article SET Content_Article ='{text_parts[i]}' WHERE ID_Article = '{ref_article}';\n"
                else:
                    insert_articles = f"UPDATE Article SET Content_Article = Content_Article || '{text_parts[i]}' WHERE ID_Article = '{ref_article}';\n"
                sql_articles_file.write(insert_articles) 


            # CSV Insert
            csv_articles_writer.writerow([ref_article, ref_category, article['title'], article['author'], date, time, text_corrected, article['url'],article['tags']])
            

