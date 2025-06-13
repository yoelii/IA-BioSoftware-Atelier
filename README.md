<table style="width: 600px; border: none;" cellpadding="10" align="center">
  <tr>
    <td align="center">
      <img src="images/iPOP-up_logo.png" alt="iPOP-up" style="height: 60px; width: auto;">
    </td>
    <td align="center">
      <img src="images/U-Paris-Cite-logo.png" alt="Université Paris-Cité" style="height: 60px; width: auto;">
    </td>
    <td align="center">
      <img src="images/IFB-logo.png" alt="IFB" style="height: 65px; width: auto;">
    </td>
    <td align="center">
      <img src="images/ELIXIR-France_logo.png" alt="ELIXIR-FR" style="height: 60px; width: auto;">
    </td>
    <td align="center">
      <img src="images/MERIT-logo.png" alt="MERIT" style="height: 50px; width: auto;">
    </td>
  </tr>
</table>

# Utilisation des IA génératives comme appui à la programmation et au scripting pour la biologie

## Information pratique et programme

- <https://moodle.france-bioinformatique.fr/course/view.php?id=41>
- https://ifb-elixirfr.github.io/AI-for-scripting-bioanalysis/

## Organisation

Le colloque est organisé et financé par les trois organisations suivantes :

- [Institut Français de Bioinformatique (IFB)](https://www.france-bioinformatique.fr/)
- Université Paris Cité ([plateforme iPOP-UP](https://ipop.u-paris.fr/) et [DU omiques](https://ipop.u-paris.fr/duomiques/))
- [Réseau métier en bioinformatique (MERIT)](https://merit.cnrs.fr/)

L'Institut Français de Bioinformatique (IFB) a été fondé par les Programme d'Investissements d'Avenir subventionné par l'Agence Nationale de la Recherche ([RENABI-IFB, ANR-11-INBS-0013](https://anr.fr/ProjetIA-11-INBS-0013)) et par le programme France 2030 relatifs aux équipements structurants pour la recherche / EQUIPEX+ ([MUDIS4LS, ANR-21-ESRE-0048](https://anr.fr/ProjetIA-21-ESRE-0048)).

### Encadrants

- [Imane Messak](https://orcid.org/0000-0002-1654-6652) (Institut Français de Bioinformatique)
- [Thomas Denecker](https://orcid.org/0000-0003-1421-7641) (Institut Français de Bioinformatique)
- [Baptiste Rousseau](https://orcid.org/0009-0002-1723-2732) (Institut Français de Bioinformatique)

## Atelier : Développement logiciel

Dans cet atelier, nous explorerons comment l’intelligence artificielle peut devenir un véritable assistant au service du développement logiciel. À l’aide d’outils comme [Pleiade](https://pleiade.mi.parisdescartes.fr/), [chatGPT](https://chat.openai.com/), [Perplexity](https://www.perplexity.ai/) ou d’autres assistants basés sur l’IA, les participant·es apprendront à:

- Corriger automatiquement des erreurs dans leur code (syntaxe, logique, style)

- Optimiser des portions de code pour plus d'efficacité ou de lisibilités

- Suggérer des améliorations respectant les bonnes pratiques de programmation

- Passer avec succès les vérifications automatiques d'intégration continue (CI)

- Générer ou compléter automatiquement des fonctions, des tests unitaires ou de la documentation

Cet atelier a pour but de montrer comment l’IA peut accompagner les bioinformaticiens dans leurs projets de scripting et d’analyse, en réduisant le temps passé à déboguer et en augmentant la qualité du code produit.

### Instruction pour l'atelier

1. Fork le project
2. Clone le projet
3. Ouvre le projet et commence a debuger avec ton outils IA préférer

À la fin de la session dans le `README`:

- Ajouter l’outil utilisé (pléiade, chatGPT, copitot,...)
- Ajouter le modèle utilisé
- Ajouter le nombre de requêtes réalisée

## Contributor Code of conduct

Veuillez noter que ce projet est publié avec [Contributor Code of Conduct](https://www.contributor-covenant.org/). En participant, vous acceptez d’en respecter les termes. Voir le fichier [CODE_OF_CONDUCT](code_of_conduct.md).

## Licence

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

---

## Retour atelier

### Premier test sur pleiade avec codellama.

J'ai demandé une explication de l'ensemble du code python contenu dans le fichier "burger.py".

--> j'ai obtenu la réponse en anglais qui m'a informé que le code était un code écrit en java.
Il m'a aussi répondu plus de 80 fois la même explication sans lien avec le code.

après deux autres requetes avec des réponses sans lien avec la question posée, j'ai changé de modèle

### second test sur librechat.pasteur.fr avec le modèle mistral.

première requete dans mistral : explique moi le code
--> ajoute de l'ensemble des commentaires dans le fichier burger.py

Seconde requete : donne moi le code efficace et sans redondance avec les commentaires.
remplacement de l'ensemble du code par celui généré par mistral

Modifications apportées :
Suppression des boucles inutiles et des importations non utilisées : Les boucles redondantes et les fonctionnalités inutilement compliquées ont été supprimées.
Simplification des fonctions : Les fonctions ont été simplifiées pour limiter les doublons et améliorer la lisibilité.
Gestion des erreurs : Ajout de messages d'erreur pour améliorer le suivi des exceptions.

requete explique githb action

####

requête pour modifier le code et corriger les erreurs Ruff

Les erreurs Ruff fournissent des informations précises sur les améliorations et corrections nécessaires au script. Voici le code corrigé en prenant en compte ces erreurs :

Imports inutilisés : Supprimer les import os et import time non utilisés.
Docstrings : Corriger les docstrings pour correspondre aux normes.
Assignments inutiles : Corriger les variables assignées inutilement avant un return.
Usage de print : Corriger ou écraser les messages print indisponibles.
Sécurité des fichiers temporaires : Utiliser un chemin sûr pour éviter les avertissements.
Absence de nouvelle ligne en fin de fichier : Ajouter une nouvelle ligne à la fin du fichier.

Remplacement du code par celui généré par l'IA

Changelog :
Suppression des imports os et time non utilisés.
Correction des docstrings pour qu'elles soient succinctes et conformes.
Élimination des assignations multiples inutiles.
Utilisation de systèmes d'erreurs en lieu et place de print à des fins de diagnostic.
Organisation des écritures de fichiers dans des fichiers sécurisés évitant les avertissements sur tmp.
Ajout d'une nouvelle ligne en fin de fichier.

Voici les corrections apportées au script pour résoudre les erreurs signalées par Ruff :

Ajouter une ligne vide entre les lignes de résumé et de description dans les docstrings.
Condenser les docstrings sur une seule ligne si possible.
Éviter les variables local assignées mais jamais utilisées.
Corriger les affectations inutiles avant un return.
Corriger les chemins d'accès des fichiers temporaires.
Ajouter une nouvelle ligne en fin de fichier.
Voici le code corrigé avec les erreurs commentées et rectifiées :

Nouvelle correction :
Changements apportés :
Corrections des docstrings : Ajout de ligne vide où cela était nécessaire.
Concaténiation des docstrings sur une seule ligne lorsque c'était approprié.
Élimination des affectations inutiles avant les return statements.
Supression de la variable e non utilisée dans la gestion d'erreur.
Correction des chemins de fichier temporaires (si nécessaire) : À long terme, il est recommandé de changer l'emplacement des fichiers, mais comme mentionnés précédemment, cela dépendrait de la situation d'utilisation dans un environnement sécurisé.
Ajout d'une nouvelle ligne en fin de fichier,
Ces modifications doivent rendre votre code conforme aux standards de Ruff.

Correction des Erreurs Ruff :
D401 : Changée la première ligne de la docstring pour la passer à l'impératif.
W293 : Blanc-kine pas vide, passage de la ligne vide sans espace.
S108 : Les fichiers écrits dans le chemin temporaire sont quelque peu sécurisés comme mentionnés.
W291 : Espacement en fin de ligne supprimé.
W292 : Ajout d'une nouvelle ligne en fin de fichier pour respectant les principales conventions de formatage.
Ces modifications devraient résoudre toutes les erreurs signalées par Ruff.

correction des erreurs safety sans IA.

en modifiant les numéros de version -> debugg classique.
