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
from flask import request, url_for, redirect, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_login import login_required
from functools import wraps
import os
from config import CURRENT_CONFIG
import datetime


login_manager = LoginManager()
login_manager.init_app(app)



def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.is_anonymous:
            return abort(403)
        if current_user.id != CURRENT_CONFIG.ADMIN_ID:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.template_filter('currency_format')
def currency_format(value):
    """Format a number with commas."""
    if isinstance(value, (int, float)):
        return f"{value:,}"
    return value


def get_file_path(filename):
    """returns path name for a file"""
    now = datetime.datetime.now()
    day = now.strftime('%d')
    month = now.strftime('%b')
    year = now.strftime('%Y')
    time =  now.strftime('%H%M%S%f')
    folder_path = os.path.join('web_flask', 'static', 'images', 'uploads', year, month, day)
    time =  now.strftime('%H%M%S%f')
    file_extension = filename.rsplit('.', 1)[1].lower()
    filename = f'lumo-{time}.{file_extension}'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, filename)
    relative_url = f'/static/images/uploads/{year}/{month}/{day}/{filename}'
    return file_path, relative_url


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
            flash("That email does not exist, sign up instead.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password_hash, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        login_user(user)
        print(current_user.id)
        if current_user.id == 'bf9dae03-2e21-4336-9c45-d7943255e05b':
            return redirect(url_for('admin_page'))
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
        if not region_id:
            flash('Select a region to proceed')
            return redirect(url_for('add_property'))
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
        if not area_id:
            flash('Select an area to proceed')
            return redirect(url_for('add_p_area', region_id=region_id))
        return redirect(url_for('add_property_c', area_id=area_id))
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
        city = City.get(city_id)
        if not city:
            print('Not city provided')
            flash('Select a city')
            return redirect(url_for('add_property_c', area_id=area_id))
        location = city.return_location()
        title = request.form.get('title')
        description = request.form.get('description')
        price = request.form.get('price')
        property_type = request.form.get('type')
        files = request.files.getlist('images[]')
        image_urls = []
        if None in [title, description, price, property_type]:
            flash('Missing field')
            return redirect(url_for('add_property_c', area_id=area_id))

        if property_type not in ['rent', 'sale']:
            flash('Property be must for rent or sale')
            return redirect(url_for('add_property_c', area_id=area_id))

        if files and len(files) < 5:
            flash("Please enter at least 5 images")
            return redirect(url_for('add_property_c', area_id=area_id))
        
        for file in files:
            if file:
                file_path, image_url = get_file_path(file.filename)
                file.save(file_path)
                image_urls.append(image_url)
        amenity_ids = request.form.getlist('amenities[]')
        amenities = [Amenity.get(amenity_id) for amenity_id in amenity_ids]

        if None in [title, description, price, property_type, image_urls]:
            flash('Missing required field')
            return redirect(url_for('add_property_c', area_id=area_id))

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
        flash('Property successfully added')
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
    '/properties/<property_id>/edit',
    methods=['GET', 'POST'],
    strict_slashes=False
)
@login_required
def edit_property(property_id):
    """Edit a property"""
    current_property = Property.get(property_id)
    if not current_property:
        flash('Property not Found')
        return redirect(request.referrer)
    if not current_property.user_id != current_user.id:
        flash('You are not authorized to edit this property')
        return redirect(request.referrer)
    if request.method == 'POST':
        cant_edits = [
            '__class__',
            'created_at',
            'updated_at', 
            'properties',
            '__class__',
            'amenities[]'
        ]

        for key in request.form:
            if key not in cant_edits:
                value = request.form[key]
                if key == 'is_active':
                    value = request.form[key] == 'on'
                setattr(current_property, key, value)
        files = request.files.getlist('images[]')
        amenity_ids = request.form.getlist('amenities[]')
        amenities = [Amenity.get(amenity_id) for amenity_id in amenity_ids]
        current_property.amenities = amenities
        image_urls = []
        if files:
            for file in files:
                if file:
                    file_path, image_url = get_file_path(file.filename)
                    file.save(file_path)
                    image_urls.append(image_url)

        images = [Image(image_url=url, property_id=current_property.id) for url in image_urls]
        [image.save() for image in images]
        current_property.save() 
        return redirect(url_for('get_current_user'))
    amenities = Amenity.get_all()
    amenity_ids = [amenity.id for amenity in current_property.amenities]

    return render_template(
    'edit_property.html',
    property=current_property,
    property_amenities=amenity_ids,
    amenities=amenities
    )

@app.route(
    '/users/me/edit',
    methods=['GET', 'POST']
)
@login_required
def edit_current_user():

    if request.method == 'POST':
        cant_edits = [
                '__class__',
                'created_at',
                'updated_at', 
                'properties',
                '__class__',
                'current-password',
                'new-password'
            ]

        
        for key in request.form:
            if key not in cant_edits:
                value = request.form[key]
                if key == 'phone':
                    key = 'phone_number'
                setattr(current_user, key, value)
                flash(f"{key.capitalize().replace('_', ' ')} successfully changed.")
        current_password = request.form.get('current-password')
        if current_password:
            is_valid = check_password_hash(current_user.password_hash, current_password)
            if not is_valid:
                flash('Incorrect password')
                return redirect(request.referrer)
        new_password = request.form.get('new-password')
        if new_password:
            hash_password = generate_password_hash(
                new_password,
                method='pbkdf2:sha256',
                salt_length=8
            )
            current_user.password_hash = hash_password
            flash('Password successfully changed')
        current_user.save() 
        return redirect(request.referrer)

    # return render_template('edit_me.html', user=current_user)
    return render_template('settings.html', user=current_user)


@app.route('/users/me/delete')
@login_required
def delete_current_user():
    '''Deletes authenticated user'''
    properties = current_user.properties
    [property.delete() for property in properties]
    current_user.delete()
    logout()
    return redirect(url_for('home')) 


@app.route(
    '/images/<image_id>/delete',
    strict_slashes=False
)
@login_required
def delete_property_image(image_id):
    """Delete property image by current user"""
    image = Image.get(image_id)
    if not image:
        flash("Image not found")
        return redirect(request.referrer)
    property = Property.get(image.property_id)
    if not property:
        flash("Property don't exist")
        return redirect(request.referrer)
    if property.user_id != current_user.id:
        flash("Unauthorized action!")
        return redirect(request.referrer)
    
    try:
        os.remove(image.image_url)
    except FileNotFoundError:
        pass
    image.delete()
    flash("Image deleted successfully")
    return redirect(request.referrer)


@app.route(
    '/properties/search',
    strict_slashes=False,
    methods=['GET', 'POST']
)
def search():
    """Search for a property"""
    if request.method == 'POST':
        search_query = request.form.get('search')
        properties = Property.search(search_query)
        return render_template('search.html', properties=properties, search_query=search_query)
    return render_template(url_for('home'))


@app.route('/properties/<property_id>/delete')
@login_required
def delete_user_property(property_id):
    property = Property.get(property_id)
    if property.user_id != current_user.id:
        flash('Not authorised to delete this property')
        return redirect(request.referrer)
    if not property:
        flash('Property not found!', 'error')
        return redirect(request.referrer)
    property_images = property.images
    property.delete()
    for image in property_images:
        if not image:
            flash('Image not found!', 'error')
            return redirect(request.referrer or url_for('get_current_user'))
        image_path = image.image_url

        if os.path.exists(image_path):
            os.remove(image_path)
        image.delete()
    flash('Property deleted successfully!', 'success')
    return redirect(request.referrer)


####################################################################################
####                            Admin Users Routes                              ####
####################################################################################

@app.route('/admin')
@admin_only
def admin_page():
    return render_template('admin.html')

@app.route('/admin/users')
@admin_only
def all_users():
    users = User.get_all()
    return render_template('admin.html', items=users, table_name='users')

@app.route('/admin/properties')
@admin_only
def all_properties():
    properties = Property.get_all()
    return render_template('admin.html', items=properties, table_name='properties')

@app.route('/admin/regions')
@admin_only
def all_regions():
    regions = Region.get_all()
    return render_template('admin.html', items=regions, table_name='regions')


@app.route('/admin/areas')
@admin_only
def all_areas():
    areas = Area.get_all()
    return render_template('admin.html', items=areas, table_name='areas')

@app.route('/admin/cities')
@admin_only
def all_cities():
    cities = City.get_all()
    return render_template('admin.html', items=cities, table_name='cities')

@app.route('/admin/amenities')
@admin_only
def all_amenities():
    amenities = Amenity.get_all()
    return render_template('admin.html', items=amenities, table_name='amenities')

@app.route('/admin/images')
@admin_only
def all_images():
    images = Image.get_all()
    return render_template('admin.html', items=images, table_name='images', count=Image.count())



@app.route('/admin/<table_name>/edit/<id>', methods=['GET', 'POST'])
@admin_only
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
    cant_edits = [
        '__class__',
        'created_at',
        'updated_at', 
        'properties',
        '__class__',
    ]

    if table_name not in table_mapping:
        return jsonify({"error": "Invalid table name"}), 400

    table_class = table_mapping[table_name]
    item = table_class.get(id)

    if request.method == 'POST':
        for key in request.form:
            if key not in cant_edits:
                value = request.form[key]
                if key == 'is_active':
                    value = eval(value)
                setattr(item, key, value)
        item.save() 
        return redirect(url_for('admin_page', table_name=table_name))

    item_dict = item.to_dict()
    for cant_edit in cant_edits:
        if cant_edit in item_dict:
            del item_dict[cant_edit]

    return render_template('edit_item.html', table_name=table_name, item=item_dict)

@app.route('/admin/<table_name>/view/<id>', methods=['GET', 'POST'])
# @login_required
@admin_only
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




@app.route('/admin/users/<user_id>/properties', methods=['GET'])
# @login_required
@admin_only
def admin_view_user_properties(user_id):
    user = User.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    properties = user.properties
    return render_template('user_properties.html', user=user, properties=properties)

@app.route('/admin/properties/<property_id>/images')
@admin_only
def admin_view_property_images(property_id):
    cur_property = Property.get(property_id)
    if not cur_property:
        return jsonify(error="Property not found"), 404
    images = cur_property.images
    return render_template('property_images.html', property=cur_property, images=images)

@app.route('/admin/cities/<city_id>/properties', methods=['GET'])
# @login_required
@admin_only
def admin_view_city_properties(city_id):
    city = City.get(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404
    properties = city.properties
    return render_template('city_properties.html', city=city, properties=properties)

@app.route('/admin/regions/<region_id>/areas', methods=['GET'])
# @login_required
@admin_only
def admin_view_region_areas(region_id):
    region = Region.get(region_id)
    if not region:
        return jsonify({"error": "Region not found"}), 404
    areas = region.areas
    return render_template('region_areas.html', region=region, areas=areas)

@app.route('/admin/areas/<area_id>/cities', methods=['GET'])
# @login_required
@admin_only
def admin_view_area_cities(area_id):
    area = Area.get(area_id)
    if not area:
        return jsonify({"error": "Area not found"}), 404
    cities = area.cities
    return render_template('area_cities.html', area=area, cities=cities)

@app.route('/admin/properties/<property_id>', methods=['GET', 'POST'])
# @login_required
@admin_only
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
@admin_only
def admin_view_property_amenities(property_id):
    cur_property = Property.get(property_id)
    if not cur_property:
        return jsonify(error="Property not found"), 404
    images = cur_property.amenities
    return render_template('property_images.html', property=cur_property, amenities=amenities)

@app.route('/admin/amenities/<amenity_id>/properties')
@admin_only
def admin_view_amenity_properties(amenity_id):
    amenity = Amenity.get(amenity_id)
    if not amenity:
        return jsonify(error="Property not found"), 404
    properties = amenity.properties
    return render_template('amenity_properties.html', amenity=amenity, properties=properties)



@app.route('/admin/add/region', methods=['GET', 'POST'])
@admin_only
def add_region():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            flash('Region name is required!', 'error')
            return redirect(request.url)
        region = Region.get_by_name(name)
        if region:
            flash('Region exist already')
            return redirect(url_for('admin_page', table_name='regions'))
        new_region = Region(name=name)
        new_region.save()
        flash('Region added successfully!', 'success')
        return redirect(url_for('admin_page', table_name='regions'))

    return render_template('add_region.html')


@app.route('/admin/add/area', methods=['GET', 'POST'])
@admin_only
def add_area():
    regions = Region.get_all()  # Fetch all regions to associate with the area
    if request.method == 'POST':
        name = request.form.get('name')
        region_id = request.form.get('region_id')
        
        if not name or not region_id:
            flash('Both area name and region are required!', 'error')
            return redirect(request.url)
        area = Area.get_by_name(name)
        if area:
            flash('Area already exist')
            return redirect(url_for('admin_page')), 400
        
        new_area = Area(name=name, region_id=region_id)
        new_area.save()
        flash('Area added successfully!', 'success')
        return redirect(url_for('admin_page', table_name='areas'))

    return render_template('add_area.html', regions=regions)


@app.route('/admin/add/city', methods=['GET', 'POST'])
@admin_only
def add_city():
    areas = Area.get_all()  # Fetch all areas to associate with the city
    if request.method == 'POST':
        name = request.form.get('name')
        area_id = request.form.get('area_id')
        
        if not name or not area_id:
            flash('Both city name and area are required!', 'error')
            return redirect(request.url)
        
        city = City.get_by_name(name)
        if city:
            flash('City exist already')
            return redirect(url_for('admin_page', table_name='cities')), 400
        
        new_city = City(name=name, area_id=area_id)
        new_city.save()
        flash('City added successfully!', 'success')
        return redirect(url_for('admin_page', table_name='cities'))

    return render_template('add_city.html', areas=areas)


@app.route('/admin/add/amenity', methods=['GET', 'POST'])
@admin_only
def add_amenity():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            flash('Amenity name is required!', 'error')
            return redirect(request.url)
        amenity = Amenity.get_by_name(name)
        if amenity:
            flash('Amenity exist already')
            return redirect(url_for('admin_page', table_name='amenities'))
        new_amenity = Amenity(name=name)
        new_amenity.save()
        flash('Amenity added successfully!', 'success')
        return redirect(url_for('admin_page', table_name='amenities'))

    return render_template('add_amenity.html')

@app.route('/admin/users/delete/<user_id>', methods=['POST'])
@admin_only
def delete_user(user_id):
    # if request.method == 'GET':
        # return redirect(url_for('admin_page', table_name='users'))
    user = User.get(user_id)
    if not user:
        flash('User not found!', 'error')
        return redirect(url_for('admin_page', table_name='users'))
    
    user.delete()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('admin_page', table_name='users'))


@app.route('/admin/properties/delete/<property_id>', methods=['POST'])
@admin_only
def delete_property(property_id):
    property = Property.get(property_id)
    if not property:
        flash('Property not found!', 'error')
        return redirect(url_for('admin_page', table_name='properties'))
    property_images = property.images
    property.delete()
    for image in property_images:
        image.delete()
    flash('Property deleted successfully!', 'success')
    return redirect(url_for('admin_page', table_name='properties'))


@app.route('/admin/regions/delete/<region_id>', methods=['POST'])
@admin_only
def delete_region(region_id):
    region = Region.get(region_id)
    if not region:
        flash('Region not found!', 'error')
        return redirect(url_for('admin_page', table_name='regions'))
    
    region.delete()
    flash('Region deleted successfully!', 'success')
    return redirect(url_for('admin_page', table_name='regions'))


@app.route('/admin/areas/delete/<area_id>', methods=['POST'])
@admin_only
def delete_area(area_id):
    area = Area.get(area_id)
    if not area:
        flash('Area not found!', 'error')
        return redirect(url_for('admin_page', table_name='areas'))
    
    area.delete()
    flash('Area deleted successfully!', 'success')
    return redirect(url_for('admin_page', table_name='areas'))


@app.route('/admin/cities/delete/<city_id>', methods=['POST'])
@admin_only
def delete_city(city_id):
    city = City.get(city_id)
    if not city:
        flash('City not found!', 'error')
        return redirect(url_for('admin_page', table_name='cities'))
    
    city.delete()
    flash('City deleted successfully!', 'success')
    return redirect(url_for('admin_page', table_name='cities'))


@app.route('/admin/images/delete/<image_id>', methods=['POST'])
@admin_only
def delete_image(image_id):
    image = Image.get(image_id)
    if not image:
        flash('Image not found!', 'error')
        return redirect(request.referrer or url_for('admin_page', table_name='images'))
    image_path = image.image_url

    if os.path.exists(image_path):
        os.remove(image_path)
    image.delete()

    flash('Image deleted successfully!', 'success')
    return redirect(request.referrer or url_for('admin_page', table_name='images'))


@app.route('/admin/amenities/delete/<amenity_id>', methods=['POST'])
@admin_only
def delete_amenity(amenity_id):
    amenity = Amenity.get(amenity_id)
    if not amenity:
        flash('Amenity not found!', 'error')
        return redirect(url_for('admin_page', table_name='amenities'))
    
    amenity.delete()
    flash('Amenity deleted successfully!', 'success')
    return redirect(url_for('admin_page', table_name='amenities'))
