pipeline {
    agent any
    options {
            buildDiscarder(logRotator(numToKeepStr: '20', artifactDaysToKeepStr: '5'))
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('30 * * * *')])])
                }
                git 'https://github.com/aakram786/GDE-Project-AA.git'
            }
        }
        stage('run rest app') {
            steps {

                sh 'nohup /Users/anwarakram/PycharmProjects/GDE-Project/venv/bin/python rest_app.py &'

            }
        }
        stage('run web app') {
            steps {

                sh 'nohup /Users/anwarakram/PycharmProjects/GDE-Project/venv/bin/python web_app.py &'

            }
        }
        stage('run backend testing') {
            steps {

                sh '/Users/anwarakram/PycharmProjects/GDE-Project/venv/bin/python backend_testing_j.py'

            }
        }
        stage('run frontend testing') {
            steps {

                sh '/Users/anwarakram/PycharmProjects/GDE-Project/venv/bin/python frontend_testing_j.py'

            }
        }
        stage('run combined testing') {
            steps {

                sh '/Users/anwarakram/PycharmProjects/GDE-Project/venv/bin/python combined_testing.py'

            }
        }
        stage('run clean environment') {
            steps {

                sh '/Users/anwarakram/PycharmProjects/GDE-Project/venv/bin/python clean_environment.py'

            }
        }
    }
}