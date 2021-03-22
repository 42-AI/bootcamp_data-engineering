terraform {
  required_version = ">=0.12"
}

provider "aws" {
  region = var.region
}

###########
#   VPC   #
###########

resource "aws_vpc" "module02_vpc" {
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

resource "aws_subnet" "module02_public_subnet" {
  depends_on = [aws_vpc.module02_vpc]

  vpc_id                  = aws_vpc.module02_vpc.id
  count                   = length(var.availability_zones)
  availability_zone       = var.availability_zones[count.index]
  cidr_block              = cidrsubnet(var.vpc_cidr, 8, count.index + 1)
  map_public_ip_on_launch = true

  tags = {
    "Name"    = "${var.project_name}-pub-${count.index + 1}"
    "Project" = var.project_name
  }
}