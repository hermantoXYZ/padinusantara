document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0;
    const testimonialsWrapper = document.querySelector('.testimonials-wrapper');
    const testimonials = document.querySelectorAll('.testimonial');
    const totalTestimonials = testimonials.length;
    let isManualScroll = false;
    let scrollTimer;

    function showNextTestimonial() {
        if (!isManualScroll) {
            currentIndex = (currentIndex + 1) % totalTestimonials;
            testimonialsWrapper.scrollTo({
                left: currentIndex * testimonialsWrapper.clientWidth,
                behavior: 'smooth'
            });
        }
    }

    function resetScrollTimer() {
        clearTimeout(scrollTimer);
        isManualScroll = true;
        scrollTimer = setTimeout(() => {
            isManualScroll = false;
        }, 10000);
    }

    testimonialsWrapper.addEventListener('scroll', resetScrollTimer);
    testimonialsWrapper.addEventListener('scroll', function() {
        const scrollLeft = testimonialsWrapper.scrollLeft;
        const width = testimonialsWrapper.clientWidth;
        currentIndex = Math.round(scrollLeft / width);
    });

    setInterval(showNextTestimonial, 10000);
});
