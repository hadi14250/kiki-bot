#!/bin/bash

export CR_PAT=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
echo $CR_PAT | docker login ghcr.io -u scomcoin --password-stdin
docker compose -f docker-compose-dev.yml up
docker logout
docker compose -f docker-compose-dev.yml down
