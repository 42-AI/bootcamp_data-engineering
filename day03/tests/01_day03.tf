provider "aws" {
  region  = var.region
}

# Create a VPC
resource "aws_vpc" "day03" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = "true"

  tags = {
      "Name": "day03-vpc"
      "Project": var.project_name
  }
}