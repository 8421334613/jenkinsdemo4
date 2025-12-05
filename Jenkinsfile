pipeline {
    agent any

    environment {
        Python = 'C:\\Users\\sakha\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Extract Data') {
            steps {
                script {
                    bat "${Python} extract_data.py > extracted_data.csv"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Assuming you have a requirements.txt file
                    bat "${Python} -m pip install -r requirements.txt"
                }
            }
        }
    }
}
