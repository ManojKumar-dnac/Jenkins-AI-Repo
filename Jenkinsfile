pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/ManojKumar-dnac/Jenkins-AI-Repo.git'
            }
        }
        stage ('Install Python Dependencies') {
            steps {
                sh 'pip3 install openai'
            }
        }
        stage('Create Sample Log') {
            steps {
                sh '''
                echo "ERROR: Docker build failed" > app.log
                echo "unable to prepare context: Dockerfile not found" >> app.log
                '''
            }
        }

        stage('Run AI Log Analyzer') {
            steps {
                sh 'python3 analyze_logs.py'
            }
        }
    }
}
