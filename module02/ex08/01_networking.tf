terraform {
  required_version = ">=0.12"
}

provider "aws" {
  region = var.region
}

resource "aws_default_vpc" "default" {
  tags = {
    Name = "Default VPC"
  }
}