pipeline {
  agent any

  stages {
    stage('Checkout SCM'){
      steps{
        checkout scm
      }
    }
    stage('Build Docker Image'){
      steps {
        sh 'echo "Hello Message-Server" '
        dir("apiserver/"){
          sh 'pwd'
          script {
            docker.build("sylesh687/message-server:${env.BUILD_TAG}")
          }
        }
      }

    }

  }
}
