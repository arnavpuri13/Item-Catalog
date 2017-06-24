"""Creates Database"""


from catalog import engine
from catalog.models import Base

Base.metadata.create_all(engine)
