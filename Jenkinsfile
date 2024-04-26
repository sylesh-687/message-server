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
            docker.withRegistry('037e759f-0510-4e93-ae9a-7201b932675a'){
              docker.build("sylesh687/message-server:${env.BUILD_TAG}").push()
            }
          }
        }
      }

    }

  }
}
