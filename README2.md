# I build a Docker file for Nginx image with Alpine to make it lightweiaght
# I used a Docker_compose file for multi-container application, this allows me to incorporate all the essential components of the containerized application in a single file which is in line with best practices.
# I generated the ssl private key with the following command: "openssl genpkey -algorithm RSA -out nginx.key -pkeyopt rsa_keygen_bits:2048"
# I generate the ssl crt with the following command: openssl x509 -req -days 365 -in nginx.csr -signkey nginx.key -out nginx.crt
# these commands are passed in the Dockerfile
# Docker_compose file, Dockerfile, application code nginx.config file must all be in the same root directory so te code does not break



