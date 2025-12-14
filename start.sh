#!/bin/bash

# Vérifier si PostgreSQL tourne
if ! sudo systemctl is-active --quiet postgresql@16-main; then
    echo "Démarrage de PostgreSQL..."
    sudo systemctl start postgresql@16-main
fi

# Démarrer l'application
echo "Démarrage de l'application..."
uvicorn app.main:app --reload

# rendre executable : chmod +x start.sh

# démarrer avec : ./start.sh