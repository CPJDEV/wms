from app import db
from models import Bin

from sqlalchemy.exc import InvalidRequestError, IntegrityError, SQLAlchemyError


class Dot_(dict):
     # Usage: arr = Map(dict)
     # keyvalue = arr.key
    def __init__(self, *args, **kwargs):
        super(Dot_, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Dot_, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Dot_, self).__delitem__(key)
        del self.__dict__[key]


def db_bulk_insert(db_obj):
    error = None
    return_obj = 0
    if len(db_obj) > 0:
        db_sess = db.session

        try:
            db_sess.bulk_save_objects(db_obj, return_defaults=True)
            for obj_ in db_obj:
                assert obj_.id is not None
            
            db_sess.commit()
        except (SQLAlchemyError, IntegrityError), e:
            db_sess.rollback()
            db_sess.flush() # for resetting non-commited .add()
            error = e

        if error:
            return_obj = "%s"%error
        
    else:
        return_obj = "No entry to process!"

    return return_obj

def addMultiBins(form):
    bins_ , abins = [],[]
    bins = form.name.data.split(",")
    error = 0
    if bins:
        for bin_ in bins:
            bin_exist = Bin.query.filter_by(name=bin_).first()
            if not bin_exist:
                abin = Bin(name=bin_.upper(),depth=form.depth.data,warehouse_id=form.warehouse.data,aisle_id=form.aisle.data)
                if bin_.upper() not in abins:
                    abins.append(bin_.upper())
                    bins_.append(abin)

        error = db_bulk_insert(bins_)


    return error