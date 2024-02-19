# code2gram

Python application created for diagram code from Terraform.

To use, initialize the virtual env  executing:

``` $ python3 -m venv .venv ```

``` source .venv/bin/activate```


``` pip install -r requirements ```


To execute run: 

``` python main.py ```

Error:

make sure the Graphviz executables are on your systems' PATH


Linux Ubuntu/Debian

sudo apt-get install graphviz


macOS

brew install graphviz

-------------


pip install python-hcl2


terraform plan -out=tfplan.binary

terraform show -json tfplan.binary > tfplan.json
jq . tfplan.json
