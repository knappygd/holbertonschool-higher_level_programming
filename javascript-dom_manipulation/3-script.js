document.querySelector("#toggle_header").addEventListener("click", function () {
    if (this.className == "red") {
        this.className = "green"
    } else {
        this.className = "red"
    }
})