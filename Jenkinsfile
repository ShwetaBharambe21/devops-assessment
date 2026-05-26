pipeline {
    agent any

    environment {
        APP_NAME = "flask-devops-app"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh '/usr/local/bin/docker build -t flask-devops-app .'
            }
        }

        stage('Deploy Redis') {
            steps {
                sh 'kubectl apply -f redis-deployment.yaml'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl get pods'
                sh 'kubectl get svc'
            }
        }
    }
}