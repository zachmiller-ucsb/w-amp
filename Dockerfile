FROM ubuntu:22.04

RUN apt-get update \
  && apt-get install -y \
    git \
    build-essential \
    libgflags-dev \
    zlib1g \
    bzip2 \
    liblz4-dev \
    libsnappy-dev \
    zstd \
  && apt-get -y upgrade

RUN git clone https://github.com/zachmiller-ucsb/w-amp.git ~/w-amp \
  && cd ~/w-amp \
  && git switch rocksdb \
  && DEBUG_LEVEL=0 DISABLE_WARNING_AS_ERROR=1 make -j$(nproc) db_bench