$('.login-button').on('click', () => {
    $('.login-form').toggle();
  });

//Event handlers
$(document).ready(() => {
    const $menuButton = $('.menu-button');
    const $navDropdown = $('#nav-dropdown');
  $menuButton.on('click', ()=>{
    $navDropdown.show()
  })
  
  
  })