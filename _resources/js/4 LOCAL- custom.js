
// $(document).ready(function(){   
//     setTimeout(function () {
//         $("#cookieConsent").fadeIn(200);
//      }, 4000);
//     $("#closeCookieConsent, .cookieConsentOK").click(function() {
//         $("#cookieConsent").fadeOut(200);
//     }); 
// }); 

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth',
        });        
    });
});


window.onscroll = function() {scrollFunction()};
function scrollFunction() {

    if (document.body.clientWidth > 991) {

        // cr = document.getElementById("myCarousel")
        // var h = cr.clientHeight
        // var limit = h - 70
        var limit = 10

        if (document.body.scrollTop > limit || document.documentElement.scrollTop > limit ) {
            document.getElementById("navbar").classList.add('nav-solid')
            document.getElementById("navbar").classList.remove('transparent')
        } else {
            document.getElementById("navbar").classList.remove('nav-solid');
            document.getElementById("navbar").classList.add('transparent');
        }
    }
}
