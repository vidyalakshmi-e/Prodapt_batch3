//Load JSON data
const products= require('./products.json')

//Activity 1
console.log('\nActivitiy1 -Display Product names')

products.forEach(product=>{
    console.log(`${product.name}- ₹${product.price}`)
})

//Activity 2
console.log('\nActivity2 - Calculate Total Price')
const totalPrice = products.map(product=>({ //creates a dict n need a () for evaluation for function no () needed
    name:product.name,
    total:product.price*product.quantity
}))

console.log(totalPrice)

//Activity 3
console.log('\n Activity3 - Find Available products')
const availableProducts=products.filter(product=>product.inStock)
console.log(availableProducts)

//Activity4- Find Expensive product >5000
console.log('\n Activity4- Expensive product >5000')
const expensiveProduct=products.filter(product=>product.filter>5000)
console.log(expensiveProduct)

//Activity5- Search for a product (find)
console.log("\nActivity5- Search for a product")
const SearchProduct=products.find(product=>product.id==103)
console.log(SearchProduct)

//Activity6- Check Product Availability (some)
console.log("\nActivity6- check product Availability")
const checkAvailable=products.some(product=> !product.inStock)
console.log(checkAvailable)

//Actiivity7 verify stock status(Every)
console.log("\nActivity 7 - Verify stock status")
const allavailable=products.every(product=>product.inStock)
console.log(allavailable)

//Activity 8 calculate Grand Total
console.log("\nActivity 8- Calculate Grand Total")
const grandTotal=products.reduce((total,product)=>{
    return total+(product.price*product.qunatity)
},0)
console.log(grandTotal)

//Activity 9 - sort products by price (sort)
console.log("\nActivity9- Sort Products by Price")
const sortProducts =[...products].sort((a,b)=>a.price-b.price)
sortProducts.forEach(product=>{
    console.log(product.name)
})

//Activity10 display only product names(map)
console.log("\n Activity 10 only prodcut names(map)")
const displayProduct=products.map(product=>product.name)
console.log(displayProduct)

//Activity-11 Find Product(Office Chair) Posiiton (findIndex)
console.log("\nActivity 11 Find product position")
const index=products.findIndex(product=>product.name==="office Chair")
console.log(index)

//Activity-12 Remove out-of-stock products(filter)
console.log("\nActivity 12 Remove out of stock product")
const availableProduct=products.filter(product=>product.instock)
console.log(availableProduct)

//Activity 13 add gst(map)- 18%
console.log("Activity 13 add gst(map 18%")
const productwithGST=products.map(product=>({
    ...product,
    gst:product.price*0.18
}))
console.log(productwithGST)

//Activity14 Top 3 cheapest product
console.log("Activity 14 top 3 cheapest product")
const cheapestProduct=[...products]
.sort((a,b)=>a.price-b.price)
.slice(0,3)

cheapestProduct.forEach(product=>{
    console.log(`${product.name} - ₹${product.price}`)
})

//Activity 15- Generate bill summary(Reduce)
console.log("Activity 15 generate bill summary")
const billSummary=products.reduce(
    (summary,product)=>{
        summary.totalProducts++,
        summary.totalPrice += product.price,
        summary.totalAmount += product.price * product.quantity
        return summary
    },{
        totalProducts:0,
        totalPrice:0,
        totalAmount:0
    }
)
console.log(billSummary)