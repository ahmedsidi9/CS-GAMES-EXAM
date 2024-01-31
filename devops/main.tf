provider "docker" {
  host = "tcp://localhost:2375"  # socket local machine
}

resource "docker_image" "rust_server" {
  name = "rust:latest" 
}

resource "docker_container" "rust_container" {
  name  = "rust-server-container"
  image = docker_image.rust_server.latest
  ports {
    internal = 80  # Port interne dans le conteneur
    external = 8080  # Port exposé sur votre machine locale
  }
  restart = "unless-stopped"
}
