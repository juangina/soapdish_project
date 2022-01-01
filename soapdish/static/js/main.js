//console.log('main.js implemented');
//Learning how to pass view(python) data through the DOM to javascript
//var domObject = document.getElementById('domData');
//var myObject = domObject.dataset.domdata;
//console.log(myObject);

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);


//Cookie Functions "Borrowed" from W3Schools Example
function _setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }
  
function _getCookie(cname) {
  let name = cname + "=";
  let ca = document.cookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
  
function _checkCookie() {
  let user = _getCookie("username");
  if (user != "") {
    alert("Welcome again " + user);
  } else {
    user = prompt("Please enter your name:", "");
    if (user != "" && user != null) {
      _setCookie("username", user, 365);
    }
  }
}



