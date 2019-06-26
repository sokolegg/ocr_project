# NVIDIA GPU LINK BUILD
# LOOK ANOTHER OPTIONS https://hub.docker.com/r/nvidia/cuda/
# FOR GPU USE:  
# FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

# OR JUST UBUNTU
FROM ubuntu:18.04

# ANACONDA BUILD
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean
COPY \environment.yml ~\environment.yml
RUN cd ~
RUN conda env create -f ~\environment.yml


ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash", "-c", "source activate ocr_env && cd ~ && jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root"]
