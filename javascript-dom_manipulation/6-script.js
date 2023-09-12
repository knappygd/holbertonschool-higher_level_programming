async function showname() {
    let req = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    let char = await req.json()
    let charelem = document.createElement("p")
    charelem.appendChild(document.createTextNode(char.name))
    document.querySelector("#character").appendChild(charelem)
}

showname()