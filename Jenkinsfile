pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                    python3 -m pytest -q
                '''
            }
        }

        stage('Docker Build') {
            steps {
                    sh 'docker build -t scientific-calculator:latest .'
            }
        }
            

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh '''
                        docker rmi -f ${DOCKERHUB_USER}/scientific-calculator:latest || true
                        docker tag scientific-calculator:latest ${DOCKERHUB_USER}/scientific-calculator:latest

                        echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin
                        docker push ${DOCKERHUB_USER}/scientific-calculator:latest
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                // Use Docker Hub credentials for pulling the image if it's private
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh '''
                        # Ensure Ansible and dependencies are ready
                        ansible-galaxy collection install community.docker
                        python3 -m pip install --user docker

                        # Run the Ansible playbook locally
                        ansible-playbook ansible/playbook.yml -i ansible/inventory/hosts.ini -c local \
                        --extra-vars "image_name=${DOCKERHUB_USER}/scientific-calculator:latest \
                        registry_username=${DOCKERHUB_USER} registry_password=${DOCKERHUB_PASS}"
                    '''
                }
            }
        }



    }

    post {
        success {
            emailext(
                to: 'dakshrajesh04@gmail.com',
                // to: 'dakshrajesh04@gmail.com',
                replyTo: 'dakshrajesh04@gmail.com',
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """<p>Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}</p>
                        <p>Console: <a href='${env.BUILD_URL}'>${env.BUILD_URL}</a></p>""",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext(
                to: 'dakshrajesh04@gmail.com',
                // to: 'dakshrajesh04@gmail.com',
                replyTo: 'dakshrajesh04@gmail.com',
                subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """<p>Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}</p>
                        <p>Console: <a href='${env.BUILD_URL}'>${env.BUILD_URL}</a></p>""",
                mimeType: 'text/html'
            )
        }
    }


}
