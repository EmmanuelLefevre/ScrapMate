# SCRAPMATE

## SOMMAIRE
- [INTRODUCTION](#introduction)
- [API](#api)
  - [Installer Python](#installer-python)
  - [Librairies](#librairies)
  - [Installation](#installation)
- [CHROME EXTENSIONS SETTINGS](#chrome-extensions-settings)
- [LIENS UTILES](#liens-utiles)

## INTRODUCTION
Dans un monde numérique où l'information en ligne est omniprésente, l'accès rapide et structuré aux données est devenu essentiel pour les développeurs, les analystes de données et les créateurs de contenu. C'est dans ce contexte qu'intervient ScrapMate, une extension Chrome conçue pour simplifier et automatiser le processus de récupération du contenu HTML d'une page web.  
L'objectif principal de cette extension est de permettre aux utilisateurs d'extraire rapidement des données brutes ou structurées depuis n'importe quelle page web. ScrapMate offre un gain de temps considérable en rendant le scraping accessible, même pour les utilisateurs ayant peu ou pas d'expérience technique.  
Grâce à ScrapMate, l'utilisateur peut exporter les données dans le format JSON, le tout directement depuis son navigateur.  
En un simple clic, ScrapMate transforme la complexité du scraping en une opération rapide, pratique et sans effort.  

## API
### Installer Python
[Télécharger Python 3.13.1](https://www.python.org/downloads/)

- Vérifier l'installation de Python
```bash
python --version
```
- Vérifier l'installation de Pip
```bash
pip --version
```
### Librairies
- Flask
- Flask-cors
- Beautifulsoup4
- Requests

### Installation
1. Installer les librairies (en local dans python)
```bash
pip install -r api/requirements.txt
```
2. Vérifier l'installation des librairies
```bash
pip list
```
3. Créer un .env à partir du .env.template et changer **MANUELLEMENT** les valeurs pertinentes
```bash
cp api/.env.template api/.env
```
4. Lancer l'application python
```bash
python api/app.py
```

## CHROME EXTENSIONS SETTINGS
1. Activer mode développeur
2. Repérer le bouton "Charger l'extension non empaquetée"

![Chrome extension settings](https://github.com/EmmanuelLefevre/MarkdownImg/blob/main/chrome_settings.png)

3. Ouvrir l'URL ci dessous dans le navigateur Chrome
```bash
chrome://extensions/
```
4. Vérifier les permissions d'extension Chrome
```bash
chrome://settings/content/notifications
```
5. Ajouter/Bloquer permission de notifications
```bash
chrome-extension://<id>
```
```bash
chrome-extension://mphajpdnlknfhohmjkdkljjjkgdfello
```
![Chrome extension id](https://github.com/EmmanuelLefevre/MarkdownImg/blob/main/chrome_extension_id.png)

6. Accéder aux requêtes réseau du service worker

![Chrome extension requête](https://github.com/EmmanuelLefevre/MarkdownImg/blob/main/chrome_extension_requête.png)

## LIENS UTILES
[Chrome extension documentation](https://developer.chrome.com/docs/extensions/reference?hl=fr)  

[Manifest documentation](https://developer.chrome.com/docs/extensions/reference/manifest?hl=fr)  

[Chrome permission](https://developer.chrome.com/docs/extensions/reference/api/permissions?hl=fr)  

***

⭐⭐⭐ I hope you enjoy it, if so don't hesitate to leave a like on this repository and on the [Dotfiles](https://github.com/EmmanuelLefevre/Dotfiles) one (click on the "Star" button at the top right of the repository page). Thanks 🤗
