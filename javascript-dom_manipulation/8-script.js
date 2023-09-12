async function showname() {
    let req = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    let salut = await req.json()
    let charelem = document.createElement("p")
    charelem.appendChild(document.createTextNode(salut.hello))
    document.querySelector("#hello").appendChild(charelem)
}

showname()