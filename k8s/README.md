# Kubernetes Deployment for FastAPI Microservice with ELK Stack

This directory contains Kubernetes manifests for deploying your FastAPI microservice with a complete observability stack (ELK + OpenTelemetry) on Minikube.

## 📋 Prerequisites

### Required Software
- **Minikube** v1.35.0+ - [Installation Guide](https://minikube.sigs.k8s.io/docs/start/)
- **kubectl** v1.30.0+ - [Installation Guide](https://kubernetes.io/docs/tasks/tools/)
- **Docker** - For building application images
- At least **8GB RAM** and **4 CPU cores** available for Minikube
- **20GB free disk space**

### System Requirements
```bash
# Verify prerequisites
minikube version
kubectl version --client
docker --version

# Check available resources
free -h  # Should show at least 8GB total memory
```

## 🚀 Quick Start

### 1. Start Minikube Cluster

```bash
# Start Minikube with sufficient resources
minikube start --cpus=2 --memory=4096 --disk-size=10gb --driver=docker

# Enable required addons
minikube addons enable ingress
minikube addons enable metrics-server

# Verify cluster is ready
minikube kubectl -- cluster-info
```

### 2. Build and Load Application Image

```bash
# From project root directory
cd ..

# Build Docker image
docker build -t fastapi-base-service:latest .

# Load image into Minikube
minikube image load fastapi-base-service:latest

# Verify image is loaded
minikube image ls | grep fastapi-base-service
```

### 3. Deploy the Application Stack

```bash
# Return to k8s directory
cd k8s

# Deploy in order (dependencies first)
minikube kubectl -- apply -f namespace.yml
minikube kubectl -- apply -f elasticsearch.yml
minikube kubectl -- apply -f otel-collector.yml
minikube kubectl -- apply -f fastapi-app.yml

# Optional: Deploy Kibana for visualization
minikube kubectl -- apply -f kibana.yml
```

### 4. Verify Deployment

```bash
# Check all resources
minikube kubectl -- get all -n fastapi-microservice

# Wait for pods to be ready
minikube kubectl -- wait --for=condition=ready pod -l app=elasticsearch -n fastapi-microservice --timeout=300s
minikube kubectl -- wait --for=condition=ready pod -l app=fastapi-app -n fastapi-microservice --timeout=300s
```

### 5. Access Your Application

#### Option A: Port Forwarding (Recommended for testing)
```bash
# Forward FastAPI service
minikube kubectl -- port-forward -n fastapi-microservice svc/fastapi-app 8000:8000

# Test in another terminal
curl http://localhost:8000/health
curl -X POST "http://localhost:8000/process" \
  -H "Content-Type: application/json" \
  -d '{"input_data": "kubernetes test", "options": {"env": "k8s"}}'
```

#### Option B: Ingress (Production-like)
```bash
# Get Minikube IP
MINIKUBE_IP=$(minikube ip)
echo "Minikube IP: $MINIKUBE_IP"

# Add to /etc/hosts (Linux/Mac)
sudo echo "$MINIKUBE_IP    fastapi-app.local" >> /etc/hosts
sudo echo "$MINIKUBE_IP    kibana.local" >> /etc/hosts

# Access services
curl -H "Host: fastapi-app.local" http://$MINIKUBE_IP/health
# Browser: http://fastapi-app.local/docs
```

## 📊 Accessing Observability Tools

### Kibana Dashboard
```bash
# If Kibana is deployed
minikube kubectl -- port-forward -n fastapi-microservice svc/kibana 5601:5601

# Access at: http://localhost:5601
```

### Application Logs
```bash
# View FastAPI logs
minikube kubectl -- logs -f deployment/fastapi-app -n fastapi-microservice

# View Elasticsearch logs
minikube kubectl -- logs -f deployment/elasticsearch -n fastapi-microservice

# View all logs
minikube kubectl -- logs -f -l app=fastapi-app -n fastapi-microservice --all-containers
```

## 🛠️ Makefile Commands

Use these convenient commands from the project root:

```bash
# Deploy full stack to Minikube
make k8s-deploy

# Check deployment status
make k8s-status

# View application logs
make k8s-logs

# Clean up deployment
make k8s-cleanup
```

## 🔧 Configuration

### Environment Variables

The FastAPI application can be configured via the `fastapi-config` ConfigMap in `fastapi-app.yml`:

```yaml
data:
  # Application settings
  APP_NAME: "FastAPI Microservice"
  DEBUG: "false"
  LOG_LEVEL: "INFO"

  # ELK Stack
  ELASTICSEARCH_URL: "http://elasticsearch:9200"
  ELASTICSEARCH_INDEX: "fastapi-logs-prod"

  # OpenTelemetry
  OTEL_SERVICE_NAME: "fastapi-base-service"
  ENABLE_TRACING: "true"
  ENABLE_METRICS: "true"
  ENABLE_LOGGING: "true"
```

### Resource Limits

Adjust resource requests and limits in the deployment manifests:

```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "200m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. Minikube Won't Start
```bash
# Check if there's an existing cluster
minikube status

# Delete existing cluster and recreate
minikube delete
minikube start --cpus=2 --memory=4096 --disk-size=10gb --driver=docker

# If Docker driver issues, try different driver
minikube start --driver=virtualbox  # or --driver=hyperkit
```

#### 2. Pods Stuck in "ImagePullBackOff"
```bash
# Verify image is loaded in Minikube
minikube image ls | grep fastapi-base-service

# If not found, rebuild and load
docker build -t fastapi-base-service:latest ..
minikube image load fastapi-base-service:latest

# Check imagePullPolicy in fastapi-app.yml should be "Never"
```

#### 3. Elasticsearch Pod CrashLoopBackOff
```bash
# Check logs
minikube kubectl -- logs deployment/elasticsearch -n fastapi-microservice

# Common causes and fixes:
# - Insufficient memory: Increase Minikube memory
# - Volume issues: Delete PVC and recreate
minikube kubectl -- delete pvc elasticsearch-pvc -n fastapi-microservice
```

#### 4. OpenTelemetry Collector Issues
```bash
# Check collector logs
minikube kubectl -- logs deployment/otel-collector -n fastapi-microservice

# Collector may crash initially while waiting for Elasticsearch
# This is normal - it will recover once Elasticsearch is ready

# If persistent issues, check Elasticsearch connectivity:
minikube kubectl -- exec -it deployment/elasticsearch -n fastapi-microservice -- curl localhost:9200/_cluster/health
```

#### 5. Ingress Not Working
```bash
# Verify ingress addon is enabled
minikube addons list | grep ingress

# Enable if not active
minikube addons enable ingress

# Check ingress controller
minikube kubectl -- get pods -n ingress-nginx

# Verify /etc/hosts entries
cat /etc/hosts | grep -E "(fastapi-app|kibana).local"
```

#### 6. Port Forward Connection Refused
```bash
# Check if service exists and has endpoints
minikube kubectl -- get svc -n fastapi-microservice
minikube kubectl -- get endpoints -n fastapi-microservice

# Ensure pods are ready
minikube kubectl -- get pods -n fastapi-microservice

# Try different port or restart port-forward
pkill -f "kubectl.*port-forward"
minikube kubectl -- port-forward -n fastapi-microservice svc/fastapi-app 8001:8000
```

#### 7. High Resource Usage
```bash
# Check resource usage
minikube kubectl -- top nodes
minikube kubectl -- top pods -n fastapi-microservice

# Reduce resource requests in manifests if needed
# Scale down replicas temporarily
minikube kubectl -- scale deployment fastapi-app --replicas=1 -n fastapi-microservice
```

### Resource Monitoring

```bash
# Monitor cluster resources
watch "minikube kubectl -- get pods -n fastapi-microservice"

# Check node resource usage
minikube kubectl -- describe node minikube

# Monitor application metrics (if metrics-server is enabled)
minikube kubectl -- top pods -n fastapi-microservice --containers
```

### Logs and Debugging

```bash
# Comprehensive logging
minikube kubectl -- logs --previous deployment/fastapi-app -n fastapi-microservice
minikube kubectl -- describe pod <pod-name> -n fastapi-microservice

# Event monitoring
minikube kubectl -- get events -n fastapi-microservice --sort-by='.firstTimestamp'

# Debug connectivity
minikube kubectl -- exec -it deployment/fastapi-app -n fastapi-microservice -- sh
# Inside container:
# curl elasticsearch:9200/_cluster/health
# nslookup elasticsearch
```

## 🧹 Cleanup

### Remove Application
```bash
# Delete namespace (removes all resources)
minikube kubectl -- delete namespace fastapi-microservice
```

### Stop Minikube
```bash
# Stop cluster (keeps configuration)
minikube stop

# Delete cluster completely
minikube delete

# Clean up Docker images
docker rmi fastapi-base-service:latest
```

## 📈 Scaling and Production Considerations

### Horizontal Scaling
```bash
# Scale FastAPI application
minikube kubectl -- scale deployment fastapi-app --replicas=5 -n fastapi-microservice

# Scale Elasticsearch (for production)
minikube kubectl -- scale deployment elasticsearch --replicas=3 -n fastapi-microservice
```

### Production Readiness Checklist
- [ ] Enable Elasticsearch security and authentication
- [ ] Configure proper resource limits and requests
- [ ] Set up persistent volume storage for Elasticsearch data
- [ ] Configure ingress with TLS certificates
- [ ] Implement proper log retention policies
- [ ] Set up monitoring and alerting
- [ ] Configure network policies for security
- [ ] Enable RBAC and service accounts

### Persistent Storage
```yaml
# For production, use proper StorageClass
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: elasticsearch-pvc
spec:
  storageClassName: "fast-ssd"  # Use appropriate storage class
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
```

## 🔗 Additional Resources

- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Elasticsearch on Kubernetes](https://www.elastic.co/guide/en/cloud-on-k8s/current/index.html)
- [OpenTelemetry Kubernetes](https://opentelemetry.io/docs/kubernetes/)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)

## 🆘 Getting Help

If you encounter issues not covered in this guide:

1. Check the [project's main README](../README.md) for general setup
2. Review Minikube logs: `minikube logs`
3. Check Kubernetes events: `minikube kubectl -- get events --all-namespaces`
4. Verify system resources: `free -h` and `df -h`
5. Consult the troubleshooting section above

For additional help, ensure your environment meets the minimum requirements and follow the step-by-step deployment process.
