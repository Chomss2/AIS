#Activer les module de points de restorations sur le disque C:\
Enable-ComputerRestore "C:"
#Lancer un point de restoration immediatement
Checkpoint-Computer -Description "Pont de restauration initial"
#Ajouter une tache mensuelle de 