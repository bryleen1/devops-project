pipeline {
    agent any
    stages {
        stage('Unit tests for services') {
            steps {
                sh "bash tests.sh"
            }
        }
        stage('Build images') {
            steps {
                sh "docker-compose build --parallel"
            }
        }
        stage('Deploy') {
            steps {
                sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-manager:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarm-manager:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }
    }
    post {
        always {
            junit '**/*.xml'
            cobertura coberturaReportFile: 'front-end/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'truth_api/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'dare_api/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'merge_api/coverage.xml', failNoReports: false
        }
    }
}