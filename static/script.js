function validar() {
    const usuario = document.getElementById("name").value;
    const password = document.getElementById("password").value;
    if (usuario === "" || password === "") {
        alert("Porfavor completa el formulario");
        return false;
    }
    return true;
}
function TooglePassword() {
    const input = document.getElementById("password");
    if (input.type === "password") {
        input.type = "text";
    }else {
        input.type = "password";
    }
}