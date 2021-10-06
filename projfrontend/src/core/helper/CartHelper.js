

export const addItemToCart = (item, next) => {
    let cart = []

    if(typeof window !== undefined){

        if (localStorage.getItem("cart")) {

            cart =JSON.parse(localStorage.getItem("cart"))
            
        }
        else{

            cart.push({
                ...item
            });
            localStorage.setItem("cart", JSON.stringify(cart));
            next();
        }
    }
}

// to load the cart
export const loadCart = () => {

    if (typeof window !== undefined){

        if(localStorage.getItem("cart")){
            return JSON.parse(localStorage.getItem("cart"))
        }
    }
}

// to remove item from the cart
export const removeItemFromCart = productId => {

    let cart = []

    if (typeof window !== undefined) {

        if(localStorage.getItem("cart")) {
            cart = JSON.parse(localStorage.getItem("cart"))
        }
        cart.map((product, i) => {

            if (product.id=== productId) {
                cart.splice(i, 1)            
            }
        })

        localStorage.setItem("cart", JSON.stringify(cart))
        
    }

    return cart;

};

export const cartEmpty = next => {

    if (typeof window !== undefined){
        localStorage.removeItem("cart")
        let cart = []
        localStorage.setItem("cart", JSON.stringify(cart))
    }
}