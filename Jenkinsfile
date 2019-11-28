pipeline{
    agent any
    parameters{
        string(
            description: 'target instanceId',
            name:'targetID'
        )
        choice(
            choices:'Add\nRemove',
            description: 'provide your action here',
            name: 'Action'
        )
    }
    stages{
        stage('Add'){
                when {
                    expression {
                        params.Action == "Add"
                        }
                }
                steps{
                    
                    sh '''echo "We are going to add targets to target group"
                          echo $Action
                          pwd
                          python script.py
                          echo $targetID
                          aws elbv2 describe-target-health --target-group-arn arn:aws:elasticloadbalancing:us-east-1:967503416995:targetgroup/target-group-jenkins/7469e804f4a073ee
                          '''
                }
        }
        stage('Remove'){
                when{
                    expression{
                        params.Action == 'Remove'
                    }
                }
                steps{
                    
                    sh '''echo "we are removing the targets"
                    echo $Action
                    python script.py
                    echo $targetID
                    aws elbv2 describe-target-health --target-group-arn arn:aws:elasticloadbalancing:us-east-1:967503416995:targetgroup/target-group-jenkins/7469e804f4a073ee
                    '''
                }

            }
    }
    post{
        always{
            cleanWs()
        }
    }
}
