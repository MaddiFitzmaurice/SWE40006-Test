pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MaddiFitzmaurice/SWE40006-Test.git']]])
            }
        }
        stage('Build') {
            steps {
                script {
                    env.CI = 'true'
                }
                //sh 'python3 web_calculator.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }
        stage('Docker Build + Push')
        {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'maddifswin-dockerhub') {
                        sh 'docker build -t maddifswin/group-task:latest .'
                        sh 'docker push maddifswin/group-task:latest'
                    }
                }
               
            }
        }
    }
}