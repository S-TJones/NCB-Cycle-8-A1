from flask import Flask
from flask import render_template

app = Flask(__name__)

# The first route "/" should represent your home page and can simply display your Team name, your name and your photo.
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")


# Products----------------------------------------------
# Current list of products
thumb_drive = {"id": 0, "name": "Thumb/Flash Drives", "price": 23.99, "image": "thumb-drives.jpg", "description": "Description for Product 1."}
water_bottle = {"id": 1, "name": "Water Bottles", "price": 19.89, "image": "water-bottle-mira.jpg", "description": "Description for Product 2."}
pack_pencils = {"id": 2, "name": "Pack of Pencils", "price": 2.99, "image": "pencil-pack.jpg", "description": "Description for Product 3."}
small_speakers = {"id": 3, "name": "Small Speakers", "price": 49.99, "image": "small-speaker.jpg", "description": "Description for Product 4."}
all_products = [thumb_drive, water_bottle, pack_pencils, small_speakers]

@app.route('/product/')
def product():
    return render_template('products.html', products=all_products)

@app.route('/product/<int:product_id>')
def get_product(product_id=None):
    
    # Get number of products
    products_avail = len(all_products)

    # Verify product number received
    if product_id in range(products_avail):
        item = None
        # Find product
        for product in all_products:
            if product["id"] == product_id:
                print("Found")
                item = product
                break
        
        return render_template('products-single.html',  product=item)
    else:
        return render_template('products.html', products=all_products)
