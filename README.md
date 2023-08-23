# Weefo - Application de Gestion de Livraisons

Weefo est une application de gestion de livraisons qui permet aux administrateurs, livreurs et clients de gérer efficacement le processus de livraison.

## Fonctionnalités

- **Admin :** Les administrateurs peuvent gérer les livreurs, les clients et les livraisons.
- **Livreur :** Les livreurs peuvent consulter et effectuer des livraisons.
- **Client :** Les clients peuvent demander une livraison et suivre leur historique de livraison.

## Installation

1. Clonez ce dépôt :
git clone https://github.com/SyRachid/Weefo.git

2. Accédez au répertoire du projet :
cd Weefo



3. Installez les dépendances :
pip install -r requirements.txt



## Configuration

- Configurez votre base de données en modifiant les paramètres de connexion dans `connect.py`.
- creer les tables en exécutant le fichier 'create_tables.py' après avoir configuré votre base de données

## Utilisation

- Exécutez l'application :
python main.py
- Login via un des utilisateurs dont les informations de connexiont  se trouveront dans votre base de données


## Tests

- Pour exécuter les tests, utilisez la commande suivante :
python -m pytest tests/


## Conception et Implémentation

Ce projet a été développé en suivant les étapes suivantes :

1. Conception des classes et des modèles de données pour les administrateurs, livreurs, clients et livraisons.
2. Mise en place de la base de données en utilisant SQLAlchemy.
3. Implémentation des fonctionnalités d'authentification et de gestion des utilisateurs.
4. Création de fonctions pour la gestion des livraisons par les livreurs.
5. Mise en place de tests unitaires pour chaque fonctionnalité.

## Intégration Continue

Ce projet utilise GitHub Actions pour l'intégration continue. Les tests sont automatiquement déclenchés à chaque modification du code source.

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, suivez les instructions dans [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

-Concepteurs:
@SyRachid et @Reine2001

© 
