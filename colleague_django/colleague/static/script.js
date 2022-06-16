//garpozir@gmail.com

function login() {
    if ($('#typeEmailX').val() === "" || $('#typePasswordX').val() === '') {
        $('#myModal').modal('show');
        return;
    }
    var xhr = new XMLHttpRequest();
    xhr.open('GET', `/?user=${document.getElementById("typeEmailX").value}&&pass=${document.getElementById("typePasswordX").value}`);
    xhr.setRequestHeader('content-3Type', 'application/json');
    xhr.send();
}