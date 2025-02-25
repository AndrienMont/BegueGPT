# Groupe : BegueChat

# Membres : 

- POLICASTRO Luca
- BOITOUZET Emilien
- MONTMAYEUR Andrien

# Entrainement

Le but de notre projet est de créer un chatbot qui bégaie. Pour cela nous l'avons entrainé sur un jeu de donnée de conversations sur lequel nous avons appliqué une simple fonction qui transforme le texte en texte bégayé.
Le [dataset](https://huggingface.co/datasets/Khmarigou/alpace_begue_fr) a été généré depuis le [dataset initial](https://huggingface.co/datasets/yahma/alpaca-cleaned) en applicant ce [notebook kaggle](https://www.kaggle.com/code/khmarigou/transforme-dataset-into-begue)

Une fois le dataset prêt, nous avons entrainé le modèle disponible sur **Hugging Face** [SmolLM2-135M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct), avec ce [notebook kaggle](https://www.kaggle.com/code/khmarigou/trainingbeguemodel). 
Après plusieurs entrainement nous avons un modèle qui arrive correctement à bagayer mais divague et se répète en boucle, après plusieurs ajustement en changeant la taille de l'entrainement ou le learning rate nous avons toujours le même résultat. Même en faisant un entrainement sur un tout petit jeu de donnée, le modèle ne bagaye pas mais divague quand même, nous n'avons pas réussit à le stabiliser. Le modèle fonctionne quand même et est disponible sur hugging face [BegueGPT](https://huggingface.co/Khmarigou/Begue).

L'entrainement final a été fait avec les paramètres suivants :
- per_device_train_batch_size=2,
- gradient_accumulation_steps=4,
- warmup_steps=100,
- num_train_epochs=1,
- learning_rate=0.00002,
- lr_scheduler_type="cosine",
- eval_strategy="steps",
- eval_steps=500,
- weight_decay=0.01,
- bf16=True,
- logging_strategy="steps",
- logging_steps=10,
- optim="paged_adamw_8bit",
- seed=42,
- save_steps=31,
- save_total_limit=4

# Fonctionnement

BegueGPT est composé de deux fichiers : le *backend.py*, qui communique avec le model sur HuggingFace, et le *frontend.html*, qui fait l'affichage.
Le projet est dockerisé. Il suffit de clone le repo et d'exécuter la commande :
```
docker build -t <nom_img> .
docker run -p 8000:8000 <nom_img>
```
L'application tournera sur l'adresse *localhost:8000*.
