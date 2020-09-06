provider "aws" {
  region  = var.region
}

###########
#   VPC   #
###########

resource "aws_vpc" "day03_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
      "Name"    = "day03-vpc"
      "Project" = var.project_name
  }
}

###############
#   SUBNETS   #
###############

resource "aws_subnet" "day03_sn_1" {
  depends_on = [
    aws_vpc.day03_vpc
  ]

  vpc_id     = aws_vpc.day03_vpc.id
  cidr_block = "10.0.1.0/28"
  map_public_ip_on_launch = true
  availability_zone = "eu-west-1a"

  tags = {
    "Name"    = "day03-sn-1"
    "Project" = var.project_name
  }
}

resource "aws_subnet" "day03_sn_2" {
  depends_on = [
    aws_vpc.day03_vpc
  ]

  vpc_id     = aws_vpc.day03_vpc.id
  cidr_block = "10.0.2.0/28"
  map_public_ip_on_launch = true
  availability_zone = "eu-west-1b"

  tags = {
    "Name"    = "day03-sn-2"
    "Project" = var.project_name
  }
}

###########
#   IGW   #
###########

resource "aws_internet_gateway" "day03_igw" {
  depends_on = [
    aws_vpc.day03_vpc,
    aws_subnet.day03_sn_1,
    aws_subnet.day03_sn_2
  ]
  
  vpc_id = aws_vpc.day03_vpc.id

  tags = {
    "Name"    = "day03-igw"
    "Project" = var.project_name
  }
}

###################
#   ROUTE TABLE   #
###################

resource "aws_route_table" "day03_rt" {
  depends_on = [
    aws_vpc.day03_vpc,
    aws_internet_gateway.day03_igw
  ]

  vpc_id = aws_vpc.day03_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.day03_igw.id
  }

  tags = {
    "Name"    = "day03-rt"
    "Project" = var.project_name
  }
}

resource "aws_route_table_association" "day03_sn1_rt" {

  depends_on = [
    aws_vpc.day03_vpc,
    aws_subnet.day03_sn_1,
    aws_route_table.day03_rt
  ]

  subnet_id      = aws_subnet.day03_sn_1.id

  route_table_id = aws_route_table.day03_rt.id
}

resource "aws_route_table_association" "day03_sn2_rt" {

  depends_on = [
    aws_vpc.day03_vpc,
    aws_subnet.day03_sn_2,
    aws_route_table.day03_rt
  ]

  subnet_id      = aws_subnet.day03_sn_2.id

  route_table_id = aws_route_table.day03_rt.id
}

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

###########
#   RDS   #
###########

resource "aws_db_instance" "default" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "8.0.17"
  instance_class       = "db.t2.micro"
  name                 = "wordpress"
  username             = var.rds_user
  password             = var.rds_password
  parameter_group_name = "default.mysql8.0"
}