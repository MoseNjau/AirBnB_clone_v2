#!/usr/bin/env bash

# Update package lists and upgrade installed packages
sudo apt-get update
sudo apt-get upgrade -y

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get install nginx -y
fi

# Create required directories if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a test HTML file
echo "<html><head></head><body>This is a test</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or update symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo tee -a /etc/nginx/sites-available/default > /dev/null <<EOF
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
EOF

# Restart Nginx to apply changes
sudo service nginx restart

# Exit successfully
exit 0
