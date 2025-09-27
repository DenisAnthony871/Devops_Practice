# Complete DevOps Pipeline Demo

[![CI](https://github.com/DenisAnthony871/Devops_Practice/actions/workflows/ci.yml/badge.svg)](https://github.com/DenisAnthony871/Devops_Practice/actions/workflows/ci.yml)

* **Author:** YOUR_NAME
* **Date:** 2025-09-27

## Project Description

This project demonstrates a complete end-to-end DevOps pipeline including:

* **Development**: Python application with Git version control
* **Containerization**: Docker for consistent environments
* **CI/CD**: Automated testing with GitHub Actions
* **Deployment**: Container orchestration with HashiCorp Nomad
* **Monitoring**: Log aggregation with Grafana Loki

### Pipeline Flow

1. Code changes pushed to GitHub
2. GitHub Actions automatically tests the code
3. Docker image built and pushed to Docker Hub
4. Nomad deploys the container
5. Loki collects and aggregates logs

This repository demonstrates a complete DevOps workflow including:

* Version control with Git
* Basic scripting
* Docker containerization
* CI/CD with GitHub Actions
* Deployment with HashiCorp Nomad
* Monitoring using Grafana Loki

## Project Structure

```plaintext
.
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions workflow
├── monitoring/
│   └── loki_setup.txt      # Loki configuration guide
├── nomad/
│   └── hello.nomad         # Nomad job specification
├── scripts/
│   └── sysinfo.sh         # System information script
├── .gitignore             # Git ignore patterns
├── Dockerfile             # Container definition
├── README.md             # This documentation
└── hello.py              # Main Python application
```

## Step-by-Step Pipeline Implementation

### 1. Development Environment

#### Python Application (hello.py)

```python
print("Hello, DevOps!")
```

### 2. Containerization

#### Docker Configuration (Dockerfile)

```dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY hello.py .

# Command to run on startup
CMD ["python", "hello.py"]
```

### 3. Continuous Integration

#### GitHub Actions Workflow (.github/workflows/ci.yml)

```yaml
name: Basic CI

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Run script
        run: python hello.py
```

### 4. Container Orchestration

#### Nomad Job Configuration (nomad/hello.nomad)

```hcl
job "hello-devops-job" {
  datacenters = ["dc1"]
  type = "service"

  group "hello-group" {
    count = 1

    task "hello-task" {
      driver = "docker"

      config {
        image = "DOCKERHUB_USERNAME/hello-devops:latest"
      }

      resources {
        cpu    = 100 # MHz
        memory = 64  # MB
      }
    }
  }
}
This repository documents a complete DevOps workflow, including version control, scripting, containerization, CI/CD, deployment, and monitoring.

## 1. Git & GitHub Setup
This repository includes:
* Python script (`hello.py`) that prints "Hello, DevOps!"
* README.md with project documentation
* Proper Git configuration and .gitignore

## 2. Linux & Scripting Basics
The `scripts/sysinfo.sh` script provides system information:
* Current user (whoami)
* Current date
* Disk usage (df -h)

To run the script:
```bash
chmod +x scripts/sysinfo.sh
./scripts/sysinfo.sh
```

## 3. Docker Container

The application is containerized using Docker. The `Dockerfile` uses a lightweight Python image and copies the script into the container.

To build and run:

```bash
# Build the Docker image
docker build -t hello-devops .

# Run the container
docker run --rm hello-devops
```

To publish to Docker Hub:

```bash
# Log in to Docker Hub
docker login

# Tag and push the image
docker tag hello-devops DOCKERHUB_USERNAME/hello-devops:latest
docker push DOCKERHUB_USERNAME/hello-devops:latest
```

## 4. CI/CD with GitHub Actions

The repository uses GitHub Actions for continuous integration. On each push to main:

* Checks out the code
* Runs the Python script
* Reports success/failure

The workflow file is located at `.github/workflows/ci.yml`

## 5. Nomad Deployment

The application can be deployed to Nomad using the job configuration in `nomad/hello.nomad`. The job:

* Uses the Docker driver
* Runs a single instance
* Allocates minimal resources (100MHz CPU, 64MB memory)

To deploy:

```bash
# Verify the Nomad configuration
nomad job validate nomad/hello.nomad

# Deploy the job
nomad job run nomad/hello.nomad

# Check job status
nomad job status hello-devops-job
```

Note: Update the Docker image name in `nomad/hello.nomad` with your Docker Hub username before deployment.

## 6. Monitoring with Loki

This project uses Grafana Loki for log aggregation and monitoring. The setup includes:

* Loki for log storage
* Promtail for log collection
* Docker Compose for orchestration

Setup steps:

1. Navigate to the monitoring directory:

   ```bash
   cd monitoring
   ```

2. Create required configuration files:
   * `docker-compose.yml` for service definitions
   * `promtail-config.yml` for log collection rules

3. Start the monitoring stack:

   ```bash
   docker-compose up -d
   ```

4. View logs using either:
   * Grafana web interface (if configured)
   * Loki's logcli tool: `logcli query '{job="containerlogs"}'`

For detailed setup instructions and configuration examples, see [monitoring/loki_setup.txt](monitoring/loki_setup.txt).
