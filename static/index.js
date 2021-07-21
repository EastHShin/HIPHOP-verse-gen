let isRunning = false;
function suggestion() {
    if (isRunning == false) {
        var textarea = document.getElementById("context");
        var context = textarea.value;
        if(context == ""){
            alert("write your context!");
            isRunning = false;
            return;
        }
        isRunning = true;
        var formdata = new FormData();
        formdata.append("context", context);
        fetch(
            "/hiphop",
            {
                method: "POST",
                body: formdata
            }
        )
            .then(response => response.text())
            .then(result => {
                console.log(result)
                concat(result)
            });

    }
}

function concat(newText) {
    var context = document.getElementById("context");
    context.value = newText;
    isRunning = false;
}