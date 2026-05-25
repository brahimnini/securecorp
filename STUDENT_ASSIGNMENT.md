# SecureCorp Portal - Énoncé de l'Exercice de Cybersécurité Applicative

## Table des matières
1.  [Présentation Pédagogique](#1-présentation-pédagogique)
2.  [Présentation Technique](#2-présentation-technique)
3.  [Missions des Étudiants](#3-missions-des-étudiants)
4.  [Liste des Vulnérabilités à Corriger](#4-liste-des-vulnérabilités-à-corriger)
5.  [Objectifs de Sécurité](#5-objectifs-de-sécurité)
6.  [Livrables Attendus](#6-livrables-attendus)

## 1. Présentation Pédagogique

### Contexte du Projet
Bienvenue dans le **SecureCorp Portal**, un laboratoire de formation pratique au *Secure Coding*. Dans le monde réel, les développeurs sont souvent confrontés à la tâche d'auditer, de sécuriser et d'améliorer des applications existantes. Ce projet simule un tel scénario en vous fournissant une application web fonctionnelle mais volontairement vulnérable, représentant un portail interne d'entreprise.

### Objectifs Pédagogiques
Cet exercice a pour but de vous immerger dans le processus de sécurisation d'une application web. À travers ce projet, vous apprendrez à :
-   **Auditer** une application web pour identifier les failles de sécurité.
-   **Comprendre** les mécanismes sous-jacents des vulnérabilités courantes.
-   **Développer** des correctifs de sécurité efficaces et robustes.
-   **Appliquer** les principes du *secure coding* pour prévenir de futures vulnérabilités.
-   **Évaluer** l'impact des modifications de code sur la sécurité globale de l'application.

### Rôle des Étudiants
Votre rôle ne sera pas de développer l'application de zéro, mais d'agir en tant qu'auditeurs et développeurs de sécurité. Vous recevrez une application déjà largement développée (la **Version 1 - Vulnérable**). Votre tâche consistera à analyser des parties spécifiques du code, à identifier les vulnérabilités qui y sont cachées, puis à programmer les correctifs de sécurité nécessaires pour transformer cette application en une version sécurisée.

## 2. Présentation Technique

### Architecture Globale
Le SecureCorp Portal est une application web basée sur le micro-framework Python Flask. Elle suit une architecture modulaire, organisée en 
blueprints pour chaque fonctionnalité majeure (authentification, administration, API, tickets, utilisateurs). La persistance des données est gérée par SQLAlchemy avec une base de données SQLite.

### Modules Principaux
-   **`auth/`** : Gère l'authentification des utilisateurs, l'enregistrement, la connexion/déconnexion et la gestion des sessions JWT.
-   **`admin/`** : Contient les fonctionnalités d'administration pour la gestion des utilisateurs, tickets et documents.
-   **`api/`** : Expose des endpoints JSON pour l'accès programmatique aux données.
-   **`tickets/`** : Gère la création, l'affichage et le commentaire des tickets support.
-   **`users/`** : Permet la gestion des profils utilisateurs.
-   **`templates/`** : Contient tous les fichiers HTML (Jinja2) pour l'interface utilisateur.
-   **`static/`** : Héberge les fichiers CSS et JavaScript.

### Technologies Utilisées
-   **Backend** : Python 3, Flask, SQLAlchemy, SQLite.
-   **Frontend** : HTML, CSS, Bootstrap, Jinja2.
-   **Sécurité** : PyJWT, bcrypt.

## 3. Missions des Étudiants

Votre mission principale est de prendre la **Version 1 - Vulnérable** du SecureCorp Portal et de la transformer en une application sécurisée en passant par une étape **Semi-Sécurisée**.

Vous devrez :
1.  **Auditer l'application** : Examiner le code source de la Version 1 pour identifier les vulnérabilités de sécurité. Portez une attention particulière aux commentaires `TODO SECURITY` qui indiquent des zones potentiellement problématiques, sans pour autant vous donner la solution.
2.  **Identifier les vulnérabilités** : Documenter chaque vulnérabilité trouvée, expliquer son fonctionnement, son impact potentiel et les risques qu'elle représente.
3.  **Corriger les failles** : Implémenter les correctifs de sécurité nécessaires pour chaque vulnérabilité identifiée. Vous devrez créer une **Version 2 - Semi-Sécurisée** qui corrige certaines des failles, puis une **Version 3 - Sécurisée** qui intègre toutes les protections nécessaires.
4.  **Améliorer le Secure Coding** : Appliquer les bonnes pratiques de développement sécurisé (validation des entrées, gestion des erreurs, contrôle d'accès, etc.) pour rendre le code plus robuste.

## 4. Liste des Vulnérabilités à Corriger

La **Version 1 - Vulnérable** contient les types de vulnérabilités suivants. Votre tâche est de les trouver et de les corriger. **L'emplacement exact de ces vulnérabilités n'est pas indiqué dans le code.**

-   **IDOR** (Insecure Direct Object Reference) : Problèmes de contrôle d'accès direct aux objets.
-   **XSS stocké** (Cross-Site Scripting) : Injection de scripts malveillants stockés dans la base de données.
-   **XSS réfléchi** (Cross-Site Scripting) : Injection de scripts malveillants via les paramètres d'URL.
-   **CSRF** (Cross-Site Request Forgery) : Attaques où une requête non autorisée est transmise depuis un utilisateur authentifié.
-   **Mauvais contrôle RBAC** (Role-Based Access Control) : Problèmes dans la gestion des permissions basées sur les rôles.
-   **JWT mal sécurisé** : Utilisation d'un secret faible, absence d'expiration ou de validation appropriée du token.
-   **Upload de fichier dangereux** : Permettre l'upload de fichiers malveillants ou l'exécution de code via des fichiers téléchargés.
-   **Validation MIME insuffisante** : Ne pas vérifier correctement le type de fichier lors de l'upload.
-   **Path Traversal** : Accès à des fichiers ou répertoires en dehors du répertoire prévu.
-   **SQL Injection simple** : Injection de code SQL via les entrées utilisateur.
-   **Logs sensibles** : Journalisation d'informations confidentielles ou de débogage en production.
-   **Fuite d'informations de debug** : Affichage d'informations techniques détaillées aux utilisateurs finaux.
-   **Export de données non sécurisé** : Exportation de données sans contrôle d'accès ou avec des informations sensibles.
-   **Validation utilisateur insuffisante** : Mots de passe faibles, formats d'email incorrects, etc.
-   **Mauvaise gestion des erreurs** : Messages d'erreur génériques ou divulgation d'informations sensibles.
-   **Absence de Rate Limiting** : Ne pas limiter le nombre de requêtes pour prévenir les attaques par force brute ou DoS.
-   **Énumération d'utilisateurs** : Possibilité de déterminer si un nom d'utilisateur existe ou non.
-   **Mauvaise validation API** : Absence de validation ou d'autorisation sur les endpoints de l'API.

## 5. Objectifs de Sécurité

Pour chaque vulnérabilité identifiée, vous devrez implémenter les bonnes pratiques suivantes :
-   **Validation des entrées** : Toujours valider et assainir toutes les entrées utilisateur.
-   **Encodage des sorties** : Échapper correctement toutes les données affichées dans les templates HTML.
-   **Contrôle d'accès robuste** : Mettre en œuvre des vérifications d'autorisation strictes pour toutes les actions sensibles et l'accès aux ressources.
-   **Gestion sécurisée des sessions et JWT** : Utiliser des secrets forts, définir des expirations appropriées et valider systématiquement les tokens.
-   **Upload de fichiers sécurisé** : Valider les types de fichiers, les extensions, les contenus et les noms de fichiers. Stocker les fichiers de manière sécurisée.
-   **Prévention des injections** : Utiliser des requêtes préparées ou des ORM pour interagir avec la base de données.
-   **Journalisation sécurisée** : Enregistrer les événements pertinents sans divulguer d'informations sensibles. Gérer la rotation des logs.
-   **Gestion des erreurs** : Afficher des messages d'erreur génériques aux utilisateurs et logger les détails techniques en interne.
-   **Protection CSRF** : Implémenter des tokens CSRF pour toutes les requêtes modifiant l'état.
-   **Rate Limiting** : Mettre en place des mécanismes pour limiter le nombre de requêtes.

## 6. Livrables Attendus

À la fin de cet exercice, vous devrez soumettre :
1.  **Le code corrigé** : Les versions **Semi-Sécurisée** et **Sécurisée** de l'application, avec toutes les vulnérabilités corrigées et les bonnes pratiques implémentées.
2.  **Un rapport de vulnérabilités** : Pour chaque vulnérabilité trouvée dans la Version 1, décrivez :
    -   La vulnérabilité (type, description).
    -   Son emplacement dans le code (fichier, ligne).
    -   Comment elle peut être exploitée.
    -   Son impact potentiel.
3.  **Explication des corrections** : Pour chaque vulnérabilité corrigée, expliquez les modifications apportées au code dans les versions 2 et 3.
4.  **Justification des protections ajoutées** : Expliquez pourquoi les protections implémentées sont efficaces et comment elles préviennent les attaques.

Bonne chance dans votre mission de sécurisation du SecureCorp Portal !
