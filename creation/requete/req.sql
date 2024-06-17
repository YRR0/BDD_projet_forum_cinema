-- 1. Requête sur au moins trois tables :
-- Cette requête sélectionne les logins des utilisateurs, les textes des publications, et les noms des catégories.
SELECT u.logins, p.texte, c.nom
FROM projet.Utilisateur u
JOIN projet.Publication p ON u.logins = p.auteur
JOIN projet.Categorie c ON p.categorie = c.nom;

-- 2. Auto Jointure 
-- Cette requête sélectionne les noms des artistes ayant le même sexe et le même nombre d'Oscars.
SELECT a1.nom AS artiste1, a2.nom AS artiste2
FROM projet.Artiste a1
JOIN projet.Artiste a2 ON a1.sexe = a2.sexe AND a1.nb_Oscars = a2.nb_Oscars
WHERE a1.ID_Artiste <> a2.ID_Artiste;

-- Cette requête sélectionne des films du même genre mais avec des titres différents.
SELECT f1.titre, f2.titre AS film_similaire
FROM projet.Film f1
JOIN projet.Film f2 ON f1.genre = f2.genre AND f1.titre != f2.titre;

-- 3. Sous-requête corrélée
-- Cette requête sélectionne les logins des utilisateurs qui sont suivis par au moins un autre utilisateur.
SELECT u.logins
FROM projet.Utilisateur u
WHERE EXISTS (
    SELECT *
    FROM projet.Follow f
    WHERE f.suiveur = u.logins
);

-- 4. Sous-requête dans le FROM :
-- Cette requête sélectionne les logins des utilisateurs et le nombre de followers qu'ils ont.
SELECT logins, nb_followers
FROM (
    SELECT suivi AS logins, COUNT(suiveur) AS nb_followers
    FROM projet.Follow
    GROUP BY suivi
) AS followers;

-- 5. Sous-requête dans le WHERE :
-- Cette requête sélectionne les logins des utilisateurs qui sont suivis par au moins un autre utilisateur.
SELECT logins
FROM projet.Utilisateur
WHERE logins IN (
    SELECT suivi
    FROM projet.Follow
);

-- 6. Agrégats nécessitant GROUP BY et HAVING :
-- Cette requête sélectionne les artistes ayant remporté plus de 9 Oscars, en affichant leur identifiant et le nombre maximal d'Oscars remporté.
SELECT ID_Artiste, MAX(nb_Oscars) AS mx_oscars
FROM projet.Artiste 
GROUP BY ID_Artiste
HAVING MAX(nb_Oscars) > 9
ORDER BY ID_Artiste DESC;

-- 7. Calcul de deux agrégats :
-- Cette requête sélectionne pour chaque réalisateur le nombre maximum d'entrées et le nombre moyen d'entrées de ses films.
SELECT a.nom, MAX(f.nb_Entrees) AS max_entrees, AVG(f.nb_Entrees) AS moy_entrees
FROM projet.Artiste a
JOIN projet.Film f ON a.ID_Artiste = f.ID_Realisateur
GROUP BY a.nom;

-- 8. Jointure externe (LEFT JOIN, RIGHT JOIN ou FULL JOIN) :
-- Cette requête sélectionne le nom de chaque artiste ainsi que le nombre total de réactions associées à cet artiste, même si certains artistes n'ont aucune réaction.
SELECT a.nom, COUNT(r.ID_Utilisateur) AS reactions
FROM projet.Artiste a
LEFT JOIN projet.Reaction r ON a.nom = r.ID_Utilisateur
GROUP BY a.nom;

-- 9. Deux requêtes équivalentes exprimant une condition de totalité :
-- Avec sous-requêtes corrélées :
-- Cette requête sélectionne les logins des utilisateurs qui n'ont aucun follower.
SELECT u.logins
FROM projet.Utilisateur u
WHERE NOT EXISTS (
    SELECT 1
    FROM projet.Follow f
    WHERE f.suivi = u.logins
);

-- Avec agrégation :
-- Cette requête sélectionne les logins des utilisateurs qui n'ont aucun follower.
SELECT u.logins
FROM projet.Utilisateur u
LEFT JOIN projet.Follow f ON u.logins = f.suivi
GROUP BY u.logins
HAVING COUNT(f.suiveur) = 0;

-- 10. Deux requêtes renvoyant des résultats différents à cause de NULLs :
-- La première requête utilise INTERSECT pour trouver les genres qui sont à la fois parent1 et parent2.
SELECT R.parent1 
FROM projet.Sous_Genre AS R
INTERSECT
SELECT S.parent2 
FROM projet.Sous_Genre AS S;

-- La deuxième requête utilise DISTINCT pour trouver les genres qui sont à la fois parent1 et parent2.
SELECT DISTINCT R.parent1
FROM projet.Sous_Genre AS R, projet.Sous_Genre AS S
WHERE R.parent1 = S.parent2;


-- 11. Requête récursive :
-- Cette requête récursive cherche la profondeur des commentaires à partir d'un commentaire spécifique.

WITH RECURSIVE commentairesRecursifs AS (
   select ID_commentaire , auteur,origine_c
   from projet.commentaire where ID_Commentaire = 4
   union all
   select c.id_commentaire , c.auteur, c.origine_c from projet.commentaire as c , commentairesRecursifs
   where c.id_commentaire = commentairesRecursifs.origine_c)
SELECT * FROM commentairesRecursifs;


-- 12. Requête utilisant le fenêtrage :
-- Cette requête trouve, pour chaque mois de l'année 2023, les dix lieux d'événements ayant le plus de succès en termes de nombre de participants.
CREATE VIEW V_Lieux_Participants_Par_Mois AS
SELECT e.lieu, COUNT(i.ID_Utilisateur) AS nb_participants, DATE_TRUNC('month', e.date_e) AS month
FROM projet.Evenement e
JOIN projet.Interesse i ON e.ID_Evenement = i.ID_Evenement
WHERE DATE_PART('year', e.date_e) = 2024
GROUP BY e.lieu, DATE_TRUNC('month', e.date_e);

SELECT v1.lieu, v1.nb_participants, v1.month
FROM V_Lieux_Participants_Par_Mois v1
WHERE (
    SELECT COUNT(*)
    FROM V_Lieux_Participants_Par_Mois v2
    WHERE v2.month = v1.month
    AND v2.nb_participants > v1.nb_participants
) < 10
ORDER BY v1.month, v1.nb_participants DESC;

-- 13. Recommandation d'événements basés sur les événements suivis par les amis :
-- Cette requête recommande des événements basés sur les événements suivis par les amis de l'utilisateur 'colin59'.
WITH Amis AS (
    SELECT suivi
    FROM projet.Follow 
    WHERE suiveur = 'colin59'
),
EvenementsAmis AS (
    SELECT e.ID_Evenement, e.titre, COUNT(i.ID_Utilisateur) AS nb_interesses
    FROM projet.Evenement e
    JOIN projet.Interesse i ON e.ID_Evenement = i.ID_Evenement
    WHERE i.ID_Utilisateur IN (SELECT suivi FROM Amis)
    GROUP BY e.ID_Evenement, e.titre
)
SELECT e.ID_Evenement, e.titre, e.lieu, e.date_e, e.prix, ea.nb_interesses
FROM projet.Evenement e
JOIN EvenementsAmis ea ON e.ID_Evenement = ea.ID_Evenement
ORDER BY ea.nb_interesses DESC
LIMIT 10;

-- 14. Récupérer les événements auxquels un utilisateur est intéressé :
-- Cette requête sélectionne les événements auxquels l'utilisateur 'sydneylee' est intéressé.
SELECT ID_Evenement
FROM projet.Interesse
WHERE ID_Utilisateur = 'sydneylee';

-- 15. Recommandation de publications en fonction des sujets consultés par l'utilisateur :
-- Cette requête recommande des publications basées sur les sujets consultés par l'utilisateur 'michael17'.
SELECT p.*
FROM projet.Publication p
JOIN projet.Hashtag h ON p.ID_Publication = h.ID_Publication
JOIN projet.Historique hi ON h.nom_Sujet = hi.sujet
WHERE hi.utilisateur = 'michael17';

-- 16. Calculer un score de recommandation :
-- Cette requête calcule un score de recommandation pour les événements basés sur la similarité de lieux et d'organisateurs.
WITH UserEvents AS (
    SELECT ID_Evenement
    FROM projet.Interesse
    WHERE ID_Utilisateur = 'sydneylee'
),
SimilarEvents AS (
    SELECT e1.ID_Evenement, e2.ID_Evenement AS SimilarEvent
    FROM projet.Evenement e1
    JOIN projet.Evenement e2 ON e1.lieu = e2.lieu OR e1.organisateur = e2.organisateur
    WHERE e1.ID_Evenement IN (SELECT ID_Evenement FROM UserEvents) AND e1.ID_Evenement != e2.ID_Evenement
),
EventScores AS (
    SELECT SimilarEvent, COUNT(*) AS Score
    FROM SimilarEvents
    GROUP BY SimilarEvent
)
SELECT e.ID_Evenement, e.titre, es.Score
FROM projet.Evenement e
JOIN EventScores es ON e.ID_Evenement = es.SimilarEvent
ORDER BY es.Score DESC
LIMIT 10;

-- 17. Recommander les n meilleurs événements :
-- Cette requête recommande les n meilleurs événements pour l'utilisateur 'sydneylee' en utilisant un score basé sur la similarité de lieux et d'organisateurs.
WITH UserEvents AS (
    SELECT ID_Evenement
    FROM projet.Interesse
    WHERE ID_Utilisateur = 'sydneylee'
),
SimilarEvents AS (
    SELECT e1.ID_Evenement, e2.ID_Evenement AS SimilarEvent
    FROM projet.Evenement e1
    JOIN projet.Evenement e2 ON e1.lieu = e2.lieu OR e1.organisateur = e2.organisateur
    WHERE e1.ID_Evenement IN (SELECT ID_Evenement FROM UserEvents) AND e1.ID_Evenement != e2.ID_Evenement
),
EventScores AS (
    SELECT SimilarEvent, COUNT(*) AS Score
    FROM SimilarEvents
    GROUP BY SimilarEvent
)
SELECT e.ID_Evenement, e.titre, e.lieu, e.date_e, es.Score
FROM projet.Evenement e
JOIN EventScores es ON e.ID_Evenement = es.SimilarEvent
ORDER BY es.Score DESC
LIMIT 10;

-- 18. Recommandation de films basée sur les films aimés par les utilisateurs suivis :
-- Cette requête recommande des films basés sur les films aimés par les utilisateurs suivis par 'sydneylee'.
WITH UtilisateursSuivis AS (
    SELECT suivi
    FROM projet.Follow
    WHERE suiveur = 'sydneylee'
),
PublicationsAimees AS (
    SELECT r.ID_Publication 
    FROM projet.Reaction r
    JOIN projet.Emoji e ON r.ID_Emoji = e.ID_Emoji
    WHERE e.nom = 'like' AND r.ID_Utilisateur IN (SELECT suivi FROM UtilisateursSuivis)
)
SELECT DISTINCT f.*
FROM projet.Film f
JOIN projet.Publication p ON f.titre = p.texte
JOIN PublicationsAimees pa ON p.ID_Publication = pa.ID_Publication;

-- 19. Recommandation d'événements en fonction de l'historique des événements suivis par l'utilisateur :
-- Cette requête sélectionne les événements suivis par l'utilisateur 'nicholasbryant'.
SELECT e.*
FROM projet.Evenement e
JOIN projet.Interesse i ON e.ID_Evenement = i.ID_Evenement
WHERE i.ID_Utilisateur = 'nicholasbryant';

-- 20. Recommandation de publications basée sur les publications aimées par l'utilisateur et son réseau :
-- Cette requête recommande des publications basées sur les publications aimées par l'utilisateur et les utilisateurs qu'il suit.
WITH UtilisateursSuivis AS (
    SELECT suivi
    FROM projet.Follow
    WHERE suiveur = 'sydneylee'
),
PublicationsAimees AS (
    SELECT r.ID_Publication
    FROM projet.Reaction r
    JOIN projet.Emoji e ON r.ID_Emoji = e.ID_Emoji
    WHERE e.nom = 'like' AND (r.ID_Utilisateur = 'sydneylee' OR r.ID_Utilisateur IN (SELECT suivi FROM UtilisateursSuivis))
)
SELECT DISTINCT p.*
FROM projet.Publication p
JOIN PublicationsAimees pa ON p.ID_Publication = pa.ID_Publication;