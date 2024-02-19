from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
import subprocess

import json

title = "EXAMPLE"
vpc_id = "default"
tf_json_file = "./examples/tfplan.json"

def get_data_plan():
    with open('examples/tfplan.json', 'r') as file:
        plan_data = json.load(file)
    return plan_data

def get_region(tfstate_path):
    with open(tfstate_path, 'r') as file:
        tfstate_data = json.load(file)
    region = tfstate_data.get('configuration').get('provider_config').get('aws').get('expressions').get('region').get('constant_value')
    return region

def get_instances(resources):
    ec2 = resources.get()

    

def listar_recursos(tfstate_path):
    with open(tfstate_path, 'r') as file:
        tfstate_data = json.load(file)

    resources = tfstate_data.get('planned_values').get('root_module').get('resources')
    recursos = []

    for resource in resources:
        recursos.append(resource)
   
    return recursos

# resources = get_region(elementos)

def generar_codigo_diagrama(elementos, archivo_salida):

    indentacion = 4 

    with open(archivo_salida, 'w') as archivo:
        archivo.write("from diagrams import Diagram, Cluster\n")
        archivo.write("from diagrams.aws.compute import EC2\n\n")
        archivo.write("with Diagram(\"Diagrama de Elementos\", show=True):\n")

        archivo.write(f"{(indentacion * ' ')}with Cluster(\"Region {region}\" ): \n")

        if vpc_id == 'default':
            archivo.write(f"{(indentacion + 4) * ' '}with Cluster(\"VPC Default\"):\n")
        else:
            archivo.write(f"{(indentacion + 4) * ' '}with Cluster(\"VPC tal y tal\"):\n")
        for elemento in elementos:
            print(elemento)
            print("##########")
            name = elemento['name']
            for clave, valor in elemento.items():
                 # Define el nivel de indentación deseado
                if clave == 'type':
                    if valor == 'aws_instance':
                        archivo.write(f"{(indentacion + 8) * ' '}with Cluster(\"Cluster {title}\"):\n")
                        archivo.write(f"{(indentacion + 16) * ' '}EC2(\"{name}\")\n")

# # Nombre del archivo de salida
archivo_salida = "diagrama_generado.py"

print("Run")
subprocess.run(["ls","-ls"])
subprocess.run(["sh","-c","./bash_scripts/tf_steps.sh"])



# # Generar el código del diagrama y guardar en el archivo
region = get_region(tf_json_file)
elementos = listar_recursos(tf_json_file)
generar_codigo_diagrama(elementos, archivo_salida)

subprocess.run(["python", "diagrama_generado.py"])
