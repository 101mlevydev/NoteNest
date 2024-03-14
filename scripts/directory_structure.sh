#!/bin/bash

# Create the root directory for the NoteNest application
mkdir -p NoteNest/{backend,frontend,kubernetes}

# Create backend directory and files
mkdir -p NoteNest/backend
touch NoteNest/backend/app.py
touch NoteNest/backend/requirements.txt
touch NoteNest/backend/Dockerfile

# Create frontend directory and files
mkdir -p NoteNest/frontend/{public,src/components}
touch NoteNest/frontend/package.json
touch NoteNest/frontend/Dockerfile
touch NoteNest/frontend/src/components/{NoteList.js,NoteItem.js}
touch NoteNest/frontend/src/{app.js, index.js}

# Create Kubernetes directory and subdirectories
mkdir -p NoteNest/kubernetes/{deployments,services,ingress}

# Create Kubernetes deployment files
touch NoteNest/kubernetes/deployments/backend-deployment.yaml
touch NoteNest/kubernetes/deployments/frontend-deployment.yaml
touch NoteNest/kubernetes/deployments/mongodb-deployment.yaml

# Create Kubernetes service files
touch NoteNest/kubernetes/services/backend-service.yaml
touch NoteNest/kubernetes/services/frontend-service.yaml

# Create Kubernetes Ingress file
touch NoteNest/kubernetes/ingress/ingress.yaml

# Create Jenkinsfile
touch NoteNest/Jenkinsfile

# Create README.md
touch NoteNest/README.md

# Create .gitignore
touch NoteNest/.gitignore

echo "NoteNest directory structure and files created successfully!"
