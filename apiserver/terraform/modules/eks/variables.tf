variable "kubernetes_version" {
  type        = string
  description = "kubernetes version"
  default     = "1.26"
}
variable "subnet_ids" {
  type        = list(string)
  description = "List of subnet IDs. Must be in at least two different availability zones. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane."
  nullable    = false
}
variable "aws_region" {
  type        = string
  description = "AWS region to deploy the EKS cluster"
  nullable    = false
}
