async function addCupcake() {
    data = {
        flavor: $('#flavor').val(),
        size: $('#size').val(),
        rating: $('#rating').val(),
        image: $('#image').val()
    }
    $('.list-group').append(`<li>${data.flavor}</li>`)
    await axios.post('/api/cupcakes', data = data)
}

$('#new-cupcake-btn').click(addCupcake)