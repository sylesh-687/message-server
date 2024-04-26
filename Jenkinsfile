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
        dir("apiserver/"){
          script {
            docker.withRegistry('https://index.docker.io/v1/','037e759f-0510-4e93-ae9a-7201b932675a'){
              def app=docker.build("sylesh687/message-server:${env.BUILD_TAG}")
              app.push()
            }
          }
        }
      }

    }
   stage('Deploy Docker Image'){
     steps{
       script{
         withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]){
         sh '''
           export KUBECONFIG=$KUBECONFIG
           kubectl apply -f apiserver/kubernetes-manifests/message_server.yml
           "kubectl set image deployment/message-server message-server=sylesh687/message-server:\${env.BUILD_TAG}"
         '''

         }
       }
     }
   }

  }
}
