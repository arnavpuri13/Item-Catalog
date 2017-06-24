"""It includes endpoints for getting catalog data in JSON format, and Atom feeds."""

from flask import abort
from flask import Blueprint
from sqlalchemy.orm.exc import NoResultFound
from catalog import db
from catalog.models import User, Category, Item
from auth import login_required

data = Blueprint('data', __name__)


from flask import jsonify

@data.route('/catalog.json')
def view_catalog_json():
    """Catalog."""
    categories = db.query(Category).all()
    items = db.query(Item).all()
    return jsonify(categories = [c.serialize for c in categories],
        items = [i.serialize for i in items])

@data.route("/catalog/category-<int:category_id>.json")
def view_category_json(category_id):
    """Category."""
    try:
        category = db.query(Category).filter_by(id = category_id).one()
    except NoResultFound:
        abort(404)
    items = db.query(Item).filter_by(category_id = category.id).all()
    return jsonify(category = category.serialize,
        items = [i.serialize for i in items])

@data.route("/catalog/item-<int:item_id>.json")
def view_item_json(item_id):
    """Item."""
    try:
        item = db.query(Item).filter_by(id = item_id).one()
    except NoResultFound:
        abort(404)
    return jsonify(item = item.serialize)

@data.route('/users.json')
@login_required
def users_json():
    """List of users."""
    users = db.query(User).all()
    return jsonify(users = [u.serialize for u in users])


from urlparse import urljoin
from flask import request
from flask import url_for
from werkzeug.contrib.atom import AtomFeed

ATOM_FEED_SIZE = 5

def make_external(url):
    """Convert relative URL into absolute URL."""
    return urljoin(request.url_root, url)

@data.route('/recent.atom')
def recent_atom_feed():
    """Atom feed with recently created and updated items."""
    feed = AtomFeed('Latest Items', 
        feed_url = request.url, url = request.url_root)
    items = db.query(Item).order_by(Item.updated.desc()).limit(ATOM_FEED_SIZE).all()
    for item in items:
        item_url = url_for('api.view_item', item_id = item.id)
        feed.add(title = item.name,
                 content = unicode(item.name + " (" + item.category.name + "): " + item.description),
                 content_type = 'text',
                 author = item.user.name,
                 url = make_external(item_url),
                 updated = item.updated,
                 published = item.created)
    return feed.get_response()
