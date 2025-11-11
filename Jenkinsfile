pipeline {
    agent any

    environment {
        PYTHON = 'python'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/alanbadillochz-web/seleniumdemoqa.git', branch: 'main'
            }
        }

        stage('Install dependencies') {
            steps {
                sh "${PYTHON} -m pip install -r requirements.txt"
            }
        }

        stage('Run script') {
            steps {
                sh "${PYTHON} formulariodemoqa.py"
            }
        }
    }

    post {
        success {
            echo 'OK Script ejecutado correctamente'
        }
        failure {
            echo 'Error Falló la ejecución del script'
        }
    }
}
Luego en terminal:
bash
