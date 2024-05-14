from app import models
import datetime
import traceback
import sqlalchemy as sqa
from sqlalchemy.orm import Session


class DB:
    def get_tiny_url(self, long_url):
        try:
            with Session(models.engine) as pg_session:
                stmp = sqa.select(models.TinyUrl).where(
                    models.TinyUrl.long_url == long_url
                )
                pg_records = pg_session.execute(stmp).all()

                if len(pg_records) == 0:
                    return {'success':False, 'message':'No Tiny Url Found'}
                
            return {'success':True, 'message':pg_records.short_url}
        except Exception as err:
            return {'success':False, 'message':f'Error: {str(traceback.format_exc())}'}

    def get_long_url(self, short_url):
        try:
            with Session(models.engine) as pg_session:
                stmp = sqa.select(models.TinyUrl).where(
                    models.TinyUrl.long_url == short_url
                )
                pg_records = pg_session.execute(stmp).all()

                if len(pg_records) == 0:
                    return {'success':False, 'message':'No Tiny Url Found'}
                
            return {'success':True, 'message':pg_records.long_url}
        except Exception as err:
            return {'success':False, 'message':f'Error: {str(traceback.format_exc())}'}


    

    def save_tiny_url(self, **kwargs):
        try:
            with Session(models.engine) as pg_session:
                pg_acc = models.TinyUrl(
                    long_url = kwargs['long_url'],
                    short_url = kwargs['short_url'],
                    created_date = datetime.utcnow

                )
                pg_session.add(pg_acc)
                pg_session.flush()
                pg_session.refresh(pg_acc)
                pg_session.commit()
        except Exception as err:
            return {'success':False, 'message':f'Error: {str(traceback.format_exc())}'}