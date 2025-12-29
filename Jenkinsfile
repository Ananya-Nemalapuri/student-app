pipeline {
    agent any

    environment {
        IMAGE_NAME = "ananya2dsu/student-app"
        IMAGE_TAG  = "${env.BUILD_ID}"
    }

    stages {

       stage('Clone') {
    steps {
        git branch: 'main',
            url: 'https://github.com/Ananya-Nemalapuri/student-app.git'
    }
}

        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'pytest -q || true'
            }
        }
    }
}

