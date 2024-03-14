pipeline {
    agent any

    stages {
        stage('Build Backend') {
            steps {
                sh 'docker build -t NoteNest-backend ./backend'
            }
        }
        stage('Build Frontend') {
            steps {
                sh 'docker build -t NoteNest-frontend ./frontend'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f kubernetes/deployments/'
            }
        }
    }
}
