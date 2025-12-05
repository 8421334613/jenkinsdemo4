pipeline{
    agent any
    environment{
        Python='C:\Users\sakha\AppData\Local\Programs\Python\Python311\python.exe'
    }

    stages{
        
        stage{
            name: 'Checkout'
            steps{
                checkout scm
            }
        }
        stage('Extract Data'){
            steps{
                script{
                    bat """${Python} extract_data.py > extracted_data.csv"""
                }
            }
        }
        stage('install dependencies'){
            steps{
                script{
                    bat """${Python} extract_data.py > extract_data.csv"""
                }
            }
        }
    }
}

