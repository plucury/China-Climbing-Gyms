from jsonschema import validate as json_validate
import yaml
import os

def cli():
    with open('schema.yaml') as f:
        schema = yaml.safe_load(f)
        for p, _, gyms in os.walk('gyms'):
            for gym in gyms:
                with open(os.path.join(p, gym)) as g:
                    data = yaml.safe_load(g)
                    try:
                        json_validate(data, schema)
                    except Exception as e:
                        print(f'Error validating {gym}: {e}')
                    else:
                        print(f'Validated {gym} successfully')

if __name__ == '__main__':
    cli()