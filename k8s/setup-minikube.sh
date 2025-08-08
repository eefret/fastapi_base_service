#!/bin/bash
set -e

echo "🚀 Setting up FastAPI microservice with ELK stack on Minikube"

# Check if minikube is installed
if ! command -v minikube &> /dev/null; then
    echo "❌ Minikube is not installed. Please install it first."
    exit 1
fi

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl is not installed. Please install it first."
    exit 1
fi

# Start minikube with sufficient resources
echo "🔧 Starting Minikube with sufficient resources..."
minikube start --cpus=4 --memory=8192 --disk-size=20gb --driver=docker

# Enable required addons
echo "🔧 Enabling Minikube addons..."
minikube addons enable ingress
minikube addons enable metrics-server

# Create namespace
echo "📦 Creating namespace..."
kubectl apply -f namespace.yml

# Deploy Elasticsearch
echo "📊 Deploying Elasticsearch..."
kubectl apply -f elasticsearch.yml

# Wait for Elasticsearch to be ready
echo "⏳ Waiting for Elasticsearch to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/elasticsearch -n fastapi-microservice

# Deploy OpenTelemetry Collector
echo "🔍 Deploying OpenTelemetry Collector..."
kubectl apply -f otel-collector.yml

# Wait for OpenTelemetry Collector to be ready
echo "⏳ Waiting for OpenTelemetry Collector to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/otel-collector -n fastapi-microservice

# Deploy Kibana
echo "🔍 Deploying Kibana..."
kubectl apply -f kibana.yml

# Wait for Kibana to be ready
echo "⏳ Waiting for Kibana to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/kibana -n fastapi-microservice

# Build and load FastAPI image
echo "🐳 Building FastAPI Docker image..."
cd ..
docker build -t fastapi-base-service:latest .
minikube image load fastapi-base-service:latest
cd k8s

# Deploy FastAPI application
echo "🚀 Deploying FastAPI application..."
kubectl apply -f fastapi-app.yml

# Wait for FastAPI app to be ready
echo "⏳ Waiting for FastAPI application to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/fastapi-app -n fastapi-microservice

# Add hosts entries
echo "🌐 Setting up local DNS..."
MINIKUBE_IP=$(minikube ip)
echo "Add these entries to your /etc/hosts file:"
echo "$MINIKUBE_IP    fastapi-app.local"
echo "$MINIKUBE_IP    kibana.local"

# Display service URLs
echo ""
echo "✅ Deployment completed successfully!"
echo ""
echo "🔗 Access your services:"
echo "   FastAPI App: http://fastapi-app.local"
echo "   API Docs:    http://fastapi-app.local/docs"
echo "   Kibana:      http://kibana.local"
echo ""
echo "📊 Check deployment status:"
echo "   kubectl get all -n fastapi-microservice"
echo ""
echo "🔍 View logs:"
echo "   kubectl logs -f deployment/fastapi-app -n fastapi-microservice"
echo ""
echo "🧹 To cleanup:"
echo "   kubectl delete namespace fastapi-microservice"
echo "   minikube stop"
