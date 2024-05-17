#For nodejs image.
FROM node:14
#Container icinde /app dizini olustur.
WORKDIR /app
#Package json icindeki npm bagimliliklarini yükle.
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]