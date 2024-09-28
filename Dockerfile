FROM golang:1.21.6-alpine
WORKDIR /app
COPY . .
RUN go build -o server server.go
RUN chmod +x server
EXPOSE 8080
CMD [ "/app/server" ]