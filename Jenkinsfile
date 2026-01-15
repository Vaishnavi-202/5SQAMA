pipeline {
    agent {
        label 'windows-wja'
    }

    options {
        timestamps()
        ansiColor('xterm')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                python --version
                python -m pip install --upgrade pip
                pip install pytest allure-pytest pywinauto pillow
                '''
            }
        }

        stage('Run WJA Tests') {
            steps {
                bat '''
                cd qama_regression_ascendion
                pytest -v -m wja --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'qama_regression_ascendion/allure-results/**', allowEmptyArchive: true
        }
        failure {
            echo 'WJA test failure detected'
        }
    }
}
