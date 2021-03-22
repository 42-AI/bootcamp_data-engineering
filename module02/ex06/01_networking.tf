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