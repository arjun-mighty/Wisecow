# Wisecow Kubernetes Project

This repository contains the containerized version of the Wisecow application, along with Kubernetes manifests and CI/CD pipelines for automated deployment.

## Overview

Wisecow is a simple web server that displays random quotes from the `fortune` command formatted as ASCII art using `cowsay`. This project demonstrates how to:

1. Containerize a simple bash application
2. Deploy it to Kubernetes
3. Implement CI/CD using GitHub Actions
4. Enable secure TLS communication

## Project Structure

```
.
├── Dockerfile                 # Docker image definition
├── wisecow.sh                 # Main application script
├── kubernetes/                # Kubernetes manifests
│   ├── wisecow-deployment.yaml
│   ├── wisecow-service.yaml
│   ├── wisecow-ingress.yaml
│   └── cert-manager-issuer.yaml
└── .github/
    └── workflows/
        └── ci-cd.yaml        # GitHub Actions workflow
```

## Containerization

The application is containerized using Docker. The Dockerfile installs the necessary dependencies (`fortune-mod`, `cowsay`, and `netcat-openbsd`) and configures the application to run on port 4499.

To build the Docker image locally:

```bash
docker build -t wisecow:latest .
```

To run the container locally:

```bash
docker run -p 4499:4499 wisecow:latest
```

## Kubernetes Deployment

The application is deployed to Kubernetes using the following resources:

- **Deployment**: Manages the Wisecow application pods with proper resource limits and health checks
- **Service**: Exposes the application within the cluster
- **Ingress**: Exposes the application outside the cluster with TLS termination
- **ClusterIssuer**: Configures cert-manager to issue and manage TLS certificates

To deploy to Kubernetes manually:

```bash
# Apply Kubernetes manifests
kubectl apply -f kubernetes/wisecow-deployment.yaml
kubectl apply -f kubernetes/wisecow-service.yaml
kubectl apply -f kubernetes/wisecow-ingress.yaml
kubectl apply -f kubernetes/cert-manager-issuer.yaml
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment:

1. **On code push**:
   - The workflow builds a Docker image
   - Pushes the image to Docker Hub
   - Deploys the updated application to Kubernetes

### Prerequisites for CI/CD

To use the CI/CD pipeline, you need to set up the following GitHub Secrets:

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password
- `KUBECONFIG`: Your Kubernetes cluster configuration (base64 encoded)

To obtain the base64 encoded kubeconfig:

```bash
cat ~/.kube/config | base64
```

## TLS Implementation

The application is secured with TLS using cert-manager and Let's Encrypt:

1. cert-manager automatically requests and manages certificates
2. The Ingress resource is configured with TLS settings
3. Let's Encrypt issues free certificates with automatic renewal

### Prerequisites for TLS

1. Install cert-manager in your cluster:

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0/cert-manager.yaml
```

2. Update the email address in `cert-manager-issuer.yaml`
3. Update the hostname in the Ingress resource to match your domain

## Accessing the Application

Once deployed, the application can be accessed at:

```
https://wisecow.example.com
```

(Replace `wisecow.example.com` with your actual domain)

## Local Development

To run the application locally without Docker:

1. Install prerequisites:
   ```bash
   sudo apt install fortune-mod cowsay -y
   ```

2. Run the script:
   ```bash
   ./wisecow.sh
   ```

3. Access the application at `http://localhost:4499`

## Troubleshooting

### Common Issues

1. **Pods not starting**: Check events with `kubectl describe pod <pod-name>`
2. **Certificate issues**: Verify cert-manager logs with `kubectl logs -n cert-manager -l app=cert-manager`
3. **Ingress not working**: Ensure your Ingress controller is properly configured

### Logs

To view application logs:

```bash
kubectl logs -l app=wisecow
```
