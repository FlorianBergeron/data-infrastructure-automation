# Automation Infrastructure de Données
Projet scolaire

* Le but de ce projet est de fournir aux artistes un moyen de suivre la popularité de leurs titres sur les différentes plateformes de streaming comme Deezer ou spotify.

* Nous voulons que notre projet permette de suivre les gros artistes comme :

* * Petit Biscuit, Nekfeu, JUL

* Mais aussi de repérer les artistes qui arrivent en tendance.

## Architecture
![Alt text](/architecture.png?raw=true "Architecture")

## main.py

Pour lancer le projet, il suffit d'éxecuter la commande suivante :
```python3 main.py ```

**api.py**

Récupère les données de Deezer, filtre les données et créer des datasets au format ```.parquet```.

**hdfs.py**

Créé un dossier ```top_hit_parquet``` sur HDFS et envoie le fichier ```top_hit.parquet``` dessus.

## Automatisation
Début rudimentaire d'automatisation de la solution :

**Cron**

```0 0 * * * /usr/bin/python3 ~/data-infrastructure-automation/api_extract/main.py```


## Pré-Requis
**Librairies**
* python 3.7
* pandas
* requests
* tqdm
