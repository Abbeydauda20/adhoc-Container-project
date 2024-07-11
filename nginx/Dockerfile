#FROM nginx:alpine

#COPY nginx.conf /etc/nginx/nginx.conf

#EXPOSE 80 443

#CMD ["nginx", "-g", "daemon off;"]

##################################################################################

FROM nginx:alpine

# Copy custom nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy SSL certificates
COPY files/localhost.crt /etc/nginx/ssl/localhost.crt
COPY files/localhost.key /etc/nginx/ssl/localhost.key

# Expose ports
EXPOSE 80 443








