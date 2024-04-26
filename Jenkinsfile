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
        def messageServer = docker.build("message-server:${env.BUILD_TAG}", "--file apiserver/Dockerfile .")
      }

    }

  }
}
