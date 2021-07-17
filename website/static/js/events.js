const events = document.querySelectorAll(".event-button")
const body = document.querySelector("#event-body")
const title = document.querySelector("#exampleModalLabel")
const url = document.querySelector(".register-url")

for (const event of events) {
    const pk = event.getAttribute('button-id')
    event.addEventListener("click", (e) => {
        console.log("working bro  " + pk);
        getData(pk, e);
    })
}
const getData = (pk, e) => {
    $.ajax({
        type: "GET",
        url: `/events/${pk}/`,
        data: {
            "pk": pk,
        },
        success: (response) => {
            console.log(response);
            e.preventDefault();
            title.innerHTML = response.data.name;
            body.innerHTML = response.data.description;
            url.href = response.data.link;
        },
        error: (error) => console.log(error),
    })
}