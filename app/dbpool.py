from app import models
import datetime
import sqlalchemy as sqa
from sqlalchemy.orm import Session


class DB:
    def get_tiny_url(self, long_url):
        with Session(models.engine) as pg_session:
            stmp = sqa.select(models.TinyUrl).where(
                models.TinyUrl.long_url == long_url
            )
            pg_records = pg_session.execute(stmp).all()

            if len(pg_records) == 0:
                return {'success':False, 'message':'No Tiny Url Found'}
        return {'success':True, 'message':pg_records.short_url}

    def get_long_url(self, short_url):
        with Session(models.engine) as pg_session:
            stmp = sqa.select(models.TinyUrl).where(
                models.TinyUrl.long_url == short_url
            )
            pg_records = pg_session.execute(stmp).all()

            if len(pg_records) == 0:
                return {'success':False, 'message':'No Tiny Url Found'}
        return {'success':True, 'message':pg_records.long_url}


    def get_max_id(self, pg_session):

        max_meta_id = pg_session.execute(
            sqa.select(sqa.func.max(models.TinyUrl.id))
        ).scalar()

        if max_meta_id is None:
            max_meta_id = 1
        else:
            max_meta_id += 1

        return max_meta_id
    
    def save_tiny_url(self, **kwargs):
        with Session(models.engine) as pg_session:

            max_id = self.get_max_id(pg_session)

            pg_acc = models.TinyUrl(
                id = max_id,
                long_url = kwargs['long_url'],
                short_url = kwargs['short_url'],
                created_date = datetime.utcnow

            )

            pg_session.add(pg_acc)
            pg_session.flush()
            pg_session.refresh(pg_acc)
            pg_session.commit()