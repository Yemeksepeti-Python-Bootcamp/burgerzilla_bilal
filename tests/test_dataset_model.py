from app import db
from app.models.dataset import Dataset
from app.models.schemas import DatasetSchema

from tests.utils.base import BaseTestCase

class TestDatasetModel(BaseTestCase):
    def test_create_dataset(self):
        d = Dataset(name='test1',userid=1,filename='test1.csv',filepath='/test/test1.csv')
        db.session.add(d)
        db.session.commit()
        self.assertTrue(d.id > 0)

    def test_update_dataset(self):
        d = Dataset(name='test2',userid=1,filename='test2.csv',filepath='/test/test2.csv')
        db.session.add(d)
        db.session.commit()
        d.name = 'test4'
        db.session.commit()
        self.assertTrue(d.name == 'test4')

    def test_delete_dataset(self):
        d = Dataset(name='test3',userid=1,filename='test3.csv',filepath='/test3/test2.csv')
        db.session.add(d)
        db.session.commit()
        db.session.delete(d)
        db.session.commit()
        res =  Dataset.query.get(d.id)
        self.assertTrue(res is None)

    def test_schema(self):
        # d = Dataset(user_id=1)
        d = Dataset(name='test5',userid=1,filename='test5.csv',filepath='/test5/test5.csv')
        d_dump = DatasetSchema().dump(d)
        self.assertTrue(d_dump['name'] == 'test5')
    
