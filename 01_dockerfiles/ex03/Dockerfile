from debian

RUN apt-get update && apt-get upgrade
RUN apt-get install -y openssh-server ca-certificates postfix wget curl
RUN curl -LO https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh
RUN bash script.deb.sh
RUN apt-get update && EXTERNAL_URL="http://gitlab.example.com" && /
    apt-get install -yq gitlab-ce
# https://gitlab.com/gitlab-org/omnibus-gitlab/issues/2229
RUN apt update && apt install -y tzdata && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 443 80 22
ENTRYPOINT (/opt/gitlab/embedded/bin/runsvdir-start &) && gitlab-ctl reconfigure && tail -f /dev/null


#docker build -t ex03 .
#docker run -it --rm -p 8080:80 -p 8022:22 -p 8443:443 --privileged ex03
