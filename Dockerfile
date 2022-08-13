FROM node:alpine

# Install dependencies
RUN apk update && apk upgrade && apk add --no-cache bash git openssh \
    && rm -rf /var/cache/apk/*

RUN npm install -g gitbook-cli

RUN mkdir /gitbook
WORKDIR /gitbook
RUN git clone https://github.com/mdmcoin/mdmcoin-documentation.git
WORKDIR waves-documentation
RUN gitbook install

EXPOSE 4000

ENTRYPOINT gitbook serve --timing && cat index.html > _book/index.html
# CMD ["gitbook", "serve", "--timing"]


# serve
# docker run -d -p 4000:4000
