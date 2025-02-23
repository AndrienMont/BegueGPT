# Groupe : BegueChat
# Membres : 
- POLICASTRO Luca
- BOITOUZET Emilien
- MONTMAYEUR Andrien

BegueGPT est composé de deux fichiers : le *backend.py*, qui communique avec le model sur HuggingFace, et le *frontend.html*, qui fait l'affichage.
Le projet est dockerisé. Il suffit de clone le repo et d'exécuter la commande :
```
docker build -t <nom_img> .
docker run -p 8000:8000 <nom_img>
```
L'application tournera sur l'adresse *localhost:8000*.
