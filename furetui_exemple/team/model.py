"""demo Example model, this model is goging to create table at startup
"""
from anyblok import Declarations
from anyblok.column import Integer, String, Boolean
from anyblok_pyramid_rest_api.adapter import Adapter


Model = Declarations.Model


@Declarations.register(Model)
class Team():

    class FuretUIAdapter(Adapter):

        @Adapter.tag('active')
        def tag_is_active(self, querystring, query):
            query = query.filter(self.Model.active.is_(True))
            return query

    id = Integer(primary_key=True)
    first_name = String(nullable=False)
    last_name = String(nullable=False)
    active = Boolean(default=True)
