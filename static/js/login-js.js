function myFunction(idP) {
    var x = document.getElementById(idP);
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }
