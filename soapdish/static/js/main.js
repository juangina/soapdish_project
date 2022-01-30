$(document).ready(function() {

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
  if(searchFlagDiv && pageLinks) {
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
  }
});
