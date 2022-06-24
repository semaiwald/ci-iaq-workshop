def test_docker_is_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed
    # testen, ob das Paket "docker-ce" installiert ist

def test_docker_service_is_running(host):
    docker = host.service("docker-ce")
    assert docker.is_running
    # testen, ob der Service "docker" läuft und verfügbar ist

def test_heroapp_container_is_running(host):
    myheroapp = host.docker("my-hero-app")
    assert myheroapp.is_running
    # testen, ob der container mit dem Namen "my-hero-app" läuft

def test_heroapp_is_available_on_port_80(host):
    port80 = host.socket ("tcp://0.0.0.0:80")
    assert port80.is_listening
    # testen, ob auf tcp://0.0.0.0:80 gehorcht wird
