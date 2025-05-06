FROM python:3.13.2-alpine3.21
RUN addgroup react && adduser -S -G react react
USER react
WORKDIR /app/
RUN mkdir datos
COPY --chown=react package*.json .
RUN npm install
COPY --chown=react . .
ENV API=https:api.tecnm.mx/alumnos
EXPOSE 5173
CMD ["npm", "run", "dev"]