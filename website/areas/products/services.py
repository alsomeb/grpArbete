from website.models import Category, Product, db

def getTrendingCategories():
    return Category.query.order_by(Category.CategoryID.desc()).paginate(1,4,False).items

def getCategory(id):
    return Category.query.filter(Category.CategoryID ==id).first()

def getProduct(id):
    return Product.query.filter(Product.ProductID ==id).first()

def getLatestTrendingProducts():
    # query = Product.query.order_by(Product.ProductID.desc()).paginate(1,8,False).items
    query = db.session.query(Product).order_by(Product.ProductID.desc()).limit(10).all()
    return query

def getTrendingProductsByName():
    query = db.session.query(Product).order_by(Product.ProductName.asc()).limit(10).all()
    return query
    
def getTrendingProductsByPriceHigh():
    query = db.session.query(Product).order_by(Product.UnitPrice.desc()).limit(10).all()
    return query
    
def getTrendingProductsByPriceLow():
    query = db.session.query(Product).order_by(Product.UnitPrice.asc()).limit(10).all()
    return query

def getProductByIdStockCount(id):
    count = db.session.query(Product.UnitsInStock).filter(Product.ProductID==id).count()
    return count
