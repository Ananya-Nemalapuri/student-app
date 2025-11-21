pipeline {
  agent any

  environment {
    IMAGE_NAME = "student-app"
    IMAGE_TAG  = "${env.BUILD_ID}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
      }
    }
    stage('Unit Tests') {
      steps {
        sh '. .venv/bin/activate || true || echo "venv not used in Jenkins"; pytest -q'
      }
    }
    // Later: stage('Push to Registry'), stage('Deploy'), etc.
  }

  post {
    always {
      echo "Build finished"
    }
  }
}
