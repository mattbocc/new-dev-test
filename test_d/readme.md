# Part D: CloudOps Question - Moving to GCP steps

1. Cloud Run: Deploy the containerized pipeline as a job
2. Cloud Storage: Store input/output data in buckets
3. Cloud Build: Auto-build Docker images from Git commits

## Workflow

GitHub => Cloud Build => Container Registry => Cloud Run Jobs

(Having Cloud Storage as data in/out)

## What we will have at the end
- Serverless (no infrastructure management)
- Pay per execution
- Auto scaling
- Built-in logging and monitoring

Cloud Run Jobs with Cloud Storage is the sweet spot for small to medium pipelines