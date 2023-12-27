#!/bin/bash

export CR_PAT=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
echo $CR_PAT | docker login ghcr.io -u scomcoin --password-stdin
docker compose -f docker-compose-dev.yml up
docker logout
docker compose -f docker-compose-dev.yml down
