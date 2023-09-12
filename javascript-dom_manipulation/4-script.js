document.querySelector("#add_item").addEventListener("click", function () {
    let li = document.createElement("li")
    li.appendChild(document.createTextNode("Item"))
    document.querySelector(".my_list").appendChild(li)
})