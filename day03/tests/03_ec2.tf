###########
#   EC2   #
###########


data "aws_ami" "amazon-linux-2" {
  depends_on = [
      aws_db_instance.mysql_wordpress 
  ]

  most_recent = true
  owners = ["amazon"]

  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
}

data "template_file" "init" {
  template = "${file("ec2_bootstrap.sh.tpl")}"

  vars = {
    rds_address = aws_db_instance.mysql_wordpress.address,
    rds_db = var.rds_db
    rds_user = var.rds_user,
    rds_password = var.rds_password
  }
}

resource "aws_instance" "test" {
    depends_on = [
        aws_internet_gateway.day03_igw,
        aws_db_instance.mysql_wordpress
    ]


 ami                         = data.aws_ami.amazon-linux-2.id
 associate_public_ip_address = true
 instance_type               = "t2.micro"
 key_name                    = "ddd"
 vpc_security_group_ids      = [aws_security_group.day03_wp_sg.id]
 subnet_id                   = aws_subnet.day03_sn_1.id

 user_data = data.template_file.init.rendered

}