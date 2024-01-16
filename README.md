# Scrapping_TechCrunch

## Nom du Projet

Scrapping des catégories et articles du site web TechCrunch et création d'une petite api.

## Table des matières

- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Captures d'écran](#captures-décran)
- [Prérequis](#prérequis)
- [Installation](#installation)
  
## Aperçu

Ce projet est une solution complète pour le scraping, le stockage, et la visualisation de données d'articles de TechCrunch, un site web leader dans l'actualité technologique. Il a été conçu pour récupérer des articles en fonction de leurs catégories (comme la crypto, les applications, etc.) et les stocker dans une base de données choisie pour une analyse et une visualisation ultérieures. Le projet comprend également un prototype de dashboard pour une représentation visuelle des données, ainsi qu'une API pour faciliter l'accès aux données stockées.

## Fonctionnalités

- **Scraping Dynamique :** 
  Le projet intègre un outil de scraping capable de récupérer les articles de différentes catégories de TechCrunch.
- **Stockage de Données :** 
  Les articles récupérés sont utilisés pour créer deux fichier .sql d'insertion de catégories et articles qui devront être executé par la suite pour insérer dans la base de données. catégories -> articles.
- **Dashboard Interactif :** 
  Un tableau de bord est mis à disposition pour visualiser et analyser les données des articles.
- **API :** 
  Le projet inclut une API permettant une visualisation de la base de données.
- **Documentation Détaillée :** 
  Le projet est accompagné d'une documentation complète, facilitant sa prise en main et son utilisation.


## Prérequis

- selenium (version 4.15.2 ou supérieure)
- streamlit (version 1.30.0 ou supérieure)
- seaborn (version 0.13.1 ou supérieure)
- pandas (version 0.3.1 ou supérieure)
- cx_Oracle (version 8.3.0 ou supérieure)
- matplotlib (version 3.8.2 ou supérieure)
- google chrome (version 114.0.5735.90 ou inférieure)
- Oracle Database (CMD ou IDE), sqldeveloper a été utilisé ici
- Python (version 3.10.4 ou supérieure)
- (optionnel) jupyter notebook pour lire le fichier .ipynb 

## Installation

Pour installer et configurer ce projet localement, suivez les étapes ci-dessous :

1. **Cloner le Répertoire** :
   - Ouvrez un terminal et clonez le répertoire du projet en utilisant :
     ```
     git clone [URL_DU_REPERTOIRE_DU_PROJET]
     ```
   - Accédez au répertoire du projet :
     ```
     cd Scrapping_TechCrunch
     ```

2. **Configuration de l'Environnement** :
   - Assurez-vous que Python est installé sur votre machine. Vous pouvez le télécharger depuis [le site officiel de Python](https://www.python.org/downloads/).
   - Il est recommandé d'utiliser un environnement virtuel pour gérer les dépendances. Créez un environnement virtuel en exécutant :
     ```
     python -m venv venv
     ```
   - Activez l'environnement virtuel :
     - Sur Windows :
       ```
       .\venv\Scripts\activate
       ```
     - Sur Unix ou MacOS :
       ```
       source venv/bin/activate
       ```

3. **Installation des Dépendances** :
   - Installez toutes les dépendances nécessaires en utilisant pip :
     ```
     pip install  selenium
     pip install  streamlit
     pip install  seaborn
     pip install  matplotlib
     pip install  pandas
     pip install  cx_Oracle
     ```

4. **Configuration de la Base de Données** :
   - Assurez-vous que Oracle Database est installé et configuré sur votre machine.
   - Créez une nouvelle base de données ou utilisez une existante pour stocker les données scrapées.
   - Modifiez les fichiers de configuration du projet pour pointer vers votre base de données.

5. **(Optionnel) Lancer le Scraper** :
   - Exécutez le script de scraping pour commencer à récupérer les données :
     ```
     python Web_Scrapping.py
     ```
6. **Exécuter les scripts d'insertions** :
   Suivre les étapes suivantes :
   - Exécutez le script de création de tables table_creation.sql
   - Exécuter le script d'insertion insert_categories.sql
   - Exécuter le script d'insertion insert_articles.sql

8. **Démarrage de l'API** :
   - Lancez l'API pour accéder aux données stockées :
     ```
     streamlit run app.py
     ```

9. **(Optionnel) Jupyter Notebook** :
   - Si vous souhaitez utiliser Jupyter Notebook pour visualiser ou analyser les données, assurez-vous qu'il est installé :
     ```
     pip install notebook
     ```
   - Lancez Jupyter Notebook :
     ```
     jupyter notebook
     ```

Vous pouvez maintenant utiliser le projet pour scraper, stocker et visualiser les données d'articles de TechCrunch !
