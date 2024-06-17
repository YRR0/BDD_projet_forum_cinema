from faker import Faker
import csv
import random
from datetime import datetime, timedelta

fake = Faker()
import random
from datetime import datetime

#valeurs

nombre_emojis=100
nombre_evenements=100

probabilite_artiste_null=0.99

def ecrire_donnees_dans_csv(donnees, nom_fichier, entetes):
    with open(nom_fichier, mode='w', newline='', encoding='utf-8') as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(entetes)
        writer.writerows(donnees)
    print(f"Le fichier {nom_fichier} a été généré avec succès.")

nombre_artistes=1000
def generer_artistes(nombre_artistes):
    artistes = []
    artistes_ids = []  # Liste pour stocker les IDs des artistes générés
    i=0
    for _ in range(nombre_artistes):
        ID_Artiste = i
        nom = fake.name()
        sexe = fake.random_element(elements=("feminine", "masculine"))
        nb_Oscars = fake.random_int(min=0, max=30)
        #artiste_id = fake.random_int(min=1, max=1000000)  # Générer un ID d'artiste aléatoire
        artistes.append([ID_Artiste, nom, sexe, nb_Oscars])
        i+=1

    return artistes

nombre_utilisateurs=4000
def generer_utilisateurs( nombre_utilisateurs):
    utilisateurs = []
    i=0
    for _ in range(nombre_utilisateurs):
        #login = fake.random_int (min=1, max=100 000 000)  # Générer un ID d'artiste aléatoire
        logins=i
        nom_utilisateur = fake.user_name()
        mot_de_passe = fake.password(length=10)
        anniversaire = fake.date_of_birth(minimum_age=12, maximum_age=120)
        
        # Déterminer si ID_Artiste est NULL pour certains utilisateurs
        if random.random() < probabilite_artiste_null:
            ID_Artiste = None
        else:
            ID_Artiste = random.choice (artistes) [0]  # Sélectionner un ID_Artiste existant
        
        utilisateurs.append([logins, nom_utilisateur, mot_de_passe, anniversaire, ID_Artiste])
        i+=1
    return utilisateurs

# Générer des catégories fictives
def generer_categories():
    categories = [
        "-18 ans", "18-25 ans", "26-39 ans", "40-59 ans", "60 ans et +",
        "Le temps du muet : 1895 - 1929",
        "L'Age classique : 1930 - 1945",
        "Les années 50 : 1946 -1958",
        "Les années 60 : 1959-1967",
        "Les années 70 : 1968-1983",
        "Les années 80 : 1984-1991",
        "Les années 90 : 1992-2001",
        "Les années 2000 : 2002-2010"
    ]
    return [[categorie] for categorie in categories]

def generer_sujets():
    sujets = []
    
    # Ajouter des sujets liés au cinéma avec des hashtags
    sujets = [
        "BruceWillis", "StarWars", "Nemo", "CeremonieCesar2020", "Marvel", "DCComics", 
        "Oscar", "Cannes", "FilmNoir", "Blockbuster", "Hitchcock", "Tarantino", 
        "Spielberg", "Disney", "Pixar", "HarryPotter", "LordOfTheRings", 
        "JamesBond", "Superhero", "Animation", "Action", "Adventure", "Comedy", 
        "Drama", "Horror", "ScienceFiction", "Fantasy", "Thriller", "Mystery", 
        "Romance", "Biopic", "Documentary", "Musical", "Western", "War", "Crime", 
        "History", "Sport", "Family", "Teen", "Indie", "ForeignFilm", "ClassicFilm", 
        "SilentFilm", "CinemaScope", "IMAX", "3D", "CGI", "MotionCapture", 
        "SpecialEffects", "GreenScreen", "CostumeDesign", "Makeup", "Cinematography", 
        "FilmEditing", "SoundEditing", "VisualEffects", "Score", "Soundtrack", 
        "Screenplay", "Adaptation", "OriginalStory", "Dialogue", "Director", 
        "Actor", "Actress", "SupportingRole", "Casting", "Stunt", "Cameo", 
        "VoiceOver", "PerformanceCapture", "Producer", "ExecutiveProducer", 
        "ProductionDesign", "ArtDirection", "SetDecoration", "CostumeDesign", 
        "Wardrobe", "MakeupArtist", "HairStyling", "SoundDesign", "SoundMixing", 
        "FoleyArtist", "BoomOperator", "ADR", "FilmScore", "FilmFestival", 
        "RedCarpet", "MovieTheater", "Popcorn", "CinemaTickets", "BoxOffice", 
        "DVD", "BluRay", "Streaming", "Piracy", "FilmCritic", "MovieReview", 
        "AwardSeason", "FilmIndustry", "Screening", "FilmClub", "FilmSchool", 
        "FilmMaking", "MovieMagic", "BehindTheScenes", "OnSet", "Cinematography", 
        "Storyboard", "Rehearsal", "Take", "Cut", "Action", "Scene", "Shot", 
        "Frame", "Sequence", "Montage", "FadeIn", "FadeOut", "CloseUp", 
        "LongShot", "Pan", "Zoom", "Tilt", "Dolly", "Crane", "TrackingShot", 
        "Steadicam", "Handheld", "StaticShot", "EstablishingShot", "Insert", 
        "JumpCut", "CrossCut", "MatchCut", "SplitScreen", "ParallelEditing", 
        "Flashback", "Flashforward", "DreamSequence", "Voiceover", "Narration", 
        "DiegeticSound", "NonDiegeticSound", "AmbientSound", "Score", "Soundtrack", 
        "SoundEffect", "Foley", "Looping", "Dubbing", "Mixing", "Mastering", 
        "SurroundSound", "DolbyAtmos", "THX", "5.1", "7.1", "DTS", "Stereo", 
        "Mono", "Dialogue", "Monologue", "Soliloquy", "Interrogation", 
        "Conversation", "Banter", "Debate", "Argument", "Discussion", 
        "Interview", "PressConference", "PressJunket", "Q&A", "Panel", 
        "Roundtable", "Seminar", "Symposium", "Keynote", "Presentation", 
        "Lecture", "Demonstration", "Workshop", "Masterclass", "Tutorial", 
        "Webinar", "Forum", "Meeting", "Assembly", "Convention", 
        "Gala", "AwardsCeremony", "Festival", "Exhibition", "Premiere", 
        "Screening", "Showcase", "Retrospective", "Tribute", "Homage", 
        "Celebration", "Gathering", "Reception", "Afterparty", "WrapParty", 
        "Launch", "OpeningNight", "ClosingNight", "MidnightScreening", 
        "Preview", "Teaser", "Trailer", "SneakPeek", "Promo", "Spot", 
        "Clip", "Featurette", "TeaserTrailer", "TheatericalTrailer", 
        "InternationalTrailer", "RedBandTrailer", "GreenBandTrailer", 
        "TeaserPoster", "CharacterPoster", "ActionPoster", "InternationalPoster", 
        "TeaserTrailer", "TheatericalTrailer", "InternationalTrailer", 
        "RedBandTrailer", "GreenBandTrailer", "TeaserPoster", "CharacterPoster", 
        "ActionPoster", "InternationalPoster", "Billboard", "BusStopPoster", 
        "SubwayPoster", "MagazineAd", "NewspaperAd", "TVSpot", "RadioSpot", 
        "InternetAd", "SocialMediaCampaign", "ViralMarketing", "GuerrillaMarketing", 
        "CrossPromotion", "ProductPlacement", "Merchandising", "TieIn", 
        "Spinoff", "Franchise", "Sequel", "Prequel", "Reboot", "Remake", 
        "Adaptation", "Novelization", "GraphicNovel", "ComicBook", "Manga", 
        "VideoGame", "BoardGame", "ToyLine", "Collectibles", "ActionFigures", 
        "TradingCards", "Poster", "ArtPrint", "SoundtrackAlbum", "ScoreAlbum", 
        "BehindTheScenesBook", "OfficialGuide", "ArtBook", "MakingOf", 
        "CinematographyBook", "ScreenplayBook", "StoryboardArt", "ConceptArt", 
        "CostumeDesignBook", "ProductionDesignBook", "FilmTheory", 
        "FilmAnalysis", "FilmHistory", "FilmCriticism", "FilmAesthetics", 
        "FilmLanguage", "FilmSemiotics", "FilmNarrative", "FilmStyle", 
        "FilmGenre", "FilmStructure", "FilmForm", "FilmTheory", 
        "FilmAnalysis", "FilmHistory", "FilmCriticism", "FilmAesthetics", 
        "FilmLanguage", "FilmSemiotics", "FilmNarrative", "FilmStyle", 
        "FilmGenre", "FilmStructure", "FilmForm", "FilmTheory", 
        "FilmAnalysis", "FilmHistory", "FilmCriticism", "FilmAesthetics", 
        "FilmLanguage", "FilmSemiotics", "FilmNarrative", "FilmStyle", 
        "FilmGenre", "FilmStructure", "FilmForm"
    ]
    return [[sujet] for sujet in sujets]

nombre_publication=500
proba_sujet2=0.5
proba_sujet3=0.25
def generer_publications(nombre_publications):
    publications = []
    i=0
    for _ in range(nombre_publications):
        ID_Publication=i
        
        texte = fake.text(max_nb_chars=140)
        sujet1 = fake.random_element(sujets)
        if random.random() < proba_sujet2:
            sujet2 = fake.random_element(sujets)
        else:
            sujet2= None
        if random.random() < proba_sujet3:
            sujet3 = fake.random_element(sujets)
        else:
            sujet3= None
            
        date_p = fake.date_time_between(start_date="-20y", end_date="now")
        auteur = fake.random_element(utilisateurs)[0]
        categorie = fake.random_element(categories)
        publications.append([ID_Publication,texte, sujet1, sujet2, sujet3, date_p, auteur, categorie])
        i+=1
    return publications

def generer_emojis():
    emojis = []
    emo = [
        "👍", "❤️", "😄", "😁", "😆",
        "😅", "😂", "🤣", "😊", "😇",
        "🙂", "🙃", "😉", "😌", "😍",
        "🥰", "😘", "😗", "😙", "😚",
        "😋", "😛", "😝", "😜", "🤪",
        "🤨", "🧐", "🤓", "😎", "🤩",
        "🥳", "😏", "😒", "😔", "😟",
        "😕", "🙁", "☹️", "😣", "😖",
        "😫", "😩", "🥺", "😢", "😭",
        "😤", "😠", "😡", "🤬", "🤯",
        "😳", "🥵", "🥶", "😱", "😨",
        "😰", "😥", "😓", "🤗", "🤔",
        "🤭", "🤫", "🤥", "😶", "😐",
        "😑", "😬", "🙄", "😯", "😦",
        "😧", "😮", "😲", "😴", "🤤",
        "😪", "😵", "🤐", "🥴", "🤢",
        "🤮", "🤧", "😷", "🤒", "🤕",
        "🥵", "🥶", "🥺", "👍", "❤️",
        "😀", "😃", "😁", "😆", "😅",
        "😂", "🤣", "😊", "😇", "🙂",
    ]
    i=0
    for _ in range(nombre_emojis):
        emojis.append([i , emo[i]])
        i+=1
    return emojis

nombre_commentaires=200
proba_commentaire=0.7
def generer_commentaires(nombre_commentaires):
    commentaires = []
    i=0
    for _ in range(nombre_commentaires):
        ID_Commentaire=i
        i+=1
        texte = fake.text(max_nb_chars=140)
        auteur = fake.random_element(utilisateurs)[0]
        origine_p = fake.random_element(publications)[0]
        
        if random.random() < proba_commentaire:
             origine_c = fake.random_int(nombre_commentaires)
        else:
            origine_c= None
        commentaires.append([ID_Commentaire,texte, auteur, origine_p, origine_c])
    return commentaires

nombre_reactions=1500
def generer_reactions(nombre_reactions):
    reactions = []
    for _ in range(nombre_reactions):
        utilisateur = fake.random_element(utilisateurs)[0]
        publication = fake.random_element(publications)[0]
        i= fake.random_int(min=0, max=nombre_emojis)
        ID_Emoji = fake.random_element(emojis)[0]
        reactions.append([utilisateur, publication, ID_Emoji])
    return reactions



nombre_hashtags=1000
def generer_hashtags(nombre_hashtags):
    hashtags = []
    for _ in range(nombre_hashtags):
        publication = fake.random_element(publications)[0]
        sujet = fake.random_element(sujets)
        date_h = fake.date_between(start_date="-20y", end_date="now")
        hashtags.append([publication, sujet, date_h])
    return hashtags

nombre_evenements=200
def generer_evenements(nombre_evenements):
    evenements = []
    i=0
    for _ in range(nombre_evenements):
        ID_Evenement=i
        titre = fake.sentence(nb_words=3)
        lieu = fake.city()
        date_e = fake.date_time_between(start_date="now", end_date="+2y")
        prix = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
        nbPlaces = fake.random_int(min=1, max=100000)
        annonce = fake.random_element(publications)[0]
        organisateur = fake.random_element(utilisateurs)[0]
        evenements.append([ID_Evenement,titre, lieu, date_e, prix, nbPlaces, annonce, organisateur])
        i+=1
    return evenements


def generer_evenements_passes(nombre_evenements):
    evenements_passes = []
    evenements_archive = {}
    i=0
    y=0
    for _ in range(nombre_evenements):
        if evenements[i][3]<datetime.now() : # on archive tous les evenments déjà passés
            ID_Archive=y
            y+=1
            programme = fake.text(max_nb_chars=300)
            nb_Participants = fake.random_int(min=0, max=120000)
            lien = fake.uri()
            ID_Evenement = i
            evenements_passes.append([ID_Archive,programme, nb_Participants, lien, ID_Evenement])     
    i+=1
    return evenements_passes 

nombre_interets=200
def generer_interesse(nombre_interets):
    interets = []
    for _ in range(nombre_interets):
        ID_Evenement = fake.random_element(evenements)[0]
        ID_Utilisateur = fake.random_element(utilisateurs)[0]
        participe = fake.random_element(elements=(True, False))
        interets.append([ID_Evenement, ID_Utilisateur, participe])
    return interets

def generer_genres():
    genres = [
        "Action", 
        "Aventure", 
        "Animation", 
        "Biographie", 
        "Comédie", 
        "Crime", 
        "Documentaire", 
        "Drame", 
        "Familial", 
        "Fantaisie", 
        "Histoire", 
        "Horreur", 
        "Musical", 
        "Mystère", 
        "Romance", 
        "Science-fiction", 
        "Thriller", 
        "Guerre", 
        "Western"]
   
    
    return [[genre] for genre in genres]

def generer_sous_genres():
    sous_genres = [
    ["Action", None, None],
    ["Aventure", None, None],
    ["Animation", None, None],
    ["Biographie", None, None],
    ["Comédie", None, None],
    ["Crime", None, None],
    ["Documentaire", None, None],
    ["Drame", None, None],
    ["Familial", None, None],
    ["Fantaisie", None, None],
    ["Histoire", None, None],
    ["Horreur", None, None],
    ["Musical", None, None],
    ["Mystère", None, None],
    ["Romance", None, None],
    ["Science-fiction", None, None],
    ["Thriller", None, None],
    ["Guerre", None, None],
    ["Western", None, None],
    ["Dystopie", "Science-fiction", None],
    ["SpaceOpera", "Science-fiction", None],
    ["HorrorComedie", "Horreur", "Comédie"],
    ]
   
    
    return [[genre] for genre in sous_genres]

nombre_films=1000
def generer_films(nombre_films):
    films = []
    for _ in range(nombre_films):
        titre = fake.sentence(nb_words=3)
        ID_Realisateur = fake.random_element(artistes)[0]
        nb_Oscars = fake.random_int(min=0, max=10)
        nb_Entrees = fake.random_int(min=1000, max=1000000)
        annee = fake.random_int(min=1950, max=2024)
        genre = fake.random_element(elements=genres)
        films.append([titre, ID_Realisateur, nb_Oscars, nb_Entrees, annee, genre])
    return films

nombre_acteurs=3000 #il y en a moins mais on les compte a chaque fois qu ils jouent dans un film
def generer_acteurs(nombre_acteurs):
    acteurs = []
    for _ in range(nombre_acteurs):
        titre = fake.random_element(films)[0]
        realisateur = fake.random_element(films)[1]
        acteur = fake.random_element(artistes)[0]
        acteurs.append([titre, realisateur, acteur])
    return acteurs

nombre_groupes=120
def generer_groupes(nombre_groupes):
    groupes = []
    i=0
    for _ in range(nombre_groupes):
        ID_Groupe=i
        nom = fake.company()
        type_g = fake.random_element(elements=("club", "presse", "studio", "festival", "cinema"))
        createur = fake.random_element(utilisateurs)[0]
        groupes.append([ID_Groupe,nom, type_g, createur])
        i+=1
    return groupes

membres=1000
def generer_membres(nombre_membres):
    membres = []
    for _ in range(nombre_membres):
        groupe = fake.random_element(groupes)[0]
        logins = fake.random_element(utilisateurs)[0]
        membres.append([groupe, logins])
    return membres

# Générer des relations de suivi fictives
def generer_follows(nombre_follows):
    follows = []
    for _ in range(nombre_follows):
        suivi = fake.random_element(utilisateurs)[0]
        suiveur = fake.random_element(utilisateurs)[0]
        follows.append([suivi, suiveur])
    return follows

nombre_historique=50000
def generer_historiques(nombre_historiques):
    historiques = []
    for _ in range(nombre_historiques):
        utilisateur = fake.random_element(utilisateurs)[0]
        sujet = fake.random_element(sujets)[0]
        date_h = fake.date_time_between(start_date="-1y", end_date="now")
        historiques.append([utilisateur, sujet, date_h])
    return historiques

if __name__ == "__main__":
    # Génération des données pour chaque table
    artistes = generer_artistes(nombre_artistes)
    utilisateurs = generer_utilisateurs(nombre_utilisateurs)
    categories = generer_categories()
    sujets = generer_sujets()
    publications = generer_publications(nombre_publication)
    emojis = generer_emojis()
    commentaires = generer_commentaires(nombre_commentaires)
    reactions = generer_reactions(nombre_reactions)
    hashtags = generer_hashtags(nombre_hashtags)
    evenements = generer_evenements(nombre_evenements)
    evenements_passes = generer_evenements_passes(nombre_evenements)
    interets = generer_interesse(nombre_interets)
    genres = generer_genres()
    sous_genres = generer_sous_genres()
    films = generer_films(nombre_films)
    acteurs = generer_acteurs(nombre_acteurs)
    groupes = generer_groupes(nombre_groupes)
    membres = generer_membres(membres)
    follows = generer_follows(50000)
    historiques = generer_historiques(nombre_historique)

# Écriture des données dans des fichiers CSV
ecrire_donnees_dans_csv(artistes, 'artistes.csv', ['ID_Artiste', 'nom', 'sexe', 'nb_Oscars'])
ecrire_donnees_dans_csv(utilisateurs, 'utilisateurs.csv', ['logins', 'pseudo', 'mdp', 'anniversaire', 'ID_Artiste'])
ecrire_donnees_dans_csv(publications, 'publications.csv', ['ID_Publication', 'texte', 'sujet1', 'sujet2', 'sujet3', 'date_p', 'auteur', 'categorie'])
ecrire_donnees_dans_csv(emojis, 'emojis.csv', ['ID_Emoji', 'nom'])
ecrire_donnees_dans_csv(commentaires, 'commentaires.csv', ['ID_Commentaire', 'texte', 'auteur', 'origine_p', 'origine_c'])
ecrire_donnees_dans_csv(reactions, 'reactions.csv', ['ID_Utilisateur', 'ID_Publication', 'ID_Emoji'])
ecrire_donnees_dans_csv(hashtags, 'hashtags.csv', ['ID_Publication', 'nom_Sujet', 'date_h'])
ecrire_donnees_dans_csv(evenements, 'evenements.csv', ['ID_Evenement', 'titre', 'lieu', 'date_e', 'prix', 'nbPlaces', 'annonce', 'organisateur'])
ecrire_donnees_dans_csv(evenements_passes, 'evenements_passes.csv', ['ID_Archive', 'programme', 'nb_Participants', 'lien', 'ID_Evenement'])
ecrire_donnees_dans_csv(interets, 'interets.csv', ['ID_Evenement', 'ID_Utilisateur', 'participe'])
ecrire_donnees_dans_csv(groupes, 'groupes.csv', ['ID_Groupe', 'nom', 'type_g', 'createur'])
ecrire_donnees_dans_csv(membres, 'membres.csv', ['groupe', 'logins'])
ecrire_donnees_dans_csv(follows, 'follows.csv', ['suivi', 'suiveur'])
ecrire_donnees_dans_csv(historiques, 'historiques.csv', ['utilisateur', 'sujet', 'date_h'])
ecrire_donnees_dans_csv(films, 'films.csv', ['titre', 'ID_Realisateur', 'nb_Oscars', 'nb_Entrees', 'annee', 'genre'])
ecrire_donnees_dans_csv(acteurs, 'acteurs.csv', ['titre', 'realisateur', 'acteur'])
ecrire_donnees_dans_csv(genres, 'genres.csv', ['nom'])
ecrire_donnees_dans_csv(sous_genres, 'sous_genres.csv', ['nom', 'parent1', 'parent2'])
ecrire_donnees_dans_csv(sujets, 'sujets.csv', ['nom'])
ecrire_donnees_dans_csv(categories, 'categories.csv', ['nom'])



print("Toutes les données ont été générées et stockées avec succès.")