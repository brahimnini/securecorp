# SecureCorp Portal - Secure Coding Training Lab

## Table des matières
1.  [Introduction](#1-introduction)
2.  [Objectifs Pédagogiques](#2-objectifs-pédagogiques)
3.  [Architecture du Projet](#3-architecture-du-projet)
4.  [Technologies Utilisées](#4-technologies-utilisées)
5.  [Structure des Versions](#5-structure-des-versions)
6.  [Installation et Lancement](#6-installation-et-lancement)
7.  [Dépendances](#7-dépendances)
8.  [Structure du Code](#8-structure-du-code)
9.  [Fonctionnalités Implémentées](#9-fonctionnalités-implémentées)
10. [Vulnérabilités Intégrées (Vue d'ensemble)](#10-vulnérabilités-intégrées-vue-densemble)
11. [Commentaires Pédagogiques](#11-commentaires-pédagogiques)
12. [Exigences de Secure Coding](#12-exigences-de-secure-coding)
13. [Données de Démonstration](#13-données-de-démonstration)

## 1. Introduction

Le projet **SecureCorp Portal** est un laboratoire de formation au *Secure Coding* conçu pour un cours de cybersécurité axé sur la sécurité des applications web. Il ne s'agit pas d'une application CRUD classique, mais d'un environnement réaliste où les étudiants peuvent pratiquer l'audit, l'identification, la correction et l'amélioration du code en matière de sécurité.

L'application simule un portail interne d'entreprise, offrant des fonctionnalités courantes telles que l'authentification, la gestion des utilisateurs, l'upload de fichiers, un tableau de bord administratif, un système de tickets support, une API interne, l'export de données et la journalisation.

## 2. Objectifs Pédagogiques

L'objectif principal de ce projet est de permettre aux étudiants de :
-   Auditer une application web existante.
-   Identifier des vulnérabilités de sécurité courantes.
-   Programmer des correctifs pour ces failles.
-   Améliorer la qualité du code en appliquant les principes du *secure coding*.
-   Comprendre l'impact des vulnérabilités et l'importance des protections.

Les étudiants ne sont pas censés développer l'application de zéro, mais plutôt analyser des parties spécifiques, identifier les problèmes et implémenter les protections nécessaires.

## 3. Architecture du Projet

Le projet est structuré de manière modulaire pour faciliter la compréhension et l'analyse par les étudiants. Il suit une architecture basée sur Flask, avec des blueprints pour organiser les différentes fonctionnalités.

```
securecorp/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── auth/
│   ├── routes.py
│   ├── services.py
│   └── utils.py
│
├── admin/
│   ├── routes.py
│   └── services.py
│
├── api/
│   ├── routes.py
│   └── services.py
│
├── uploads/
│
├── tickets/
│   ├── routes.py
│   └── services.py
│
├── users/
│   ├── routes.py
│   └── services.py
│
├── templates/
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
├── database/
│
├── logs/
│
└── tests/
```

## 4. Technologies Utilisées

Le projet utilise une stack technique spécifique pour rester simple, local et pédagogique :

**Backend :**
-   **Python 3**
-   **Flask** (micro-framework web)
-   **SQLAlchemy** (ORM pour la base de données)
-   **SQLite** (base de données légère et embarquée)

**Frontend :**
-   **HTML**
-   **CSS**
-   **Bootstrap** (framework CSS pour une interface simple et réactive)
-   **Jinja2** (moteur de templates Flask)

**Sécurité :**
-   **PyJWT** (pour la gestion des JSON Web Tokens)
-   **bcrypt** (pour le hachage des mots de passe)

**Interdictions :**
Afin de maintenir la simplicité et la focalisation pédagogique, les technologies suivantes sont explicitement exclues :
-   Frameworks Frontend (React, Vue, Angular)
-   Docker, Kubernetes, Microservices
-   Architectures complexes, Cloud
-   Bases de données externes (Redis, PostgreSQL)

## 5. Structure des Versions

Le projet est fourni en trois versions distinctes, chacune représentant un niveau de sécurité différent :

### Version 1 — VULNERABLE (`v1_vulnerable`)
Cette version contient de nombreuses vulnérabilités de sécurité courantes. Les protections sont minimales ou inexistantes. L'architecture est fonctionnelle mais le code est intentionnellement faible sur certains aspects pour servir de base d'audit aux étudiants.

### Version 2 — SEMI-SECURISEE (`v2_semi_secured`)
Dans cette version, certaines protections ont été ajoutées pour corriger les vulnérabilités les plus évidentes. Cependant, des failles persistent et le *secure coding* n'est que partiellement appliqué. Elle représente une étape intermédiaire dans le processus de sécurisation.

### Version 3 — SECURISEE (`v3_secured`)
Cette version intègre des protections correctement implémentées et applique les principes du *secure coding*. La validation est stricte, le contrôle d'accès basé sur les rôles (RBAC) est sécurisé, les JWT sont correctement gérés, les uploads de fichiers sont sécurisés, une protection CSRF est en place, et la journalisation est propre. Elle sert de référence pour les bonnes pratiques.

## 6. Installation et Lancement

Pour installer et lancer le projet (pour chaque version) :

1.  **Cloner le dépôt :**
    ```bash
    git clone <URL_DU_DEPOT>
    cd securecorp
    ```

2.  **Naviguer vers la version souhaitée :**
    ```bash
    cd v1_vulnerable # ou v2_semi_secured, ou v3_secured
    ```

3.  **Créer un environnement virtuel et installer les dépendances :**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r ../requirements.txt
    ```

4.  **Initialiser la base de données et charger les données de démonstration :**
    ```bash
    python3 seed.py
    ```

5.  **Lancer l'application Flask :**
    ```bash
    flask run
    ```

L'application sera accessible à l'adresse `http://127.0.0.1:5000`.

## 7. Dépendances

Les dépendances du projet sont listées dans `requirements.txt` :
-   `Flask`
-   `Flask-SQLAlchemy`
-   `PyJWT`
-   `bcrypt`
-   `python-dotenv`
-   `Werkzeug`

## 8. Structure du Code

Le code est organisé en modules logiques (auth, admin, api, tickets, users) pour une meilleure maintenabilité et compréhension. Chaque module contient :
-   `routes.py` : Définit les routes Flask et gère la logique de présentation.
-   `services.py` : Contient la logique métier et les interactions avec la base de données.
-   `utils.py` (si nécessaire) : Fonctions utilitaires, décorateurs, etc.

Les templates HTML sont situés dans le dossier `templates/` et les fichiers statiques (CSS, JS) dans `static/`.

## 9. Fonctionnalités Implémentées

Le portail SecureCorp inclut les fonctionnalités suivantes :
-   **Authentification :** Connexion, déconnexion, gestion des sessions (JWT), rôles utilisateur/admin.
-   **Tableau de Bord :** Statistiques simples, activité utilisateur, navigation.
-   **Gestion des Utilisateurs :** Création, modification de profil, suppression (pour les admins), gestion des rôles.
-   **Module Tickets :** Création de tickets, ajout de commentaires, affichage des tickets.
-   **Upload de Fichiers :** Téléchargement de documents, aperçu.
-   **Export de Données :** Exportation de données au format CSV et JSON.
-   **API Interne :** Endpoints JSON pour la récupération des utilisateurs et des tickets.
-   **Logs :** Journalisation des événements applicatifs et d'authentification.

## 10. Vulnérabilités Intégrées (Vue d'ensemble)

Les versions vulnérables du projet intègrent de manière réaliste et discrète une liste de vulnérabilités pédagogiques. L'objectif est que les étudiants les découvrent par l'audit du code et de l'application. Les vulnérabilités sont exploitables et clairement corrigeables.

**Liste non exhaustive des types de vulnérabilités intégrées :**
-   IDOR (Insecure Direct Object Reference)
-   XSS (Cross-Site Scripting) stocké et réfléchi
-   CSRF (Cross-Site Request Forgery)
-   Mauvais contrôle RBAC (Role-Based Access Control)
-   JWT mal sécurisé (faible secret, pas d'expiration)
-   Upload de fichiers dangereux (validation MIME insuffisante, path traversal)
-   SQL Injection simple
-   Fuite d'informations (logs sensibles, debug activé)
-   Validation utilisateur insuffisante (mots de passe faibles, formats d'email)
-   Mauvaise gestion des erreurs
-   Absence de *rate limiting*
-   Énumération d'utilisateurs
-   Mauvaise validation API

Des commentaires `TODO SECURITY` sont insérés dans le code pour indiquer des zones nécessitant une attention en matière de sécurité, sans pour autant révéler directement la solution.

## 11. Commentaires Pédagogiques

Le code est fortement commenté pour des raisons pédagogiques. Les commentaires expliquent :
-   Pourquoi certaines pratiques sont dangereuses.
-   Pourquoi certaines protections sont meilleures.
-   Les impacts de sécurité potentiels.

## 12. Exigences de Secure Coding

Le projet met en œuvre les bonnes pratiques de *secure coding* dans sa version sécurisée, notamment :
-   Utilisation de fonctions séparées et architecture modulaire.
-   Noms de variables et fonctions explicites.
-   `docstrings` pour la documentation du code.
-   Validation centralisée des entrées.
-   Logique claire et facile à suivre.

## 13. Données de Démonstration

Chaque version du projet inclut un script `seed.py` pour initialiser la base de données SQLite avec des données de test (utilisateurs, tickets, documents). Cela permet aux étudiants de lancer l'application rapidement et de commencer l'audit sans avoir à créer manuellement des données. Les mots de passe des utilisateurs de test sont simples dans les versions vulnérables et respectent des critères de complexité dans la version sécurisée.
