//console.log('main.js implemented');
//Learning how to pass view(python) data to through the DOM to javascript
//var domObject = document.getElementById('domData');
//var myObject = domObject.dataset.domdata;
//console.log(myObject);

const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);



