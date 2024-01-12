#!/usr/bin/env bash

apt-get -y update
apt-get install -y nginx
 
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "Hello, world!" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

echo '
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://www.youtube.com;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
' > /etc/nginx/sites-available/default
service nginx restart
