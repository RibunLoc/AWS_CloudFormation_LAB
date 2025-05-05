# source: 
import boto3
import yaml
import sys

# Kết nối client CloudFormation AWS
cf_client = boto3.client('cloudformation')

def validate_template(file_path):
    try:
        with open(file_path, 'r') as file:
            template_body = file.read()

        # Kiểm tra cú pháp CloudFormation template
        response = cf_client.validate_template(TemplateBody=template_body)

        print(f"\n[✔️] Template '{file_path}' passed syntax validation.")
        print("\nTemplate Parameters:")
        for param in response.get('Parameters', []):
            default = param.get('DefaultValue', 'No default')
            print(f"  - {param['ParameterKey']} (Default: {default})")

        return yaml.safe_load(template_body)

    except Exception as e:
        print(f"\n[❌] Template '{file_path}' failed validation:")
        print(str(e))
        sys.exit(1)

def check_resource_links(template):
    resources = template.get('Resources', {})
    if not resources:
        print("\n[❌] No resources found in template.")
        sys.exit(1)

    print("\nChecking resource links:")
    for name, resource in resources.items():
        res_type = resource.get('Type', 'Unknown')
        props = resource.get('Properties', {})
        if 'VpcId' in props:
            vpc_ref = props['VpcId']
            print(f"  - Resource '{name}' ({res_type}) linked to VPC: {vpc_ref}")
        if 'SubnetId' in props:
            subnet_ref = props['SubnetId']
            print(f"  - Resource '{name}' ({res_type}) linked to Subnet: {subnet_ref}")
        if 'RouteTableId' in props:
            rt_ref = props['RouteTableId']
            print(f"  - Resource '{name}' ({res_type}) linked to Route Table: {rt_ref}")
        
def check_parameters(template):
    params = template.get('Parameters', {})
    if not params:
        print("\n[❌] No parameters defined in template.")
        sys.exit(1)

    print("\nChecking template parameters:")
    for param_name, param_data in params.items():
        param_type = param_data.get('Type', 'Undefined')
        default_val = param_data.get('Default', 'No default value')
        print(f"  - Parameter '{param_name}': Type={param_type}, Default={default_val}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python validate_template.py <path_to_template.yaml>")
        sys.exit(1)

    template_file = sys.argv[1]
    template = validate_template(template_file)
    check_parameters(template)
    check_resource_links(template)
