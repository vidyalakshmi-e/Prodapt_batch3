export async function addBooking(booking){
    const response=await fetch("http://localhost:3000/bookings",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(booking)//convert an object to JSON
    });
    //return await response.json();

    if(!response.ok){
        console.log("Error fetching the API")
    }
    const booking=await response.json()
    console.log("booking added successfully")
    return booking
}