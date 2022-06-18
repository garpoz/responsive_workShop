//garpozir@gmail.com

function login() {
    if ($('#typeEmailX').val() === "" || $('#typePasswordX').val() === '') {
        $('#myModal').modal('show');
        return;
    }
    window.location.replace(`/market?user=${document.getElementById("typeEmailX").value}&&pass=${document.getElementById("typePasswordX").value}`);

}
