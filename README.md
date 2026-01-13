# Projet Web Multiconteneur Docker : Flask + PostgreSQL

## Description
Ce projet illustre une **application web Flask** conteneurisée avec **Docker**, connectée à une **base de données PostgreSQL**.  
L’objectif est de démontrer la compréhension des concepts de Docker et Docker Compose pour un environnement de développement multiconteneur.

L’application comporte :
- Une **page d'accueil** accessible via `/`
- Une **route supplémentaire** `/users` qui retourne les utilisateurs stockés dans PostgreSQL.

---

## Prérequis
- Docker >= 20.x
- Docker Compose >= 1.29
- (Optionnel pour développement local) Python 3.x

---

## Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/votre-utilisateur/mon_projet_web.git
cd mon_projet_web
```
### 2. Lancer les conteneurs avec Docker compose
```bash
docker-compose up -d
```
## Vérification du fonctionnement
### Page d'accueil
 - URL : http://localhost:5000/
 - Résultat attendu :
```bash
Bienvenue sur la page d'accueil !
```

### Liste des utilisateurs
 - URL : http://localhost:5000/users
 - Résultat attendu : JSON des utilisateurs dans PostgreSQL, par exemple :
```json
{
  "users": [
    [1, "Alice"],
    [2, "Bob"]
  ]
}

```
**Remarque :** Pour tester /users, vous devez ajouter des utilisateurs dans la base PostgreSQL :
```bash
docker-compose exec db psql -U user -d mydb
```
Puis dans psql :
```sql
CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(50));
INSERT INTO users (name) VALUES ('Alice'), ('Bob');
```

## Structure du projet
```text
eval_docker1/
├── app/
│   ├── app.py           # Application Flask
│   ├── requirements.txt # Dépendances Python
│   └── Dockerfile       # Image Docker de l'application
├── docker-compose.yml   # Déploiement multiconteneur
└── README.md
```
 - Dockerfile : image Python légère, installation des dépendances, copie du code source, exposition du port 5000. 
 - docker-compose.yml : orchestre deux services (web + db) et un volume pour la persistance des données PostgreSQL.

