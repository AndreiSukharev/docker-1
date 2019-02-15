FROM debian
RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install bzip2 wget -y &&\
    wget http://dl.4players.de/ts/releases/3.0.13.8/teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2 &&\
    tar -xvf teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2
WORKDIR teamspeak3-server_linux_amd64

EXPOSE 9987/udp 10011 30033
CMD ["sh", "ts3server_minimal_runscript.sh"]

#docker build -t ex01 .
#docker run -it --rm -p=9987:9987/udp  -p=10011:10011 -p=30033:30033 ex01
