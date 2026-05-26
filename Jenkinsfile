pipeline {
    agent any

    environment {
    APP_NAME = "flask-devops-app"
    KUBECONFIG = "/Users/shwetabharambe/.kube/config"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh '/usr/local/bin/docker build -t flask-devops-app .'
            }
        }

        stage('Deploy Redis') {
            steps {
                sh '/opt/homebrew/bin/kubectl apply -f redis-deployment.yaml'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '/opt/homebrew/bin/kubectl apply -f deployment.yaml'
                sh '/opt/homebrew/bin/kubectl apply -f service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '/opt/homebrew/bin/kubectl get pods'
                sh '/opt/homebrew/bin/kubectl get svc'
            }
        }
    }
}