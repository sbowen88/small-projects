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
  $(document).ready(()=>{
    $('#cart').on('click', ()=>{
      $('#cartMenu').show()
    })
    $('#cart').on('mouseleave', ()=>{
      $('#cartMenu').hide()
    })
    $('#account').on('click', ()=>{
      $('#accountMenu').show()
    })
      $('#account').on('mouseleave', ()=>{
      $('#accountMenu').hide()
    })
    $('#help').on('click', ()=>{
      $('#helpMenu').show()
    })
      $('#help').on('mouseleave', ()=>{
      $('#helpMenu').hide()
    })
  }
  )