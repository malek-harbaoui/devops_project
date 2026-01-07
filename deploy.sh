#!/bin/bash

ENV=$1
echo "Déploiement vers l'environnement $ENV..."

# Exemple de commande de déploiement (à adapter)
# scp -r ./app.py user@server:/path/to/$ENV/
# ssh user@server "systemctl restart myapp-$ENV"

echo "Déploiement terminé."
