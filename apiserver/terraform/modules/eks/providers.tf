terraform {
  backend "s3" {}
}
provider "aws" {
  region     = var.aws_region
  access_key = var.PROVIDER_ACCESS_KEY
  secret_key = var.PROVIDER_SECRET_KEY
}
