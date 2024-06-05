let currentIndex = 0;
const slides = document.querySelectorAll('.carousel-item');
const totalSlides = slides.length;

function updateCarousel() {
  const carouselInner = document.querySelector('.carousel-inner');
  const offset = -currentIndex * 100;
  carouselInner.style.transform = `translateX(${offset}%)`;
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % totalSlides;
  updateCarousel();
}

function prevSlide() {
  currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
  updateCarousel();
}

document.querySelector('.next').addEventListener('click', nextSlide);
document.querySelector('.prev').addEventListener('click', prevSlide);

// Swipe Gesture Handling
let startX = 0;

document.querySelector('.carousel').addEventListener('touchstart', (event) => {
  startX = event.touches[0].clientX;
});

document.querySelector('.carousel').addEventListener('touchmove', (event) => {
  const moveX = event.touches[0].clientX;
  const diffX = startX - moveX;

  if (diffX > 50) {
    nextSlide();
  } else if (diffX < -50) {
    prevSlide();
  }
});

document.querySelector('.carousel').addEventListener('mousedown', (event) => {
  startX = event.clientX;
});

document.querySelector('.carousel').addEventListener('mousemove', (event) => {
  if (startX) {
    const moveX = event.clientX;
    const diffX = startX - moveX;

    if (diffX > 50) {
      nextSlide();
      startX = 0;
    } else if (diffX < -50) {
      prevSlide();
      startX = 0;
    }
  }
});

document.querySelector('.carousel').addEventListener('mouseup', () => {
  startX = 0;
});

document.querySelector('.carousel').addEventListener('mouseleave', () => {
  startX = 0;
});
