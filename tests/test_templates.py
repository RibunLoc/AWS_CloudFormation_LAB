import boto3
import os
import pytest

cf = boto3.client("cloudformation")
TEMPLATE_DIR = "./modules"

def list_template_files():
    return [os.path.join(TEMPLATE_DIR, f) for f in os.listdir(TEMPLATE_DIR) if f.endswith(".yaml")]

@pytest.mark.parametrize("template_path", list_template_files())
def test_template_validity(template_path):
    with open(template_path, "r") as f:
        template_body = f.read()

    try:
        cf.validate_template(TemplateBody=template_body)
        print(f"[PASS] {template_path} is valid.")
    except Exception as e:
        pytest.fail(f"[FAIL] {template_path} is invalid: {str(e)}")
