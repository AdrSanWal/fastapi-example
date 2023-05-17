FROM node:20

WORKDIR /app

COPY package*.json ./

# Probar a grabar versión especifica con: RUN apt-get install npm=4.0.0-1chl1~precise1
RUN npm install

EXPOSE 5173

CMD ["npm", "run", "dev"]
