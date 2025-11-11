import os
import boto3
from dotenv import load_dotenv

load_dotenv(dotenv_path="./secret_aws.env")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

class AwsDb:
    
    def __init__(self):
        self.db_instance_id = 'xguardian-dev-sp'
        self.rds = boto3.client(
            'rds',
            aws_access_key_id='AKIAYTCEOWO5YU73T5FG',
            aws_secret_access_key='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',
            region_name='sa-east-1',
        )

    def get_status(self):
        
        response = self.rds.describe_db_instances(DBInstanceIdentifier=self.db_instance_id)
        
        return response["DBInstances"][0]["DBInstanceStatus"]
    
    
    def alternar_estado(self):
     
        status = self.get_status()
        
        print('status', status)
        
        if status == "available":
            response = self.rds.stop_db_instance(DBInstanceIdentifier=self.db_instance_id)
            
            print(f"{self.db_instance_id} estava LIGADO. Desligando...")
            
            return "Desligando"
        
        elif status == "stopped":
            
            response = self.rds.start_db_instance(DBInstanceIdentifier=self.db_instance_id)
            
            print(f"{self.db_instance_id} estava DESLIGADO. Ligando...")
            
            return "Ligando"
        
        else:
            
            print(f"{self.db_instance_id} está no status: {status}. Aguarde.")
            
            return f"Aguardando: {status}"
