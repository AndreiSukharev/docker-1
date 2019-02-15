FROM ubuntu
RUN apt-get update && apt-get upgrade -y && apt-get install -y gcc
COPY . /usr/c_proj
WORKDIR /usr/c_proj
RUN gcc -o hello main.c
CMD ["./hello"]


# docker build -t proj_c .
# docker run -it --rm proj_c
