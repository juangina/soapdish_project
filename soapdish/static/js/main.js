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


pageLinks = document.getElementsByClassName('page-link');
searchFlagDiv = document.getElementById('searchFlag');

searchFlag = searchFlagDiv.getAttribute('data-searchFlag');
//console.log('searchFlag: ', searchFlag);
if(searchFlag == '1') {
    for(let i=0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault();
            let page = this.dataset.page
            if(page) {
                //console.log('Button Clicked - Page: ', page);
                searchURL = `${window.location.href}&page=${page}`
                //console.log(searchURL);
                window.location.assign(searchURL)
            }
            else {
                //console.log('Button Clicked - Page not defined.');
            }
            
        })
    }
}
    
//Cookie Functions "Borrowed" from W3Schools Example
/*
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
*/


