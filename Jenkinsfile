
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t student-management-app:${BUILD_NUMBER} .
                    docker tag student-management-app:${BUILD_NUMBER} student-management-app:latest
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    docker rm -f student-management-test || true

                    docker run -d \
                      --name student-management-test \
                      -p 5001:5000 \
                      student-management-app:latest

                    for i in $(seq 1 15); do
                        if curl -fsS http://localhost:5001/health; then
                            echo "Application test successful"
                            exit 0
                        fi
                        sleep 2
                    done

                    docker logs student-management-test
                    exit 1
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker rm -f student-management-test || true
                    docker rm -f student-management || true

                    docker run -d \
                      --restart unless-stopped \
                      --name student-management \
                      -p 5000:5000 \
                      student-management-app:${BUILD_NUMBER}
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    for i in $(seq 1 15); do
                        if curl -fsS http://localhost:5000/health; then
                            echo "Deployment successful!"
                            exit 0
                        fi
                        sleep 2
                    done

                    docker logs student-management
                    exit 1
                '''
            }
        }
    }
}

