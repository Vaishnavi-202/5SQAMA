pipeline {
    agent { label 'windows && wja' }

    options {
        timestamps()
        ansiColor('xterm')
    }

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Windows Agent') {
            steps {
                bat '''
                echo OS INFO:
                ver
                python --version
                where python
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m pip install --upgrade pip
                pip install pytest allure-pytest pillow pywinauto
                '''
            }
        }

        stage('Run WJA Tests') {
            steps {
                dir('qama_regression_ascendion') {
                    bat '''
                    pytest -v tests/windows/wja --alluredir=allure-results
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'qama_regression_ascendion/allure-results/**', allowEmptyArchive: true
        }
        failure {
            echo '❌ WJA tests failed'
        }
        success {
            echo '✅ WJA tests completed successfully'
        }
    }
}
