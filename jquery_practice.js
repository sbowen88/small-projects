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
  $(document).ready(() => {
    $('.hide-button').on('click', () => {
      $('.first-image').hide();
    });
    
    $('.show-button').on('click', () => {
      $('.first-image').show();
    });
    
    $('.toggle-button').on('click', () => {
      $('.first-image').toggle()
    });
    
  });

  //chaining events together
  $(document).ready(() => {
  
    $('.login-button').on('click', () => {
      $('.login-form').show();
    });
    
    $('.menu-button').on('mouseenter', () => {
      $('.nav-menu').show()
    })
    
    $('.nav-menu').on('mouseleave', () => {
      $('.nav-menu').hide();
    })
    
    $('.product-photo').on('mouseenter', ()=>{
      $('.product-photo').addClass('photo-active')
    }).on('mouseleave', ()=>{
      $('.product-photo').removeClass('photo-active')
    })

    //event target
    $('.product-photo').on('mouseenter', (event) => {
        $(event.currentTarget).addClass('photo-active')
      }).on('mouseleave', (event) => {
        $(event.currentTarget).removeClass('photo-active')
      })
      