pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning source code...'
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                echo 'Building Backend Docker image...'
                sh '''
                    cd Devops_1/app/backend
                    docker build -t backendjenkins:1.${BUILD_NUMBER} .
                '''
            }
        }

        stage('Build Frontend Image') {
            steps {
                echo 'Building Frontend Docker image...'
                sh '''
                    cd Devops_1/app/frontend
                    docker build -t frontendjenkins:1.${BUILD_NUMBER} .
                '''
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo 'Deploying containers...'
                sh '''
                    cd Devops_1
                    docker-compose down || true
                    docker-compose up -d
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline SUCCESS ✅ Containers are running.'
        }
        failure {
            echo 'Pipeline FAILED ❌ Check logs.'
        }
    }
}


