#######################
#   SECURITY GROUPS   #
#######################

resource "aws_security_group" "day03_wp_sg" {

  depends_on = [
    aws_vpc.day03_vpc,
    aws_subnet.day03_sn_1
  ]

  description = "HTTP, SSH"
  name = "wordpress-sg"
  vpc_id = aws_vpc.day03_vpc.id

  ingress {
    description = "HTTP for wordpress server"
    from_port   = 80
    to_port     = 80

    protocol    = "tcp"
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

resource "aws_security_group" "day03_mysql_sg" {

  depends_on = [
    aws_vpc.day03_vpc,
    aws_subnet.day03_sn_1,
    aws_subnet.day03_sn_2,
    aws_security_group.day03_wp_sg
  ]

  description = "MySQL access for wordpress server"
  name = "mysql-sg"
  vpc_id = aws_vpc.day03_vpc.id

  ingress {
    description = "MySQL Access"
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    security_groups = [aws_security_group.day03_wp_sg.id]
  }

  egress {
    description = "output from MySQL"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
