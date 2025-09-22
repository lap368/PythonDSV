# Virtuoso Docker Setup

This directory contains the Docker Compose configuration for running Virtuoso locally for development.

## Quick Start

1. **Start Virtuoso**:
   ```bash
   cd docker/virtuoso
   docker-compose up -d
   ```

2. **Check if it's running**:
   ```bash
   docker-compose ps
   ```

3. **View logs**:
   ```bash
   docker-compose logs -f
   ```

4. **Stop Virtuoso**:
   ```bash
   docker-compose down
   ```

## Accessing Virtuoso

- **SPARQL Endpoint**: http://localhost:8890/sparql
- **Conductor (Web Interface)**: http://localhost:8890/conductor
- **Default credentials**: username `dba`, password `dba`

## Data Management

### TTL Files
TTL files in `../../data/ttl/` are mounted to `/ttl` inside the container.

### Loading TTL Data
You can load TTL files using SPARQL UPDATE queries:
```sparql
LOAD <file:///ttl/sample/products.ttl>
```

Or into a specific graph:
```sparql
LOAD <file:///ttl/sample/products.ttl> INTO GRAPH <http://example.com/products>
```

## Data Persistence

- **Database files**: `../../data/virtuoso/database/`
- **Dumps**: `../../data/virtuoso/dumps/`
- **Logs**: `../../data/virtuoso/logs/`

## Configuration

The `virtuoso.ini` file contains the Virtuoso configuration. Key settings:
- SPARQL endpoint enabled on port 8890
- File system access allowed for `/ttl` directory
- Default graph: `http://localhost:8890/DAV`

## Health Check

The container includes a health check that verifies the SPARQL endpoint is responding.
Check status with:
```bash
docker-compose ps
```

## Troubleshooting

If Virtuoso fails to start:
1. Check logs: `docker-compose logs`
2. Ensure ports 1111 and 8890 are not in use
3. Check disk space in the data directory
4. Try removing the container and recreating: `docker-compose down && docker-compose up -d`
