
class Cart():
    def __init__(self, request) -> None:
        self.session = request.session
        
        # Returning user - obtain session key
        cart = self.session.get('session_key')
        
        # New user - generate session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        self.cart = cart
        
        
    def add(self, product, product_qty):
        product_id = str(product.id)
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}
        
        self.session.modified = True
        
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())