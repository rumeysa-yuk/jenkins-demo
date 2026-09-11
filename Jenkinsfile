pipeline {
    agent any

    environment {
        IMAGE_NAME     = "jenkins-demo-app"
        IMAGE_TAG      = "build-${BUILD_NUMBER}"
        CONTAINER_NAME = "jenkins-demo-prod"
        HOST_PORT      = "5002"
    }

    stages {

        stage('Checkout Bilgisi') {
            steps {
                echo "Kod Git'ten cekildi. Icerik:"
                sh 'ls -la'
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

        // ARTIK GECICI RUN YOK. Onun yerine Ansible ile KALICI deploy.
        stage('Deploy (Ansible)') {
            steps {
                echo "Ansible ile kalici deploy yapiliyor..."
                dir('ansible') {
                    sh '''
                        ansible-playbook -i inventory.ini deploy.yml \
                          -e "image=${IMAGE_NAME}:${IMAGE_TAG}" \
                          -e "container_name=${CONTAINER_NAME}" \
                          -e "host_port=${HOST_PORT}"
                    '''
                }
            }
        }

        stage('Deploy Sonrasi Dogrulama') {
            steps {
                echo "Deploy edilen uygulama gercekten cevap veriyor mu?"
                sh '''
                    sleep 3
                    docker exec ${CONTAINER_NAME} python -c "import urllib.request; assert 'Merhaba Jenkins' in urllib.request.urlopen('http://localhost:5000/').read().decode(); print('Deploy dogrulandi, uygulama ayakta!')"
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline basarili. Uygulama http://localhost:${HOST_PORT} adresinde CANLI ve kalici."
        }
        failure {
            echo "Bir yerde patladi, Console Output'a bak."
        }
    }
}