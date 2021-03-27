#####################
#   LOAD BALANCER   #
#####################

resource "aws_elb" "module02_elb" {
  name                      = "module02-elb"
  subnets                   = aws_subnet.module02_subnet.*.id
  security_groups           = [aws_security_group.elb_sg.id]
  cross_zone_load_balancing = true

  health_check {
    target              = "TCP:5000"
    interval            = 30
    timeout             = 3
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }

  listener {
    lb_port           = 5000
    lb_protocol       = "tcp"
    instance_port     = 5000
    instance_protocol = "tcp"
  }
}

output "elb_dns_name" {
  value       = aws_elb.module02_elb.dns_name
  description = "The domain name of the load balancer"
}