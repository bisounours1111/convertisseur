# Convertisseur d'images AVIF

## Aperçu :

Ce script Python est conçu pour convertir des images de différents formats en AVIF (Format de fichier d'image AV1). L'AVIF offre une efficacité de compression supérieure par rapport aux formats traditionnels tels que le JPEG ou le PNG, ce qui se traduit par des tailles de fichier plus petites sans compromettre la qualité de l'image.

## Vous devez avoir :

Bibliothèque Pillow
Bibliothèque pillow_avif

## Pour les installer :

```bash
pip install Pillow pillow_avif
```
ou
```bash
py -m pip install Pillow pillow_avif
```

## Utilisation :

Pour démarrer le script vous devez spécifier au minimum le dossier d'entrée et si besoin celui de sortie par défaut (output)

```bash
py -m venv venv

.venv/Scripts/activate

py main.py chemin/vers/dossier/input [chemin/vers/dossier/output]
```
Une fois la conversion terminée, les images converties seront disponibles dans le dossier de sortie spécifié (ou le dossier par défaut "output" si aucun n'est spécifié).