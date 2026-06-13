'''источник: /https://docs.docker.com/build/building/variables/ '''

FROM node:20-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY report.js .

CMD ["node", "report.js"]
