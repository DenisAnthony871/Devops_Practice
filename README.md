# DevOps Intern Final Assessment

[![CI](https://github.com/DenisAnthony871/Devops_Practice/actions/workflows/ci.yml/badge.svg)](https://github.com/DenisAnthony871/Devops_Practice/actions/workflows/ci.yml)

* **Name:** Denis Anthony
* **Date:** 2025-09-27

## Project Description

This repository contains the final assessment project for the DevOps internship. It demonstrates a complete DevOps workflow including version control, scripting, containerization, CI/CD, deployment, and monitoring.

## 3. Docker Container

To build and run this project as a Docker container:

```bash
# Build the Docker image
docker build -t hello-devops .

# Run the container
docker run --rm hello-devops

# Optional: Push to Docker Hub (after logging in)
docker tag hello-devops your-username/hello-devops:latest
docker push your-username/hello-devops:latest

## 4. Nomad Deployment

To deploy the application using Nomad:

```bash
# Verify the Nomad configuration
nomad job validate nomad/hello.nomad

# Deploy the job
nomad job run nomad/hello.nomad

# Check job status
nomad job status hello-devops-job
```

Note: Make sure to update the Docker image name in `nomad/hello.nomad` with your Docker Hub username before deployment.

## 5. Monitoring with Loki

This project includes a logging setup using Grafana Loki and Promtail. To set up monitoring:

```bash
# Navigate to the monitoring directory
cd monitoring

# Follow setup instructions in loki_setup.txt
cat loki_setup.txt

# Start the monitoring stack
docker-compose up -d
```

View logs using either:
- Grafana web interface (if configured)
- Loki's logcli tool: `logcli query '{job="containerlogs"}'`

For detailed setup instructions and configuration, see [monitoring/loki_setup.txt](monitoring/loki_setup.txt).
