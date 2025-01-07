"""Home route module"""
from web_flask.run import app
from flask import render_template, jsonify
from models.user import User
from models.area import Area
from models.city import City
from models.property import Property
from models.region import Region
from flask import request, url_for, redirect

properties =  [
    {
        "__class__": "Property",
        "amenities": [
            {
                "__class__": "Amenity",
                "amount": 1,
                "created_at": "2025-01-05T19:52:02",
                "id": "6180b61c-c0cd-46db-90db-b341f095d38e",
                "name": "Garden",
                "updated_at": "2025-01-05T19:52:02"
            },
            {
                "__class__": "Amenity",
                "amount": 1,
                "created_at": "2025-01-05T19:49:54",
                "id": "8062f6ae-5608-4f52-a2f6-223be73655ea",
                "name": "Gym",
                "updated_at": "2025-01-05T19:49:54"
            },
            {
                "__class__": "Amenity",
                "amount": 1,
                "created_at": "2025-01-05T19:51:10",
                "id": "9aba2d3f-5927-4967-8f91-579ae391d324",
                "name": "Air Conditioning",
                "updated_at": "2025-01-05T19:51:10"
            }
        ],
        "city_id": "814a0146-d87f-446c-b885-54f87a84e924",
        "created_at": "2025-01-05T22:47:31",
        "description": "Two bedroom apartment with two bathrooms, fully furnished kitchen.",
        "id": "e293d506-d10e-4e2c-beda-12d6560f5497",
        "images": [
            {
                "__class__": "Image",
                "created_at": "2025-01-05T22:47:31",
                "id": "038b8c92-8217-49df-956f-e375a87dffd8",
                "image_url": "https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Prim-Apartments-Sanyang-The-GambiaWhatsApp-Image-2024-07-10-at-16.17.08.jpeg",
                "property_id": "e293d506-d10e-4e2c-beda-12d6560f5497",
                "updated_at": "2025-01-05T22:47:31"
            },
            {
                "__class__": "Image",
                "created_at": "2025-01-05T22:47:31",
                "id": "4fd48bcd-d17f-4c1b-818c-a0180afa26ce",
                "image_url": "https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Prim-Apartments-Sanyang-The-GambiaWhatsApp-Image-2024-07-10-at-16.17.07-1.jpeg",
                "property_id": "e293d506-d10e-4e2c-beda-12d6560f5497",
                "updated_at": "2025-01-05T22:47:31"
            },
            {
                "__class__": "Image",
                "created_at": "2025-01-05T22:47:31",
                "id": "66ba0900-6aa1-439e-b0ae-5d8d52e66cde",
                "image_url": "https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Prim-Apartments-Sanyang-The-GambiaWhatsApp-Image-2024-07-10-at-16.17.09-1.jpeg",
                "property_id": "e293d506-d10e-4e2c-beda-12d6560f5497",
                "updated_at": "2025-01-05T22:47:31"
            },
            {
                "__class__": "Image",
                "created_at": "2025-01-05T22:47:31",
                "id": "6e2de1d8-a6fc-417c-9a2b-2b14e744be69",
                "image_url": "https://gamrealty.com/wp-content/themes/realhomes-child/img/GR-Lets-talk-chat-icon.png",
                "property_id": "e293d506-d10e-4e2c-beda-12d6560f5497",
                "updated_at": "2025-01-05T22:47:31"
            },
            {
                "__class__": "Image",
                "created_at": "2025-01-05T22:47:31",
                "id": "e05451de-d17b-4384-bafe-a76885f898e8",
                "image_url": "https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Prim-Apartments-Sanyang-The-GambiaWhatsApp-Image-2024-07-10-at-16.17.11-2.jpeg",
                "property_id": "e293d506-d10e-4e2c-beda-12d6560f5497",
                "updated_at": "2025-01-05T22:47:31"
            },
            {
                "__class__": "Image",
                "created_at": "2025-01-05T22:47:31",
                "id": "e1c74508-c2f7-42a4-9001-7cb7e298d9f3",
                "image_url": "https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Prim-Apartments-Sanyang-The-GambiaWhatsApp-Image-2024-07-10-at-16.17.06.jpeg",
                "property_id": "e293d506-d10e-4e2c-beda-12d6560f5497",
                "updated_at": "2025-01-05T22:47:31"
            }
        ],
        "is_active": True,
        "location": "Busumbala, Busumbala Area, West Coast Region",
        "price": 6000,
        "property_type": "rent",
        "title": "Two bedroom apartment",
        "updated_at": "2025-01-05T22:58:04",
        "user_id": "bf9dae03-2e21-4336-9c45-d7943255e05b",
        "user": {
            "username": "Omar",
            "phone_number": "3588208",
            "whatsapp": "3588208"
        }
    }
]

regions = [
    {
        "name": "West Coast Region",
        "areas": [
            {
                "name": "Busumbala Area",
                "cities": [
                    "Busumbala",
                    "Yundum",
                    "Yaranbamba"
                ]
            },
            {
                "name": "Brikama",
                "cities": []
            },
            {
                "name": "Old Yundum Area",
                "cities": [
                    "Old Yundum",
                    "Wellingara"
                ]
            },
            {
                "name": "Jamburr Area",
                "cities": [
                    "Jamburr",
                    "Farato"
                ]
            }
        ]
    },
    {
        "name": "Kanifing Municipal Council",
        "areas": [
            {
                "name": "Serrekunda",
                "cities": [
                    "Litrikunda",
                    "Tallinding",
                    "Litrikunda German"
                ]
            },
            {
                "name": "Kanifing Area",
                "cities": [
                    "Kanifing South",
                    "Kanifing Estate",
                    "West Field"
                ]
            },
            {
                "name": "Bakau Area",
                "cities": [
                ]
            },
            {
                "name": "Abuko Area",
                "cities": [
                    "Fagikunda"
                ]
            }
        ]
    }
]


@app.route('/', strict_slashes=False)
def home():
    return render_template('home.html', properties=properties)

@app.route(
    '/login',
    strict_slashes=False,
    methods=['GET', 'POST']
)
def login():
    """login page"""
    return render_template('signin.html')


@app.route(
    '/register',
    strict_slashes=False,
    methods=['POST', 'GET']
)
def signup():
    """signup page"""
    return render_template('register.html')

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
def add_p_area(region_id):

    if request.method == 'POST':
        area_id = request.form.get('area')
        area = Area.get(area_id)
        if not area:
            return jsonify(message='Area Not Found'), 400
        # return redirect(url_for('add_property_c', area_id=area.id))
        return render_template('add_property.html', cities=area.cities)
    region = Region.get(region_id)
    if not region:
        return jsonify(messge='Region Not Found'), 400
    return render_template('add_property_a.html', areas=region.areas)

@app.route(
    '/properties/areas/<area_id>',
    strict_slashes=False,
    methods=['POST', 'GET']
)
def add_property_c(area_id):
    if request.method == 'POST':
        city_id = request.form.get('city')
        city = City.get(city_id)
        if not city:
            return jsonify(message='City Not Found'), 400
    area = Area.get(area_id)
    if not area:
        return jsonify(messsage='Area Not Found'), 400
    return render_template('add_property.html', cities=area.cities)

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
def current_user():
    user = User.get('bf9dae03-2e21-4336-9c45-d7943255e05b')
    if not user:
        return jsonify(message="User Not Found")
    return render_template('current_user.html', user=user)

@app.route(
    '/properties/<property_id>/edit'
)
def edit_property(property_id):
    """Edit a property"""
    current_property = Property.get(property_id)
    return render_template('edit_property.html', property=current_property)

@app.route(
    '/users/me/edit'
)
def edit_current_user():
    current_u = User.get_by_username('admin')
    return render_template('edit_me.html', user=current_u)