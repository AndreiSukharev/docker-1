FROM node:8
WORKDIR /usr/src/app

COPY package*.json ./

RUN yarn install

COPY . .

EXPOSE 8080
CMD [ "yarn", "start" ]

# docker build -t nodejs .
# docker run --rm -it -p 8080:8080 nodejs
