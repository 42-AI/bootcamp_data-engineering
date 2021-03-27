################
#   KEY-PAIR   #
################

resource "tls_private_key" "tf_key" {
  algorithm = "RSA"
  rsa_bits = 4096
}

resource "aws_key_pair" "new_kp" {
  key_name = "module02-kp"
  public_key = tls_private_key.tf_key.public_key_openssh
}

resource "local_file" "key_file" {
  content = tls_private_key.tf_key.private_key_pem
  filename = "${var.key_name}.pem"
  file_permission = "0400"
}

###########
#   AMI   #
###########

data "aws_ami" "amazon-linux-2" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
}

#####################
#   TEMPLATE FILE   #
#####################

data "template_file" "bootstrap" {
  template = file("user_data/bootstrap.sh")
}

###########################
#   LAUCH CONFIGURATION   #
###########################

resource "aws_launch_configuration" "flask_api_configuration" {
  depends_on = [
    aws_security_group.module02_sg
  ]

  image_id                    = data.aws_ami.amazon-linux-2.id
  associate_public_ip_address = true
  instance_type               = var.server_instance_class
  key_name                    = "module02-kp"
  security_groups             = [aws_security_group.module02_sg.id]
  iam_instance_profile        = "module02_s3FullAccessProfile"
  user_data                   = data.template_file.bootstrap.rendered

  lifecycle {
    create_before_destroy = true
  }
}

#########################
#   AUTOSCALING GROUP   #
#########################

resource "aws_autoscaling_group" "module02_asg" {
  depends_on = [aws_launch_configuration.flask_api_configuration]

  launch_configuration = aws_launch_configuration.flask_api_configuration.id
  vpc_zone_identifier  = aws_subnet.module02_subnet.*.id

  min_size          = var.asg_min_conf
  max_size          = var.asg_max_conf
  load_balancers    = [aws_elb.module02_elb.name]
  health_check_type = "ELB"

  tag {
    key                 = "module02 auto-scaling group"
    value               = "module02-asg"
    propagate_at_launch = true
  }
}