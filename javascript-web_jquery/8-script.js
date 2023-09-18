$(document).ready(function () {
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function (req) {
        req.results.forEach(movie => {
            $("#list_movies").append("<li>" + movie.title + "</li>")
        });
    });
})
