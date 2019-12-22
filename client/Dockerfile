FROM node:13-slim

RUN mkdir -p /opt/services/client
COPY . /opt/services/client/

WORKDIR /opt/services/client
RUN npm install && npm run build && npm install -g serve

EXPOSE 3000

CMD [ "serve", "-l", "3000", "-s", "build" ]
