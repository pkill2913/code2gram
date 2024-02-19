#!/bin/bash

cd ./examples/ && terraform init

cd ../examples/ && terraform plan -out=tfplan.binary

# cd ../examples/ &&  docker run --rm -it hashicorp/terraform:latest plan -out=tfplan.binary

cd ../examples/ && terraform show -json tfplan.binary > tfplan.json