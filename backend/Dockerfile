FROM node:14-alpine as build

WORKDIR /app1

COPY ./package*.json .

RUN npm i

COPY . .

CMD [ "node" , "server.js"]

## the running stage 

