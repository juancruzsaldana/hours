FROM node:12 AS build

WORKDIR /app

ENV NODE_ENV production

COPY package*.json ./

RUN npm i 

COPY . ./

RUN npm install --dev && npm run build

FROM nginx:1.19-alpine
COPY --from=build /app/public /usr/share/nginx/html

