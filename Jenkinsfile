pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/JEEVAABI15/FASTAPI-APPLICATION-STOCK'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker build -t fastapi-microservice .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker run -d -p 8000:8000 fastapi-microservice'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
