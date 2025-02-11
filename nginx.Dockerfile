FROM nginx:1-alpine

RUN apk add --no-cache gettext


RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled 
COPY nginx.conf /etc/nginx/conf.d
