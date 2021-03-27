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
  filename = "module02.pem"
  file_permission = "0400"
}

###########
#   EC2   #
###########

data "template_file" "bootstrap" {
  template = file("user_data/bootstrap.sh")
}

resource "aws_instance" "module02_ec2" {
  depends_on = [
    aws_key_pair.new_kp,
    aws_iam_instance_profile.module02_s3FullAccessProfile,
    aws_security_group.module02_sg
  ]
  ami = "ami-0d712b3e6e1f798ef"
  instance_type = "t2.micro"
  key_name = "module02-kp"
  iam_instance_profile = "module02_s3FullAccessProfile"
  vpc_security_group_ids = [
      aws_security_group.module02_sg.id
  ]
  associate_public_ip_address = true
  user_data = data.template_file.bootstrap.rendered

  provisioner "file" {
    source      = "user_data/app.py"
    destination = "/home/ec2-user/app.py"

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = tls_private_key.tf_key.private_key_pem
      host        = self.public_dns
    }
  }

  provisioner "file" {
    source      = "user_data/s3_funcs.py"
    destination = "/home/ec2-user/s3_funcs.py"

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = tls_private_key.tf_key.private_key_pem
      host        = self.public_dns
    }
  }

  tags = {
    "Name"    = "${var.project_name}-ec2"
    "Project" = var.project_name
  }
}

output "instance_ip_addr" {
  value = aws_instance.module02_ec2.public_ip
}