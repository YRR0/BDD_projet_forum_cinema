# Projet Bases de Données 

Rendu2:

Cette Archive contient les documents suivants:

Dossier Rapport

    1)Rapport.pdf 
		Rendu3: Rapport de 8 pages en format pdf incluant . le modèle entité-associations
									. un schéma relationnel 
									. Une explication des choix et limites
									. Requêtes
									. Calcul indice Recommandation

	2)ExplicationDiagrammeUML.odt
			
			Fichier explicatif complet de la version finale du diagramme UML.
			Contient la liste de toutes les tables, leur explication ainsi que leur passage au schema logique


Dossier Schema
    						
			
		1)Schema_Pre_Heredite.png

			Image du diagramme UML avant élimination des hérédités
			
			
		2)Diagramme_UML_Final.drawio.png

			Rendu1: Image du diagramme UML final après élimination des hérédités.
    
Dossier Création
 
	1)traduction.sql 
		le fichier sql qui traduit le schema relationnel et crée les tables/
	
	2)Dossier script
		.remplissage.sql
			le fichier sql qui permet de remplir les tables
	
	3)Dossier requete
		.req.sql  
			fichier sql contenant les requêtes à tester
		.req_echo.sql  
			avec affichage

	4)Dossier CSV
		.Dossier ressources 
			contient les fichiers csv avec les données
		.Dossier venv 
			contient le script python qui génère les données


Instruction pour tester le projet:

1)On lance psql
pql

2)On crée un schéma et on s'y rend:
create schema cineNet;
CREATE SCHEMA
SET search_path to cineNet;
SET

3)On execute traduction.sql
\i traduction.sql

4)On execute remplissage.sql
\i script/remplissage.sql

5)On peut maintenant tester les requêtes.
\i requete/req_echo.sql



     
    
