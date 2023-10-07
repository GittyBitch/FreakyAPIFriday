# What

- Python 3.0 Script
- fastapi Beispiele (Route / Funktion)
- uvicorn als Webserver
- unittest für ein Dutzend Tests
- aws CloudFormation zwecks IaC
- aws CodeBuild zwecks Docker Image Erzeugung

# Intro

- auf aws einloggen (management console)
- mittels aws CLI unter WSL einloggen 
- dann die deploy.sh mittels bash ausführen (alternativ unter Windows den Befehl aus dem Shell Script ausführen)


# Behind the Scenes

Was passieren sollte, ist:

- neues ECR repo erstellen namens "freaky-api-friday"
- neues code build Projekt
- Dockerfile wird auf aws  mittels codebuild in ein docker image umgebaut
- das image landet im aws docker repo (ECR)
- (to be continued)


