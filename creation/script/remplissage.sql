\copy projet.Artiste(ID_Artiste, nom, sexe, nb_Oscars) FROM 'CSV/ressources/artistes.csv' DELIMITER ',' CSV HEADER;
\copy projet.Utilisateur(logins, pseudo, mdp, anniversaire, ID_Artiste) FROM 'CSV/ressources/utilisateurs.csv' DELIMITER ',' CSV HEADER;
 \copy projet.Categorie(nom) FROM 'CSV/ressources/categories.csv' DELIMITER ',' CSV HEADER;
\copy projet.Publication(ID_Publication, texte, date_p, auteur, categorie) FROM 'CSV/ressources/publications.csv' DELIMITER ',' CSV HEADER;
--\copy projet.Commentaire(ID_Commentaire, texte, auteur, origine_p, origine_c) FROM 'CSV/ressources/commentaires.csv' DELIMITER ',' CSV HEADER;
\copy projet.Emoji(ID_Emoji, nom) FROM 'CSV/ressources/emoji.csv' DELIMITER ',' CSV HEADER;
\copy projet.Reaction(ID_Utilisateur, ID_Publication, ID_Emoji) FROM 'CSV/ressources/reactions.csv' DELIMITER ',' CSV HEADER;
\copy projet.Sujet(nom) FROM 'CSV/ressources/sujets.csv' DELIMITER ',' CSV HEADER;
\copy projet.Hashtag(ID_Publication, nom_Sujet, date_h) FROM 'CSV/ressources/hashtags.csv' DELIMITER ',' CSV HEADER;
\copy projet.Evenement(ID_Evenement, titre, lieu, date_e, prix, nbPlaces, annonce, organisateur) FROM 'CSV/ressources/evenements.csv' DELIMITER ',' CSV HEADER;
\copy projet.Evenement_Passe(ID_Archive, programme, nb_Participants, lien, ID_Evenement) FROM 'CSV/ressources/evenements_passes.csv' DELIMITER ',' CSV HEADER;

\copy projet.Interesse(ID_Evenement, ID_Utilisateur, participe) FROM 'CSV/ressources/interesse.csv' DELIMITER ',' CSV HEADER;

\copy projet.Genre(nom) FROM 'CSV/ressources/genres.csv' DELIMITER ',' CSV HEADER;
\copy projet.Film(titre, ID_Realisateur, nb_Oscars, nb_Entrees, annee, genre) FROM 'CSV/ressources/films.csv' DELIMITER ',' CSV HEADER;
\copy projet.Acteur(titre_j, realisateur, acteur) FROM 'CSV/ressources/acteurs.csv' DELIMITER ',' CSV HEADER;
\copy projet.Groupe(ID_Groupe, nom, type_g, createur) FROM 'CSV/ressources/groupes.csv' DELIMITER ',' CSV HEADER;
\copy projet.Membres(groupe, logins) FROM 'CSV/ressources/membres.csv' DELIMITER ',' CSV HEADER;
\copy projet.Follow(suivi, suiveur) FROM 'CSV/ressources/follow.csv' DELIMITER ',' CSV HEADER;
\copy projet.Historique(utilisateur, sujet, date_h) FROM 'CSV/ressources/historique.csv' DELIMITER ',' CSV HEADER;
