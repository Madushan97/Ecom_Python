

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
