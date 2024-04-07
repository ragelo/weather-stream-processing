# Meteo-station real time metrics [Work in progress]

I was inspired by [1 billion records challenge](https://github.com/gunnarmorling/1brc), but the idea of language-effective processing of a single file was a bit off the real world scenario for such app. Instead, you would have a stream of data instead from each station.

This project is about creating an efficient close-realtime solution to process ingested data, and exposing an API to fetch data withn 30s, 60s, 5m windows.

# Architecture

Each region's data would be generated and processed within the same region in a real world app, but at least for the first iteration, I will do it in a single region.

Planned tech to use (can change during while project is in progress):
- Kubernetes
- Kafka
- Prometheus & Graphana


# Mock data

To create mock data generators, I would use [World Cities Database](https://simplemaps.com/data/world-cities), but slightly modify it.

# Processing

# Start

```bash
brew install minikube

minikube start --memory 8196 --cpus=4 --driver=docker --bootstrapper=kubeadm --extra-config=kubelet.authentication-token-webhook=true --extra-config=kubelet.authorization-mode=Webhook --extra-config=scheduler.bind-address=0.0.0.0 --extra-config=controller-manager.bind-address=0.0.0.0

minikube addons enable ingress



```

```
/bin/kafka-topics --create --topic weatherstation-events --bootstrap-server localhost:9092
```
