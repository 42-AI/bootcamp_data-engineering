##############
#   EC2-SG   #
##############

resource "aws_security_group" "module02_sg" {
  depends_on = [
    aws_vpc.module02_vpc
  ]

  name        = "module02-sg"
  description = "TCP, SSH"
  vpc_id      = aws_vpc.module02_vpc.id

  ingress {
    from_port = 5000
    to_port = 5000
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "output from wordpress server"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

##############
#   ELB-SG   #
##############

resource "aws_security_group" "elb_sg" {
  vpc_id = aws_vpc.module02_vpc.id
  name   = "module02-elb"

  ingress {
    description = "Load balancer input"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Load balancer output"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}