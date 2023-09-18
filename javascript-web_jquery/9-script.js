$(document).ready(function () {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (req) {
        $("#hello").append("<p>" + req.hello + "</p>")
    });
})
