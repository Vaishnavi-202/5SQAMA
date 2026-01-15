pipeline {
    agent { label 'wja' }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        PYTHONUTF8 = '1'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Setup') {
            steps {
                bat '''
                python --version
                python -m pip install --upgrade pip
                pip install pytest allure-pytest pillow pywinauto
                '''
            }
        }

        stage('Run WJA Tests') {
            steps {
                bat '''
                cd qama_regression_ascendion
                pytest -v -m %TEST_SUITE% --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'qama_regression_ascendion/allure-results/**', fingerprint: true
        }
        failure {
            echo '❌ WJA tests failed'
        }
        success {
            echo '✅ WJA tests passed'
        }
    }
}
