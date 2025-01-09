"""Home route module"""
from web_flask.run import app
from flask import render_template, jsonify, flash
from models.user import User
from models.area import Area
from models.city import City
from models.amenity import Amenity
from models.property import Property
from models.region import Region
from models.image import Image
from flask import request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_login import login_required


login_manager = LoginManager()
login_manager.init_app(app)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.email != 'admin@email.com':
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



@app.route('/', strict_slashes=False)
def home():
    properties = Property.get_all()
    return render_template('home.html', properties=properties)

@app.route(
    '/login',
    strict_slashes=False,
    methods=['GET', 'POST']
)
def login():
    """login page"""
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        user = User.get_by_email(email)
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password_hash, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('signin.html', current_user=current_user)

@app.route(
    '/logout',
    strict_slashes=False
)
def logout():
    """User logout"""
    logout_user()
    return redirect(url_for('home'))


@app.route(
    '/register',
    strict_slashes=False,
    methods=['POST', 'GET']
)
def signup():
    """signup page"""
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        phone_number = data.get('phone')
        print(data)
        if None in [username, email, password, phone_number]:
            return jsonify(message='Missing Field'), 400
        user = User.get_by_username(username)
        if user:
            flash("You've already signed up with that email, log in instead!")
        user = User.get_by_email(email)
        if user:
            return redirect(url_for('login'))
        hash_password = generate_password_hash(
            password,
            method='pbkdf2:sha256',
            salt_length=8
        )
        user_data = {
            'username': username,
            'email': email,
            'password_hash': hash_password,
            'phone_number': phone_number
        }
        whatsapp = data.get('whatsapp')
        if whatsapp:
            user_data['whatsapp'] = whatsapp
        user = User(**user_data)
        user.save()
        login_user(user)
        return redirect(url_for('home'))



    return render_template('register.html', current_user=current_user)

@app.route('/properties/<property_id>', strict_slashes=False)
def get_property(property_id):
    """Property page"""
    current_property = Property.get(property_id)
    return render_template('property.html', property=current_property)

@app.route(
    '/properties/add',
    strict_slashes=False,
    methods=['POST', 'GET']
)
def add_property():
    """Add a property page"""
    if not current_user.is_authenticated:
        flash('Must login to add a property.')
        return redirect(url_for('login'))
    if request.method == 'POST':
        region_id = request.form.get('region')
        return redirect(url_for('add_p_area', region_id=region_id))
    all_regions = Region.get_all()
    return render_template('add_property_rr.html', regions=all_regions)

@app.route(
    '/properties/regions/<region_id>',
    strict_slashes=False,
    methods=['POST', 'GET']
)
@login_required
def add_p_area(region_id):

    if request.method == 'POST':
        area_id = request.form.get('area')
        area = Area.get(area_id)
        if not area:
            return jsonify(message='Area Not Found'), 400
        return redirect(url_for('add_property_c', area_id=area.id))
    region = Region.get(region_id)
    if not region:
        return jsonify(messge='Region Not Found'), 400
    return render_template('add_property_a.html', areas=region.areas)

@app.route(
    '/properties/areas/<area_id>',
    strict_slashes=False,
    methods=['POST', 'GET']
)
@login_required
def add_property_c(area_id):
    if request.method == 'POST':
        city_id = request.form.get('city')
        print(city_id)
        city = City.get(city_id)
        if not city:
            return jsonify(message='City Not Found'), 400
        location = city.return_location()
        title = request.form.get('title')
        description = request.form.get('description')
        price = request.form.get('price')
        property_type = request.form.get('type')
        image_urls = request.form.getlist('image_urls[]')
        amenity_ids = request.form.getlist('amenities[]')
        amenities = [Amenity.get(amenity_id) for amenity_id in amenity_ids]
        if None in [title, description, price, property_type, image_urls]:
            return jsonify(message="Missing Field"), 400
        if len(image_urls) < 5:
            return jsonify(message="Please enter at least 5 images"), 400
        print(image_urls)
        images = [Image(image_url=url) for url in image_urls]

        new_property = Property(
            title=title,
            description=description,
            location=location,
            price=int(price),
            property_type=property_type,
            user_id=current_user.id,
            amenities=amenities,
            city_id=city.id,
            is_active=True
        )
        new_property.images = images
        new_property.save()
        return redirect(url_for('home'))
        
    amenities = Amenity.get_all()
    area = Area.get(area_id)
    if not area:
        return jsonify(messsage='Area Not Found'), 400
    return render_template('add_property.html', cities=area.cities, amenities=amenities)

@app.route(
    '/user/<user_id>',
    strict_slashes=False
)
def user_profile(user_id):
    """user profile page"""
    user = User.get(user_id)
    if not user:
        return jsonify(message="User Not Found")
    return render_template('user.html', user=user)

@app.route(
    '/users/me',
    strict_slashes=False
)
@login_required
def get_current_user():
    
    if not current_user:
        return jsonify(message="User Not Found")
    return render_template('current_user.html', user=current_user)

@app.route(
    '/properties/<property_id>/edit'
)
@login_required
def edit_property(property_id):
    """Edit a property"""
    current_property = Property.get(property_id)
    return render_template('edit_property.html', property=current_property)

@app.route(
    '/users/me/edit'
)
@login_required
def edit_current_user():
    return render_template('edit_me.html', user=current_user)

@app.route('/admin')
def admin_page():
    return render_template('admin.html')

@app.route('/admin/users')
def all_users():
    users = User.get_all()
    return render_template('admin.html', items=users, table_name='users')

@app.route('/admin/properties')
def all_properties():
    properties = Property.get_all()
    return render_template('admin.html', items=properties, table_name='properties')

@app.route('/admin/regions')
def all_regions():
    regions = Region.get_all()
    return render_template('admin.html', items=regions, table_name='regions')


@app.route('/admin/areas')
def all_areas():
    areas = Area.get_all()
    return render_template('admin.html', items=areas, table_name='areas')

@app.route('/admin/cities')
def all_cities():
    cities = City.get_all()
    return render_template('admin.html', items=cities, table_name='cities')

@app.route('/admin/amenities')
def all_amenities():
    amenities = Amenity.get_all()
    return render_template('admin.html', items=amenities, table_name='amenities')


@app.route('/admin/<table_name>/edit/<id>', methods=['GET', 'POST'])
# @login_required
def admin_edit(table_name, id):
    table_mapping = {
        "users": User,
        "properties": Property,
        "regions": Region,
        "areas": Area,
        "cities": City,
        "amenities": Amenity,
        "images": Image
    }

    if table_name not in table_mapping:
        return jsonify({"error": "Invalid table name"}), 400

    table_class = table_mapping[table_name]
    item = table_class.get(id)

    if request.method == 'POST':
        for key in request.form:
            setattr(item, key, request.form[key])
        item.save() 
        return redirect(url_for('admin_page', table_name=table_name))

    relationship_dict = {
        'Region': ['areas'],
        'Area': ['cities'],
        'City': ['properties'],
        'User': ['properties'],
        'Property': ['images', 'amenities'],
        'Amenity': ['properties']
    }
    relationships = relationship_dict[item.__class__.__name__]
    item_dict = item.to_dict()
    for relationship in relationships:
        item_dict[relationship] = item.its(relationship)
    return render_template('edit_item.html', table_name=table_name, item=item_dict)

@app.route('/admin/<table_name>/view/<id>', methods=['GET', 'POST'])
# @login_required
def admin_view(table_name, id):
    table_mapping = {
        "users": User,
        "properties": Property,
        "regions": Region,
        "areas": Area,
        "cities": City,
        "amenities": Amenity,
        "images": Image
    }

    if table_name not in table_mapping:
        return jsonify({"error": "Invalid table name"}), 400

    table_class = table_mapping[table_name]
    item = table_class.get(id)

    relationship_dict = {
        'Region': ['areas'],
        'Area': ['cities'],
        'City': ['properties'],
        'User': ['properties'],
        'Property': ['images', 'amenities'],
        'Amenity': ['properties']
    }
    relationships = relationship_dict[item.__class__.__name__]
    item_dict = item.to_dict()
    for relationship in relationships:
        item_dict[relationship] = item.its(relationship)
    return render_template('view_item.html', table_name=table_name, item=item_dict)


@app.route('/admin/<table_name>/delete/<id>')
def admin_delete(table_name, id):
    pass


@app.route('/admin/users/<user_id>/properties', methods=['GET'])
# @login_required
def admin_view_user_properties(user_id):
    user = User.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    properties = user.properties
    return render_template('user_properties.html', user=user, properties=properties)

@app.route('/admin/properties/<property_id>/images')
def admin_view_property_images(property_id):
    cur_property = Property.get(property_id)
    if not cur_property:
        return jsonify(error="Property not found"), 404
    images = cur_property.images
    return render_template('property_images.html', property=cur_property, images=images)

@app.route('/admin/cities/<city_id>/properties', methods=['GET'])
# @login_required
def admin_view_city_properties(city_id):
    city = City.get(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404
    properties = city.properties
    return render_template('city_properties.html', city=city, properties=properties)

@app.route('/admin/regions/<region_id>/areas', methods=['GET'])
# @login_required
def admin_view_region_areas(region_id):
    region = Region.get(region_id)
    if not region:
        return jsonify({"error": "Region not found"}), 404
    areas = region.areas
    return render_template('region_areas.html', region=region, areas=areas)

@app.route('/admin/areas/<area_id>/cities', methods=['GET'])
# @login_required
def admin_view_area_cities(area_id):
    area = Area.get(area_id)
    if not area:
        return jsonify({"error": "Area not found"}), 404
    cities = area.cities
    return render_template('area_cities.html', area=area, cities=cities)

@app.route('/admin/properties/<property_id>', methods=['GET', 'POST'])
# @login_required
def admin_view_property(property_id):
    property = Property.get(property_id)
    if not property:
        return jsonify({"error": "Property not found"}), 404
    images = property.images
    amenities = Amenity.get_all()
    if request.method == 'POST':
        # Handle adding new images or updating amenities here
        pass
    return render_template('property_details.html', property=property, images=images, amenities=amenities)

@app.route('/admin/properties/<property_id>/amenities')
def admin_view_property_amenities(property_id):
    cur_property = Property.get(property_id)
    if not cur_property:
        return jsonify(error="Property not found"), 404
    images = cur_property.amenities
    return render_template('property_images.html', property=cur_property, amenities=amenities)

@app.route('/admin/amenities/<amenity_id>/properties')
def admin_view_amenity_properties(amenity_id):
    amenity = Amenity.get(amenity_id)
    if not amenity:
        return jsonify(error="Property not found"), 404
    properties = amenity.properties
    return render_template('amenity_properties.html', amenity=amenity, properties=properties)