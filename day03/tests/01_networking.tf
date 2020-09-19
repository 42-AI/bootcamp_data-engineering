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

resource "aws_route" "route1" {
  depends_on = [
    aws_vpc.day03_vpc,
    aws_subnet.day03_sn_1,
    aws_route_table.day03_rt
  ]
  route_table_id = aws_route_table.day03_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = aws_internet_gateway.day03_igw.id
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