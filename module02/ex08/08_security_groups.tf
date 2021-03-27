resource "aws_security_group" "module02_sg" {
  depends_on = [
    aws_default_vpc.default
  ]

  name        = "module02-sg"
  description = "TCP, SSH"
  vpc_id      = aws_default_vpc.default.id

  ingress {
    from_port = 5000
    to_port = 5000
    protocol = "tcp"
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