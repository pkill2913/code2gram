#!/bin/bash

cd examples/

terraform plan -out=tfplan.binary

terraform show -json tfplan.binary > tfplan.json