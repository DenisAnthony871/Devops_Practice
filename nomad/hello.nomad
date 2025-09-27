job "hello-devops-job" {
  datacenters = ["dc1"]
  type = "service"

  group "hello-group" {
    count = 1

    task "hello-task" {
      driver = "docker"

      config {
        image = "denis0506/hello-devops:latest"
      }

      resources {
        cpu    = 100 # MHz
        memory = 64  # MB
      }
    }
  }
}