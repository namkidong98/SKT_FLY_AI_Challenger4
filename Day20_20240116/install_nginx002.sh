#!/bin/bash

#  ⑦궎吏   뚯뒪  낅뜲 댄듃
apt-get -y update

# nginx  ㅼ튂
apt-get -y install nginx

# index.html 留뚮뱾湲 
fileName=/var/www/html/index.html
echo "<html><head><title>Load Balancer</title></head><body>Running Web Server from vmeastback02</body></html>" > ${fileName}