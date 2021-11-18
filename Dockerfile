FROM rust:1.56-buster
USER root
RUN apt-get update && apt-get install -y bash curl coreutils libc-dev libssl-dev openssl
RUN cargo install --git https://github.com/jdr0887/immunespace-to-cellfie-mapper.git
CMD [ "/bin/bash" ]
ENTRYPOINT ["immunespace-to-cellfie-mapper"]