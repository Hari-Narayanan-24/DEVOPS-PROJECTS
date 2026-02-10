// pipeline {
//     agent any

//     stages {

//         stage('Checkout') {
//             steps {
//                 echo 'Cloning source code...'
//                 checkout scm
//             }
//         }

//         stage('Build Backend Image') {
//             steps {
//                 echo 'Building Backend Docker image...'
//                 sh '''
//                     cd Devops_1/app/backend
//                     docker build -t backendjenkins:1.0.${BUILD_NUMBER} .
//                     docker tag backendjenkins:1.0.${BUILD_NUMBER} backendjenkins:latest
//                 '''
//             }
//         }

//         stage('Build Frontend Image') {
//             steps {
//                 echo 'Building Frontend Docker image...'
//                 sh '''
//                     cd Devops_1/app/frontend
//                     docker build -t frontendjenkins:1.0.${BUILD_NUMBER} .
//                     docker tag frontendjenkins:1.0.${BUILD_NUMBER} frontendjenkins:latest
//                 '''
//             }
//         }

//         stage('Security Scan (Trivy)') {
//             steps {
//                 echo 'Security Scan TRIVY'
//                 sh '''
//                 mkdir -p trivy-reports
                
//                 trivy image -f table -o trivy-reports/backend-report.txt backendjenkins:latest
//                 trivy image -f table -o trivy-reports/frontend-report.txt frontendjenkins:latest
//                 '''
//                 }
//             }
//         stage('Archive Reports') {
//             steps {
//                 archiveArtifacts artifacts: 'trivy-reports/*.txt', fingerprint: true
//             }
//         }

//         stage('Deploy with Docker Compose') {
//             steps {
//                 echo 'Deploying containers...'
//                 sh '''
//                     cd Devops_1
//                     docker-compose down || true
//                     docker-compose up -d
//                 '''
//             }
//         }
//     }

//     post {
//         success {
//             echo 'Pipeline SUCCESS ✅ Containers are running.'
//         }
//         failure {
//             echo 'Pipeline FAILED ❌ Check logs.'
//         }
//     }
// }

pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Scan') {
            steps {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                    sh '''
                      sonar-scanner \
                        -Dsonar.projectKey=devops-project \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://sonarqube:9000 \
                        -Dsonar.login=$SONAR-TOKEN
                    '''
                }
            }
        }

        stage('Build Backend Image') {
            steps {
                sh '''
                  cd Devops_1/app/backend
                  docker build -t backendjenkins:1.0.${BUILD_NUMBER} .
                  docker tag backendjenkins:1.0.${BUILD_NUMBER} backendjenkins:latest
                '''
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh '''
                  cd Devops_1/app/frontend
                  docker build -t frontendjenkins:1.0.${BUILD_NUMBER} .
                  docker tag frontendjenkins:1.0.${BUILD_NUMBER} frontendjenkins:latest
                '''
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh '''
                  mkdir -p trivy-reports

                  docker exec trivy_scanner trivy image \
                    -f table backendjenkins:latest \
                    > trivy-reports/backend.txt

                  docker exec trivy_scanner trivy image \
                    -f table frontendjenkins:latest \
                    > trivy-reports/frontend.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                  docker-compose -f docker-compose-app.yml down || true
                  docker-compose -f docker-compose-app.yml up -d
                '''
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'trivy-reports/*.txt', fingerprint: true
            }
        }
    }
}
