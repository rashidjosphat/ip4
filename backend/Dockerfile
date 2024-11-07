# Use a specific version of Node.js as the base image
FROM node:18-alpine as build

# Set the working directory inside the container
WORKDIR /app  

# Copy the package.json and package-lock.json first to leverage Docker cache
COPY package*.json ./  

# Install the dependencies
RUN npm install

# Copy the rest of the application files into the container
COPY . .

# Expose port (optional) - this can be useful if you're running a web server
EXPOSE 5000  

# Define the command to run your app (assuming server.js is in the root)
CMD ["node", "server.js"]  
