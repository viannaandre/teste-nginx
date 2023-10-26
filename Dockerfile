FROM nginx
COPY ./html /usr/share/nginx/html/
COPY ./app /app
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]