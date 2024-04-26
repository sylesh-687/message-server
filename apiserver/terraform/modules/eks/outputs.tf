output "eks_endpoint" {
  description = "EKS API server endpoint"
  value       = aws_eks_cluster.eks-cluster.endpoint
}

output "cluster_name" {
  description = "Cluster name"
  value       = aws_eks_cluster.eks-cluster.name
}
