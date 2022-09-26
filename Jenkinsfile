pipeline{

    agent any

    triggers{ // Pipeline triggered on build // https://www.jenkins.io/doc/book/pipeline/syntax/#triggers
        pollSCM('')
    }

    environment{ // Create environments
        DOCKERHUB_CREDENTIALS=credentials('dockerhub') //
        IMAGE_NAME='aadelugba/iris_ml_image_jenkins:latest'
    }

    stages{

        stage("Install Requirements"){

            steps{
                // Install Python Dependencies
                echo 'Installing Python Dependencies and Requirements ...'
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }

        }

        // stage("Build"){

        //     steps{
        //         // Build ML Model
        //         echo 'Building ML Model ...'
        //         sh 'python src/training.py'                
        //     }

        // }

        stage("Test"){

            steps{
                // Run Python Tests
                echo 'Running Python Tests ...'
                sh 'pytest'                
            }

        }

        stage("Build & Push Image"){

            steps{
                // Build Docker Image
                echo 'Building Docker Image ...'
                sh "docker build -t ${IMAGE_NAME}"

                // Log into DockerHub
                withCredentials([
                    usernamePassword(credentials: 'dockerhub', usernameVariable: USER, passwordVariable: PWD)
                ])                
                sh "echo ${PWD} | docker login -u ${USER} --password-stdin"

                // Push Image Built into DockerHub
                echo 'Pushing Image to DockerHub Repository ...'
                sh "docker push ${IMAGE_NAME}"
                echo 'Image Successfully Pushed to DockerHub.'
            }

        } 

    }

    post {
        always{
            // Log out of DockerHub
            sh 'docker logout'
            echo 'Successfully logged out of Docker.'
        }
    }
}