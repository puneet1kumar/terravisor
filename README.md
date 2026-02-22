![Journey Orchestration and Choreography with Camunda 8 - visual selection (3)](https://github.com/user-attachments/assets/ed0106d5-e56a-4929-8f8a-9f9c74981a1f)

FROM
exus3.systems .uk.habc:18096/com/hsbc/group/itid/es/mw/nginx/ubuntunginx-v114:latest

LABEL DemoBy="Fraveen13 Kumar"

USER root

4 Remove the default Nginx configuration file
RUN rm -v /etc/nqinx/ncinx.conf

t Copy a configuration file from the current directory
ADD nainx.conf /etc/nainx/

ADD web /usr/share/nainx/html/
ADD web /var/www/html/

t Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /eta/nginx/nginx.conf

I Expose ports
ExPOSE 90

Set the default command to execute
t when creating a new container
CMD service nainx start

worker procesaes I7
ivents [ worker connections 1024; 1
http include sendfile oni Berver root index server listen 90:
mime.types;
lusr/share/nainx/htu1/: index.html: name localhost;
