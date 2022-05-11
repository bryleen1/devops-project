pipeline{
        agent any
        stages{
            stage('Testing Services'){
                steps{
                    sh "bash tests.sh"
                }
            }

            stage('Building and pushing images'){
                steps {
                    sh "ln -s devops-project/docker-compose.yaml build1"
                }
            }
        }
}