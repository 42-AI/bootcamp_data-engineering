#   Project
##############

region       = "eu-west-1"
project_name = "module02"

#   Networking
#################

vpc_cidr           = "10.0.0.0/16"
availability_zones = ["eu-west-1a", "eu-west-1b"]

#   Auto-scaling group
#########################

server_instance_class = "t2.micro"
key_name              = "module02"
asg_min_conf          = 2
asg_max_conf          = 2