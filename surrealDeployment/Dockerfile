# ADDED: Use a temporary Alpine stage to create the /data directory with correct permissions for Fly.io volume mounting
FROM alpine:latest as setup

# ADDED: Create /data and set ownership to the SurrealDB user (65532)
RUN mkdir -p /data && chown -R 65532:65532 /data

# ADDED: Use the official SurrealDB image
FROM surrealdb/surrealdb:latest

# ADDED: Copy the /data directory from the setup stage to ensure correct permissions
COPY --from=setup /data /data/  # ADDED: Ensures /data exists and is owned by the right user for Fly.io volume

EXPOSE 8080

# ADDED: Start SurrealDB, using the /data directory for persistent storage
CMD ["start", "--bind", "0.0.0.0:8080", "file://data/srdb.db"]