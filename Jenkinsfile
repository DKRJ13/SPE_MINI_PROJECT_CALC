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
                // Use Jenkins credentials (username/password) with id 'dockerhub-cred'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh 'docker tag scientific-calculator:latest ${DOCKERHUB_USER}/scientific-calculator:latest'
                    sh 'echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin'
                    sh 'docker push ${DOCKERHUB_USER}/scientific-calculator:latest'
                }
            }
        }

        // stage('Deploy with Ansible') {
        //     steps {
        //         // Pass Docker Hub creds into Ansible to pull private images if needed
        //         withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
        //             sh '''
        //                 ansible-galaxy collection install community.docker
        //                 python3 -m pip install --user docker
        //                 ansible-playbook ansible/playbook.yml -i inventory/hosts.ini -c local \
        //                   --extra-vars "image_name=${DOCKERHUB_USER}/scientific-calculator:latest registry_username=${DOCKERHUB_USER} registry_password=${DOCKERHUB_PASS}"
        //             '''
        //         }
        //     }
        // 

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
}
