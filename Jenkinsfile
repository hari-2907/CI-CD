pipeline {
    agent any

    environment {
        APP_URL = "http://your-ec2-public-dns:8080"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull latest code from GitHub
                git branch: 'main', url: 'https://github.com/your-username/my-python-jenkins-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies from requirements.txt
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Health Check') {
            steps {
                // Run the Python script
                sh "python3 health_check.py"
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image for the app
                sh 'docker build -t python-jenkins-demo .'
            }
        }

        stage('Run Docker Container') {
            steps {
                // Run the container and check output
                sh 'docker run --rm python-jenkins-demo'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}
