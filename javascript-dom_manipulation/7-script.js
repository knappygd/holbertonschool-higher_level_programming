async function showtitle() {
    let req = await fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    let res = await req.json()
    let movies = res.results

    movies.forEach(movie => {
        let elem = document.createElement("li")
        elem.appendChild(document.createTextNode(movie.title))
        document.querySelector("#list_movies").appendChild(elem)
    })
}

showtitle()