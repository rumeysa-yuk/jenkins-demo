pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-demo-app"
        IMAGE_TAG  = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('RUMO YENİ STAGE FEATURE ') {
            steps {
                echo "bu bir test stagesidir"
            }
        }

        stage('Merhaba') {
            steps {
                echo "Bu stage Git'ten geldi, Jenkins arayuzune hic dokunmadim!"
            }
        }
        stage('Build Image') {
            steps {
                echo "Docker image build ediliyor..."
                dir('app') {
                    sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
                }
            }
        }

        stage('Test') {
            steps {
                echo "Testler image icinde calisiyor..."
                sh 'docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} pytest -v'
            }
        }

        stage('Deploy (Dogrulama)') {
            steps {
                echo "Container dogrulaniyor..."
                sh '''
                    docker rm -f jenkins-demo-running || true
                    docker run -d --name jenkins-demo-running -p 5001:5000 ${IMAGE_NAME}:${IMAGE_TAG}
                    sleep 3
                    docker exec jenkins-demo-running python -c "import urllib.request; assert 'Merhaba Jenkins' in urllib.request.urlopen('http://localhost:5000/').read().decode(); print('Uygulama cevap verdi!')"
                '''
            }
        }
    }

    post {
        always {
            echo "Temizlik..."
            sh 'docker rm -f jenkins-demo-running || true'
        }
        success { echo "Her sey yolunda!" }
        failure { echo "Patladi, Console Output a bak." }
    }
}