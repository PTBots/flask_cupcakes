const BASE_URL = 'http://localhost:5000/api';

function createCupcakeHTML(cupcake) {
    return `
        <div cupcake-id="${cupcake.id}">
            <li>
                ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating} 
                <button class="delete-button">X</button>
            </li>
            <img class="cupcake-img"
                src="${cupcake.image}"
                alt="(no img)">
        </div>
    `;
}

async function showCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);

    for (let cupcakeData of response.data.cupcakes) {
        let newCupcake = $(createCupcakeHTML(cupcakeData));
        $("#cupcakes-list").append(newCupcake);
    }
}

$("#add-cupcake-form").on("submit", async function(e){
    e.preventDefault();

    let flavor = $("#cupcake-flavor").val();
    let rating = $("#cupcake-rating").val();
    let size = $("#cupcake-size").val();
    let image = $("#cupcake-image").val();

    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        rating,
        size,
        image
    });

    let newCupcake = $(createCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    $("#add-cupcake-form").trigger("reset");
});

$("#cupcakes-list").on("click", ".delete-button", async function (e) {
    e.preventDefault();
    let $cupcake = $(e.target).closest("div");
    let cupcakeId = $cupcake.attr("cupcake-id");

    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
});

$(showCupcakes);