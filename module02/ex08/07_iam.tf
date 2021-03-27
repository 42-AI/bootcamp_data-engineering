############
#   ROLE   #
############

resource "aws_iam_role" "module02_s3FullAccessRole" {
  name = "module02_s3FullAccessRole"

  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "ec2.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
  })

  tags = {
    "Name"    = "${var.project_name}-s3FullAccessRole"
    "Project" = var.project_name
  }
}

###############
#   PROFILE   #
###############

resource "aws_iam_instance_profile" "module02_s3FullAccessProfile" {
  depends_on = [
    aws_iam_role.module02_s3FullAccessRole
  ]
  name = "module02_s3FullAccessProfile"
  role = aws_iam_role.module02_s3FullAccessRole.name
}

##############
#   POLICY   #
##############

resource "aws_iam_role_policy" "module02_s3FullAccessPolicy" {
  depends_on = [
    aws_iam_role.module02_s3FullAccessRole
  ]
  name = "module02_s3FullAccessPolicy"
  role = aws_iam_role.module02_s3FullAccessRole.id

  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": [
          "s3:*"
        ],
        "Effect": "Allow",
        "Resource": "*"
      }
    ]
  })
}

# aws iam delete-instance-profile --instance-profile-name module02_s3FullAccessProfile