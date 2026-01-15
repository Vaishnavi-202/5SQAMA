pipeline {
    agent any

    stages {
        stage('Proof') {
            steps {
                echo 'PIPELINE IS EXECUTING'
            }
        }
    }

    post {
        always {
            echo 'PIPELINE FINISHED'
        }
    }
}
