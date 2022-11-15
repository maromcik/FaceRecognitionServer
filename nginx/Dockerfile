# the commands for creating a certificate are taken
# over from https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-16-04
FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -subj "/C=SK/ST=./L=./O=./OU=./CN=."
RUN openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
COPY nginx.conf /etc/nginx/conf.d