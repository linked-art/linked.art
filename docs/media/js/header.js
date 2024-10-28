let lastScrollY = window.scrollY;

window.addEventListener('scroll', function() {

    const header = document.querySelector('nav');

    if (window.scrollY > lastScrollY) {
      // Scrolling down
      header.style.position = 'static';
    } else {
      // Scrolling up
      header.style.position = 'sticky';
    }

    lastScrollY = window.scrollY;
    
  });
