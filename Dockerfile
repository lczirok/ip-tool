# Stage 1
FROM bitnami/kubectl:latest AS extractor
# Install jq for JSON processing
RUN apt-get update && apt-get install -y jq && rm -rf /var/lib/apt/lists/*  
# Extract Pod IPs and store them in ipcsv.csv
CMD ["sh", "-c", "kubectl get pod -A -o json | jq -r '.items[].status.podIP' | tee /data/ipcsv.csv"]

# Stage 2
FROM python:latest AS processor

WORKDIR /app

COPY ip-tool.py .

# Copy extracted IPs from previous stage
COPY --from=extractor /data/ipcsv.csv /app/ipcsv.csv

# For future usecases : RUN pip install -r requirements.txt || true

CMD ["python", "ip-tool.py"]