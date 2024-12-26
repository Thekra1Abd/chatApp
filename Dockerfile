FROM nginx:latest

# Copy static files into Nginx directory
COPY public/ /usr/share/nginx/html

# Expose port 8080 for the application
EXPOSE 8080

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]

# Add a health check to monitor the application
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 CMD curl -f http://localhost:80 || exit 1
