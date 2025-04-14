import os
import subprocess

# Spécifiez le chemin du dossier contenant les fichiers MP4
dossier = "./"

# Parcourir tous les fichiers du dossier
for filename in os.listdir(dossier):
    # Vérifiez si le fichier est un MP4
    if filename.endswith(".mp4"):
        # Créer le chemin complet du fichier
        chemin_fichier = os.path.join(dossier, filename)
        
        # Créer le nom du fichier de sortie
        nouveau_nom = os.path.join(dossier, "sans_audio_" + filename)
        
        # Exécuter FFmpeg pour supprimer la piste audio
        commande = [
            'ffmpeg', 
            '-i', chemin_fichier,  # fichier d'entrée
            '-an',  # 'an' signifie "audio none", supprimer l'audio
            '-vcodec', 'copy',  # Copier le codec vidéo sans modification
            nouveau_nom  # fichier de sortie
        ]
        
        # Lancer la commande
        subprocess.run(commande, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        print(f"Traitement terminé pour {filename}, sauvegardé sous {nouveau_nom}")
