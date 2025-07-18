# okta_demo

## Build

```
PROJECT_ID=bmbl-infosec-dev
SERVICE_NAME=hello-okta

gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME
```

## Deploy a service

```
REGION=europe-west3

gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated
```
