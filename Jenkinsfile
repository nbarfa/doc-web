pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t nitin260/doc-web:latest .'
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }
        stage('Push Image') {
            steps {
                sh 'docker push nitin260/doc-web:latest'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                cd $WORKSPACE

                docker-compose pull

                docker-compose up -d
                '''
            }
        }
    }
}