pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ananya-Nemalapuri/student-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ananya2dsu/student-app .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'PASS')]) {
                    sh '''
                        echo $PASS | docker login -u ananya2dsu --password-stdin
                        docker push ananya2dsu/student-app
                    '''
                }
            }
        }

    }
}
