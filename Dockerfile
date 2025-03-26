# Dockerfile-client

FROM node:16

WORKDIR /app

# Copy only the package files first for caching
COPY client/package.json client/package-lock.json /app/

# Install dependencies
RUN npm install

# Copy the rest of the client code
COPY . /app/

# Expose the default React dev server port
EXPOSE 3000

# Start the development server
CMD ["npm", "start"]
