###########
#   RDS   #
###########

resource "aws_db_subnet_group" "db_subnet" {
  name = "db_subnet_group"
  subnet_ids = [aws_subnet.day03_sn_1.id, aws_subnet.day03_sn_2.id]
}

resource "aws_db_instance" "mysql_wordpress" {
  allocated_storage    = 20
  identifier           = var.rds_identifier
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "8.0.17"
  instance_class       = "db.t2.micro"
  name                 = var.rds_db
  username             = var.rds_user
  password             = var.rds_password
  parameter_group_name = "default.mysql8.0"
  db_subnet_group_name = aws_db_subnet_group.db_subnet.name
  skip_final_snapshot  = true
  vpc_security_group_ids = [aws_security_group.day03_mysql_sg.id]

  tags = {
    "Name"    = "day03-mysql"
    "Project" = var.project_name
  }
}