import logging
import os

from boto3.session import Session

class Utils:
    @staticmethod
    def get_url(parameter_name: str) -> str:
        try:
            session = Session()
            client = session.client(service_name='ssm', region_name=os.getenv('REGION'))
            resp = client.get_parameter(Name=parameter_name, WithDecryption=True)
            return resp['Parameter']['Value']
        except Exception as e:
            message = f'Failed to get secret from AWS SSM: {str(e)}'
            logging.error(message)
