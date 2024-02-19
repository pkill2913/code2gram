terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}
# variable "region" {
#     region = "us-east-1"
# }
provider "aws" {
  skip_credentials_validation = true
  skip_requesting_account_id  = true
  skip_metadata_api_check     = true
  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"
  region =   "us-east-1"
}

resource "aws_instance" "example_server" {
  ami           = "ami-04e914639d0cca79a"
  instance_type = "t2.micro"
  tags = {
    Name = "JacksBlogExample"
  }
}

resource "aws_instance" "web_server" {
  ami           = "ami-04e914639d0cca79a"
  instance_type = "t2.micro"
  tags = {
    Name = "JacksBlogExample"
  }
}