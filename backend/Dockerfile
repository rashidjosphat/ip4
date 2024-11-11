FROM node:18-alpine

WORKDIR /app1

COPY ./package*.json ./

RUN npm install --omit=dev

COPY . .

EXPOSE 5000

CMD [ "node", "server.js" ]