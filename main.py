

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

import json

title = "EXAMPLE"
vpc_id = "default"


def get_data_plan():
    with open('examples/tfplan.json', 'r') as file:
        plan_data = json.load(file)
    return plan_data

def get_region(resources):
    region = resources.get('configuration').get('provider_config').get('aws').get('expressions').get('region').get('constant_value')
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

elementos = listar_recursos('examples/tfplan.json')
# resources = get_region(elementos)


def generar_codigo_diagrama(elementos, archivo_salida):
    with open(archivo_salida, 'w') as archivo:
        archivo.write("from diagrams import Diagram, Cluster\n")
        archivo.write("from diagrams.aws.compute import EC2\n\n")
        archivo.write("with Diagram(\"Diagrama de Elementos\", show=True):\n")
        for elemento in elementos:
            print(elemento)
            print("##########")
            name = elemento['name']
            for clave, valor in elemento.items():
                indentacion = 4  # Define el nivel de indentación deseado
                if clave == 'type':
                    if valor == 'aws_instance':
                        archivo.write(f"{indentacion * ' '}with Cluster(\"Cluster {title}\"):\n")
                        archivo.write(f"{(indentacion + 4) * ' '}EC2(\"{name}\")\n")

# # Nombre del archivo de salida
archivo_salida = "diagrama_generado.py"

# # Generar el código del diagrama y guardar en el archivo
generar_codigo_diagrama(elementos, archivo_salida)

