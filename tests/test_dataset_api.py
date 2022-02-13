import json
from pkgutil import get_data
from re import A

from flask_jwt_extended import create_access_token

from app import db
from app.models.dataset import Dataset

from utils.base import BaseTestCase

def get_dataset_data(self,accestoken,dataset_id):
    return self.client.get(
        f"/api/datasets/{dataset_id}",
        headers={"Authorization": "Bearer " + accestoken},
    )

def get_datasets_data(self,accestoken):
    return self.client.get(
        f"/api/datasets",
        headers={"Authorization": "Bearer " + accestoken},
    )

def post_dataset_data(self,accestoken,dataset_data,user_id):
    return self.client.post(
        f"/api/datasets/user/{user_id}",
        data=json.dumps(dataset_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accestoken},
    )

def put_dataset_data(self,accesstoken,dataset_data,dataset_id,user_id):
    return self.client.put(
        f"/api/datasets/{dataset_id}/user/{user_id}",
        data=json.dumps(dataset_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def delete_dataset_data(self,accesstoken,dataset_id):
    return self.client.delete(
        f"/api/datasets/{dataset_id}",
        headers={"Authorization": "Bearer " + accesstoken},
    )

class TestDatasetBlueprint(BaseTestCase):
    def test_dataset_get(self):
        """
        Test for getting a dataset
        """
        d = Dataset(name='test1',userid=1,filename='test1.csv',filepath='/test/test1.csv')
        db.session.add(d)
        db.session.commit()
        
        access_token = create_access_token(identity=1)

        dataset_resp = get_dataset_data(self,access_token,d.id)
        dataset_data = json.loads(dataset_resp.data.decode())

        self.assertTrue(dataset_resp.status_code == 200)
        self.assertTrue(dataset_data["dataset"]['name'] == 'test1')
        self.assertTrue(dataset_data["dataset"]['userid'] == 1)
        self.assertTrue(dataset_data["dataset"]['filename'] == 'test1.csv')
        self.assertTrue(dataset_data["dataset"]['filepath'] == '/test/test1.csv')

        data_404_resp = get_dataset_data(self,access_token,100)
        self.assertEquals(data_404_resp.status_code, 400)
