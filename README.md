# Padam Test


## Présupposés manquant
- Module googlemaps dans un fichier requirements.txt
- La page par défaut `http://localhost:8000/` est en 404
- La clé d'API Googlemaps est invalid
- Absence d'information sur la voiture louée
- Absence d'un module de paiement
- Absence d'une gestion de compte pour ajouter ses informations de facturations, de paiements etc...
- Absence de vérification du permis de conduire
- Pas d'indication sur l'endroit où récupérer la voiture
- Absence des pages légales (CGV, conditions générales de ventes etc...)
- Absence d'aide au client (contact, FAQ etc...)
- Aucune verification sur les adresses données
- L'utilisateur ne peux pas choisir la date de réservation
- Une voiture est assignée sans vérifier si elle est disponible avant
- Le multi-langue n'est pas présent
- Très peu de message d'erreur


## Refactoring

#### Organisation
Dans le but d'avoir une structure claire et ordonnée, toutes les apps ont été mises dans un dossier apps. Pour que les apps soient toujours chargées par Django, on ajoute une variable `APPS_DIR` qu'on inclu au path dans le fichier `manage.py`
De cette manière le fonctionnement de Django reste intact mais l'architecture est mieux structurée et scalable
- Déplacement de toutes les apps sous un dossier apps
- Ajout d'un dossier var pour mettre tous les fichiers à manipuler
- Ajout d'un dossier doc pour tous les fichiers de conf
- Ajout d'un dossier public qui contient tous les fichiers public, c'est à dire les fichiers HTML/JS/CSS & IMG
- Ajout d'un fichier helpers qui contient toutes les fonctions indépendantes et réutilisables

#### URLS
Dans le but de garder une cohérence entre tous les models, les listes d'objet seront de la forme `model/list` et la page de détail `model/detail`
- La page par défault `/` indique les différentes URLs d'accès du projet. L'URL admin a volontairement été enlevée de la liste affichée afin de garantir une sécurité

#### Encodage
- Ajout de l'encodage UTF-8 en haut de chaque fichiers qui ont des caractères non ascii
- Régénération des apps via manage.py startapp pour mettre le bon header UTF8 et éviter les soucis liés au caractères non ASCII

#### Norme PEP8
Afin d'avoir des fichiers propres et uniforme, la norme PEP8 doit être respectée. Tous les fichiers ont été modifiés dans le but d'être conforme.

#### Views
Pour les views, l'utilisation des `class-based-views` permet de générer ses vues plus rapidement mais aussi et surtout lorsque celle-ci doivent afficher des données d'un model.
Beaucoup d'éléments deviennent génériques et facile à maintenir.

Les templates ont ainsi été adaptés à cette nouvelle architecture.
Voici les cbv utilisés:
- DetailView
- ListView
- DeleteView
- CreateView
- FormView

Les contrôle sur les champs sont mal gérés, par exemple si je met une mauvaise adresse, la fonction get_duration est en erreur et provoque une erreur 500. Toute une partie gestion d'erreur a été ajouté

#### Models
- Dans le model Booking, la date et l'heure ont été séparé pour plus de contrôle et pour une meilleure gestion côté formulaire

#### Apps
Les apps sont trop imbriqués entre elles, par exemple le login se retrouve dans l'app booking. Le but d'une app est d'être réutilisable

- Ajout d'un app `Sign` qui gère le sign in, sign up et sign out
- Pour plus de clareté et permettre des les réutiliser dans d'autres apps, les apps ne contiennent plus les dossiers templates, ceux-ci seront placés dans le dossier public qui contient les fichiers html desormais

#### Import
Suppression de tous les imports *. Cette pratique n'est pas propre, non sécurisée et inclus énorméménet de dépendance non utilisées ce qui nuit au performance.

#### HTLM / CSS
Le HTML et CSS ne respectent pas les règles W3C. Un refactoring global a été effectué sur tous fichiers templates.

Un framework CSS / JS a été ajouté pour donner une meilleur lisibilité à l'ensemble

## Outils utilisés
- PyCharm comme IDE
- Python 2.7.12
- Materializecss

## Temps de réalisation
Commencé le `01/07/2017 à 19h30`

Fini le `02/07/2017 à 19h00`
