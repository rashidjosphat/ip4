# Build stage
FROM node:13.12.0 as build

WORKDIR /app1

COPY ./package*.json ./

RUN npm install --omit=dev

COPY . .

# Running stage
FROM alpine:latest

# Install Node.js and npm from Alpine community repository
RUN apk add --no-cache nodejs npm

WORKDIR /app2

# Copy built application and node_modules from the build stage
COPY --from=build /app1 ./

ENV HOST=0.0.0.0

EXPOSE 3000

CMD ["npm", "start"]

HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:3000 || exit 1
