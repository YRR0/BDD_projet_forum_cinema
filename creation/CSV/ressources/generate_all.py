from faker import Faker
import csv
import random

fake = Faker()

def ecrire_donnees_dans_csv(donnees, nom_fichier, entetes):
    with open(nom_fichier, mode='w', newline='', encoding='utf-8') as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(entetes)
        writer.writerows(donnees)
    print(f"Le fichier {nom_fichier} a été généré avec succès.")

# Générer des ensembles de données pour chaque table
noms_utilisateurs = {fake.user_name() for _ in range(100)}
textes_publications = {fake.sentence(nb_words=10) for _ in range(100)}
noms_categories = {fake.word() for _ in range(100)}
textes_commentaires = {fake.sentence(nb_words=10) for _ in range(100)}
noms_emoji = {fake.word() for _ in range(100)}
noms_sujets = {fake.word() for _ in range(100)}
noms_hashtags = {fake.word() for _ in range(100)}
titres_evenements = {fake.sentence(nb_words=5) for _ in range(100)}
noms_artistes = {fake.word() for _ in range(100)}
titres_films = {fake.word() for _ in range(100)}
noms_genres = {fake.word() for _ in range(100)}
noms_groupes = {fake.word() for _ in range(100)}
#noms_membres = {fake.word() for _ in range(100)}
noms_suiveurs = {fake.user_name() for _ in range(100)}
noms_sujets_historique = {fake.word() for _ in range(100)}



# Fonctions de génération de données pour chaque table

def generer_utilisateur(): 
    donnees_utilisateurs = {(nom, fake.user_name(), fake.password(length=10), fake.date_of_birth(minimum_age=18, maximum_age=60), fake.random_int(min=1, max=100)) for nom in noms_utilisateurs}
    return donnees_utilisateurs

def generer_publication():
     # Utiliser une liste pour stocker les identifiants uniques
    ids_publications = list(range(1, 101))
    # Mélanger la liste pour obtenir un ordre aléatoire des identifiants
    random.shuffle(ids_publications)
    # Générer les données de publication avec des identifiants uniques
    donnees_publications = [(id_pub, fake.sentence(nb_words=10), fake.word(), fake.word(), fake.word(), fake.date_time_between(start_date='-1y', end_date='now'), nom_u, nom_c) for id_pub, texte,nom_u, nom_c in zip(ids_publications, textes_publications,noms_utilisateurs, noms_categories)]
    
    return donnees_publications

def generer_categorie():
    donnees_categories = {(nom,) for nom in noms_categories}
    return donnees_categories

def generer_commentaire():
    donnees_commentaires = {(texte, fake.random_element(elements=noms_utilisateurs), fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)) for texte in textes_commentaires}
    return donnees_commentaires

def generer_reaction():
    donnees_reactions = {(fake.random_element(elements=noms_utilisateurs), fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)) for _ in range(100)}
    return donnees_reactions

def generer_emoji():
    donnees_emoji = {(nom,) for nom in noms_emoji}
    return donnees_emoji

def generer_sujet():
    donnees_sujets = {(nom,) for nom in noms_sujets}
    return donnees_sujets

def generer_hashtag():
    donnees_hashtags = {(fake.random_int(min=1, max=100), nom, fake.date_time_between(start_date='-1y', end_date='now')) for nom in noms_hashtags}
    return donnees_hashtags

def generer_evenement():
    donnees_evenements = {(titre, fake.word(), fake.date_time_between(start_date='now', end_date='+1y'), round(random.uniform(0, 1000), 2), fake.random_int(min=0, max=100), fake.random_int(min=1, max=100), fake.random_element(elements=noms_utilisateurs)) for titre in titres_evenements}
    return donnees_evenements

def generer_artiste():
    donnees_artistes = [(i, nom, random.choice(['feminine', 'masculine']), fake.random_int(min=0, max=10)) for i, nom in enumerate(noms_artistes, start=1)]
    return donnees_artistes


def generer_film():
    donnees_films = {(titre, fake.random_int(min=1, max=100), fake.random_int(min=0, max=10), fake.random_int(min=0, max=1000000), fake.random_int(min=1900, max=2022), fake.word()) for titre in titres_films}
    return donnees_films

def generer_genre():
    donnees_genres = {(nom, fake.word(), fake.word()) for nom in noms_genres}
    return donnees_genres

def generer_groupe():
    donnees_groupes = {(nom, random.choice(['club','presse', 'studio', 'festival', 'cinema']), fake.word() , fake.random_element(elements=noms_utilisateurs)) for nom in noms_groupes}
    return donnees_groupes

def generer_membres():
    donnees_membres = { nom for nom in noms_utilisateurs}
    return donnees_membres

def generer_follow():
    donnees_follow = {(fake.random_element(elements=noms_utilisateurs), fake.random_element(elements=noms_suiveurs)) for _ in range(100)}
    return donnees_follow

def generer_historique():
    donnees_historique = {(fake.random_element(elements=noms_utilisateurs), nom, fake.date_time_between(start_date='-1y', end_date='now')) for nom in noms_sujets_historique}
    return donnees_historique

# Générer les données pour chaque table
donnees_utilisateurs = generer_utilisateur()
donnees_publications = generer_publication()
donnees_categories = generer_categorie()
donnees_commentaires = generer_commentaire()
donnees_reactions = generer_reaction()
donnees_emoji = generer_emoji()
donnees_sujets = generer_sujet()
donnees_hashtags = generer_hashtag()
donnees_evenements = generer_evenement()
donnees_artistes = generer_artiste()
donnees_films = generer_film()
donnees_genres = generer_genre()
donnees_groupes = generer_groupe()
donnees_membres = generer_membres()
donnees_follow = generer_follow()
donnees_historique = generer_historique()

# Écrire les données dans les fichiers CSV
ecrire_donnees_dans_csv(donnees_utilisateurs, 'utilisateurs.csv', ['logins','pseudo', 'mdp', 'anniversaire', 'ID_Artiste'])
ecrire_donnees_dans_csv(donnees_publications, 'publications.csv', ['ID_Publication', 'texte', 'sujet1', 'sujet2', 'sujet3', 'date_p', 'auteur', 'categorie'])
ecrire_donnees_dans_csv(donnees_categories, 'categories.csv', ['nom'])
ecrire_donnees_dans_csv(donnees_commentaires, 'commentaires.csv', ['ID_Commentaire', 'texte', 'auteur', 'origine_p', 'origine_c'])
ecrire_donnees_dans_csv(donnees_reactions, 'reactions.csv', ['ID_Utilisateur', 'ID_Publication', 'ID_Emoji'])
ecrire_donnees_dans_csv(donnees_emoji, 'emoji.csv', ['ID_Emoji', 'nom'])
ecrire_donnees_dans_csv(donnees_sujets, 'sujets.csv', ['nom'])
ecrire_donnees_dans_csv(donnees_hashtags, 'hashtags.csv', ['ID_Publication', 'nom_Sujet', 'date_h'])
ecrire_donnees_dans_csv(donnees_evenements, 'evenements.csv', ['ID_Evenement', 'titre', 'lieu', 'date_e', 'prix', 'nbPlaces', 'annonce', 'organisateur'])
ecrire_donnees_dans_csv(donnees_artistes, 'artistes.csv', ['ID_Artiste', 'nom', 'sexe', 'nb_Oscars'])
ecrire_donnees_dans_csv(donnees_films, 'films.csv', ['titre', 'ID_Realisateur', 'nb_Oscars', 'nb_Entrees', 'annee', 'genre'])
ecrire_donnees_dans_csv(donnees_genres, 'genres.csv', ['nom', 'parent1', 'parent2'])
ecrire_donnees_dans_csv(donnees_groupes, 'groupes.csv', ['ID_Groupe', 'nom', 'type_g', 'createur'])
ecrire_donnees_dans_csv(donnees_membres, 'membres.csv', ['groupe', 'logins'])
ecrire_donnees_dans_csv(donnees_follow, 'follow.csv', ['suivi', 'suiveur'])
ecrire_donnees_dans_csv(donnees_historique, 'historique.csv', ['utilisateur', 'sujet', 'date_h'])
