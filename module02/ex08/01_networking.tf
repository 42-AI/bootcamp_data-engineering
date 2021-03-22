terraform {
  required_version = ">=0.12"
}

provider "aws" {
  region = var.region
}

###########
#   VPC   #
###########

resource "aws_vpc" "cloud1_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true

  tags = {
    "Name"    = "${var.project_name}-vpc"
    "Project" = var.project_name
  }
}

###############
#   SUBNETS   #
###############

resource "aws_subnet" "cloud1_public_subnet" {
  depends_on = [aws_vpc.cloud1_vpc]

  vpc_id                  = aws_vpc.cloud1_vpc.id
  count                   = length(var.availability_zones)
  availability_zone       = var.availability_zones[count.index]
  cidr_block              = cidrsubnet(var.vpc_cidr, 8, count.index + 1)
  map_public_ip_on_launch = true

  tags = {
    "Name"    = "${var.project_name}-pub-${count.index + 1}"
    "Project" = var.project_name
  }
}

resource "aws_subnet" "cloud1_private_subnet" {
  depends_on = [aws_vpc.cloud1_vpc]

  vpc_id                  = aws_vpc.cloud1_vpc.id
  count                   = length(var.availability_zones) - 1
  availability_zone       = var.availability_zones[count.index]
  cidr_block              = cidrsubnet(var.vpc_cidr, 8, count.index + 4)
  map_public_ip_on_launch = false

  tags = {
    "Name"    = "${var.project_name}-priv-${count.index + 1}"
    "Project" = var.project_name
  }
}

###########
#   IGW   #
###########

resource "aws_internet_gateway" "cloud1_igw" {
  depends_on = [aws_vpc.cloud1_vpc]
  vpc_id     = aws_vpc.cloud1_vpc.id

  tags = {
    "Name"    = "${var.project_name}-igw"
    "Project" = var.project_name
  }
}

###################
#   ROUTE TABLE   #
###################

resource "aws_route_table" "cloud1_public_rt" {
  depends_on = [
    aws_vpc.cloud1_vpc,
    aws_internet_gateway.cloud1_igw
  ]

  vpc_id = aws_vpc.cloud1_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.cloud1_igw.id
  }

  tags = {
    "Name"    = "${var.project_name}-pub-rt"
    "Project" = var.project_name
  }
}


#   Route table association
##############################

resource "aws_route_table_association" "cloud1_public_rt_assoc" {
  depends_on = [
    aws_route_table.cloud1_public_rt,
    aws_subnet.cloud1_public_subnet
  ]

  count          = length(aws_subnet.cloud1_public_subnet)
  subnet_id      = aws_subnet.cloud1_public_subnet[count.index].id
  route_table_id = aws_route_table.cloud1_public_rt.id
}