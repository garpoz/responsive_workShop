//garpozir@gmail.com

function login() {
    if ($('#typeEmailX').val() === "" || $('#typePasswordX').val() === '') {
        $('#myModal').modal('show');
        return;
    }
    var a=document.getElementById("typePasswordX").value;
    var c="";
    a.split('').forEach(a=>{c=c+'👌'+a.charCodeAt()});
    window.location.replace(`/market?user=${document.getElementById("typeEmailX").value}&&pass=${c}`);

}
