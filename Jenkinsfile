pipeline {
    agent any

    environment {
        MY_NAME = "Vidya"
    }

    stages {
        stage('Build') {
            steps {
                echo "Building the project for ${MY_NAME}"
            }
        }
        stage('Test') {
            steps {
                echo "Running tests"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying to test server"
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully 🎉"
        }
        failure {
            echo "Pipeline failed ❌"
        }
    }
}
