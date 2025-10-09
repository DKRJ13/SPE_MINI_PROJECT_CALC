pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build & Test') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pytest -q'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t scientific-calculator:latest .'
            }
        }
    }
}
