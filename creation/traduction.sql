DROP SCHEMA IF EXISTS projet CASCADE;
CREATE SCHEMA projet;

DROP TABLE IF EXISTS projet.Utilisateur;
DROP TABLE IF EXISTS projet.Publication;
DROP TABLE IF EXISTS projet.Categorie;
DROP TABLE IF EXISTS projet.Commentaire;
DROP TABLE IF EXISTS projet.Sujet;
DROP TABLE IF EXISTS projet.Hashtag;
DROP TABLE IF EXISTS projet.Emoji;
DROP TABLE IF EXISTS projet.Evenement;
DROP TABLE IF EXISTS projet.Reaction;
DROP TABLE IF EXISTS projet.Evenement_passe;
DROP TABLE IF EXISTS projet.Interesse;
DROP TABLE IF EXISTS projet.Artiste;
DROP TABLE IF EXISTS projet.Film;
DROP TABLE IF EXISTS projet.Acteur;
DROP TABLE IF EXISTS projet.Genre;
DROP TABLE IF EXISTS projet.Groupe;
DROP TABLE IF EXISTS projet.Membres;
DROP TABLE IF EXISTS projet.Follow;
DROP TABLE IF EXISTS projet.Historique;


--certains noms d'attribut comme date, type ou login sont prédéfinis, 
--on choisi donc de les renommer date_premiereLettreDeLaTable, type_premiereLettreDeLaTable et logins 

CREATE TABLE projet.Artiste (
    ID_Artiste SERIAL PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    sexe VARCHAR (10) CHECK (sexe IN ('feminine', 'masculine')), 
    nb_Oscars INT CHECK (nb_Oscars >=0)
);

CREATE TABLE projet.Categorie (
    nom VARCHAR(30) PRIMARY KEY
);

CREATE TABLE projet.Utilisateur (
    logins VARCHAR(30) PRIMARY KEY,
    pseudo VARCHAR(30) NOT NULL,
    mdp VARCHAR(30) NOT NULL,
    anniversaire DATE,
    ID_Artiste INTEGER,
    FOREIGN KEY (ID_Artiste) REFERENCES projet.Artiste(ID_Artiste) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE projet.Publication (
    ID_Publication SERIAL PRIMARY KEY,
    texte VARCHAR(140),
    date_p DATE NOT NULL,
    auteur VARCHAR(30) NOT NULL,
    categorie VARCHAR(30) NOT NULL,
    FOREIGN KEY (auteur) REFERENCES projet.Utilisateur(logins) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (categorie) REFERENCES projet.Categorie(nom) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE projet.Commentaire (
    ID_Commentaire SERIAL PRIMARY KEY,
    texte VARCHAR(140),
    auteur VARCHAR(30) NOT NULL,
    origine_p INTEGER NOT NULL,
    origine_c INTEGER, 
    FOREIGN KEY (auteur) REFERENCES projet.Utilisateur(logins) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (origine_p) REFERENCES projet.Publication(ID_Publication) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (origine_c) REFERENCES projet.Commentaire(ID_Commentaire) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE projet.Emoji (
    ID_Emoji SERIAL PRIMARY KEY,
    nom VARCHAR(30)
);

CREATE TABLE projet.Reaction (
    ID_Utilisateur VARCHAR(30),
    ID_Publication INTEGER,
    ID_Emoji INTEGER NOT NULL,
    PRIMARY KEY (ID_Utilisateur, ID_Publication),
    FOREIGN KEY (ID_Utilisateur) REFERENCES projet.Utilisateur(logins) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ID_Publication) REFERENCES projet.Publication(ID_Publication) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ID_Emoji) REFERENCES projet.Emoji(ID_Emoji)
);

CREATE TABLE projet.Sujet (
    nom VARCHAR(30) PRIMARY KEY
);

CREATE TABLE projet.Hashtag (
    ID_Publication INTEGER,
    nom_Sujet VARCHAR(30),
    date_h DATE NOT NULL,
    PRIMARY KEY (ID_Publication, nom_Sujet),
    FOREIGN KEY (ID_Publication) REFERENCES projet.Publication(ID_Publication) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (nom_Sujet) REFERENCES projet.Sujet(nom)
);

CREATE TABLE projet.Evenement (
    ID_Evenement SERIAL PRIMARY KEY,
    titre VARCHAR(50) NOT NULL,
    lieu VARCHAR(30),
    date_e DATE,
    prix DECIMAL(5,2) CHECK (prix >=0),
    nbPlaces INT CHECK (nbPlaces >=0),
    annonce INTEGER NOT NULL,
    organisateur VARCHAR(30) NOT NULL,
    FOREIGN KEY (annonce) REFERENCES projet.Publication(ID_Publication) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (organisateur) REFERENCES projet.Utilisateur(logins) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (annonce)
);

CREATE TABLE projet.Evenement_Passe (
    ID_Archive SERIAL PRIMARY KEY,
    programme TEXT,
    nb_Participants INT CHECK (nb_Participants >=0),
    lien VARCHAR (100),
    ID_Evenement INTEGER NOT NULL,
    FOREIGN KEY (ID_Evenement) REFERENCES projet.Evenement(ID_Evenement) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (ID_Evenement)
);

CREATE TABLE projet.Interesse (
    ID_Evenement INTEGER,
    ID_Utilisateur VARCHAR(30),
    participe BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (ID_Evenement, ID_Utilisateur),
    FOREIGN KEY (ID_Evenement) REFERENCES projet.Evenement(ID_Evenement) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ID_Utilisateur) REFERENCES projet.Utilisateur(logins) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE projet.Genre (
    nom VARCHAR(30) PRIMARY KEY
);

CREATE TABLE projet.Sous_Genre (
    nom VARCHAR(30) PRIMARY KEY,
    parent1 VARCHAR(30),
    parent2 VARCHAR(30),
    FOREIGN KEY (parent1) REFERENCES projet.Genre(nom),
    FOREIGN KEY (parent2) REFERENCES projet.Genre(nom)
);

CREATE TABLE projet.Film (
    titre VARCHAR(30),
    ID_Realisateur INTEGER,
    nb_Oscars INT CHECK (nb_Oscars >=0),
    nb_Entrees INT  CHECK (nb_Entrees >=0),
    annee INT,
    genre VARCHAR(30),
    PRIMARY KEY (titre, ID_Realisateur),
    FOREIGN KEY (ID_Realisateur) REFERENCES projet.Artiste(ID_Artiste),
    FOREIGN KEY (genre) REFERENCES projet.Genre(nom)
);

CREATE TABLE projet.Acteur (
    titre_j VARCHAR(30),
    realisateur INTEGER,
    acteur INTEGER,
    PRIMARY KEY (titre_j, realisateur, acteur),
    FOREIGN KEY (titre_j,realisateur) REFERENCES projet.Film(titre,ID_Realisateur),
    FOREIGN KEY (acteur) REFERENCES projet.Artiste(ID_Artiste)
);

CREATE TABLE projet.Groupe (
    ID_Groupe SERIAL PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    type_g VARCHAR(30) CHECK (type_g IN ('club','presse', 'studio', 'festival', 'cinema')),
    createur VARCHAR(30) NOT NULL,
    FOREIGN KEY (createur) REFERENCES projet.Utilisateur(logins) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE projet.Membres (
    groupe INTEGER,
    logins VARCHAR(30),
    PRIMARY KEY (groupe, logins),
    FOREIGN KEY (groupe) REFERENCES projet.Groupe(ID_Groupe) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (logins) REFERENCES projet.Utilisateur(logins) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE projet.Follow (
    suivi VARCHAR(30),
    suiveur VARCHAR(30),
    PRIMARY KEY (suivi, suiveur),
    FOREIGN KEY (suivi) REFERENCES projet.Utilisateur(logins) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (suiveur) REFERENCES projet.Utilisateur(logins) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE projet.Historique (
    utilisateur VARCHAR(30),
    sujet VARCHAR(30),
    date_h DATE,
    PRIMARY KEY (utilisateur, sujet, date_h),
    FOREIGN KEY (utilisateur) REFERENCES projet.Utilisateur(logins) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sujet) REFERENCES projet.Sujet(nom)
);


