#!/bin/bash

docker build -t w-amp .
docker run --rm -it --entrypoint=bash --name=w-amp-test w-amp