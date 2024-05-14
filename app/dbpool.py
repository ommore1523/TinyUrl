from app import models
import datetime
import traceback
import sqlalchemy as sqa
from sqlalchemy.orm import Session


class DB:
    def get_tiny_url(self, long_url):
        try:
            pg_session = Session(models.engine)
            
            pg_records = pg_session.query(models.TinyUrl).filter(models.TinyUrl.long_url == long_url).all()

            if len(pg_records) == 0:
                return {'success':False, 'message':'No Tiny Url Found'}
            
            pg_session.close()
                
            return {'success':True, 'message':pg_records.short_url}
        except Exception as err:
            return {'success':False, 'message':f'Error: {str(traceback.format_exc())}'}

    def get_long_url(self, short_code):
        try:
            pg_session = Session(models.engine)
            pg_records = pg_session.query(models.TinyUrl).filter(models.TinyUrl.short_url == short_code).all()

            if len(pg_records) == 0:
                return {'success':False, 'message':'No Tiny Url Found'}
            pg_session.close()
                
            return {'success':True, 'message':pg_records[0].long_url}
        except Exception as err:
            return {'success':False, 'message':f'Error: {str(traceback.format_exc())}'}


    

    def save_tiny_url(self, **kwargs):
        try:
            pg_session = Session(models.engine)
            pg_acc = models.TinyUrl(
                long_url = kwargs['long_url'],
                short_url = kwargs['short_url'],
                created_date = datetime.datetime.now()

            )
            pg_session.add(pg_acc)
            pg_session.flush()
            pg_session.refresh(pg_acc)
            pg_session.commit()
            pg_session.close()
            return {'success':True, 'message':f'Success'}
        except Exception as err:
            return {'success':False, 'message':f'Error: {str(traceback.format_exc())}'}