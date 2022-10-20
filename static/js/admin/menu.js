function toggleSidebarView() {

    $('[data-open-sidebar]').click(function() {
        $('.page-overlay').toggle();
        if($('aside.sidebar').hasClass('sidebar-open')){
            $('.page-main').removeClass('col-lg-9 ');
            $('.page-main').removeClass('col-md-9 ');
            $('.page-main').addClass('col-12');
        }else{
            $('.page-main').addClass('col-lg-9 ');
            $('.page-main').addClass('col-md-9 ');
            $('.page-main').removeClass('col-12');

        }
        $('aside.sidebar').toggleClass('sidebar-open');
    });
    $('.page-overlay').click(function() {
        $('aside.sidebar').removeClass('sidebar-open');
        $('.page-overlay').fadeOut();
    });

    $('.sidebar .toggle').click(function() {
        $(this).parent().find('ul').toggle(300);
    });

}

function navegationToggle() {
    $('body').on('click', '#btn-navegation', function() {
        $('.toggle-header').toggle(500);
    })
}

function toggleFullScreen() {
    /*
     * Fullscreen Browsing
     */
    if ($('[data-action="fullscreen"]')[0]) {
        var fs = $("[data-action='fullscreen']");
        fs.on('click', function(e) {
            e.preventDefault();

            //Launch
            function launchIntoFullscreen(element) {

                if (element.requestFullscreen) {
                    element.requestFullscreen();
                } else if (element.mozRequestFullScreen) {
                    element.mozRequestFullScreen();
                } else if (element.webkitRequestFullscreen) {
                    element.webkitRequestFullscreen();
                } else if (element.msRequestFullscreen) {
                    element.msRequestFullscreen();
                }
            }

            //Exit
            function exitFullscreen() {

                if (document.exitFullscreen) {
                    document.exitFullscreen();
                } else if (document.mozCancelFullScreen) {
                    document.mozCancelFullScreen();
                } else if (document.webkitExitFullscreen) {
                    document.webkitExitFullscreen();
                }
            }

            launchIntoFullscreen(document.documentElement);
            fs.closest('.dropdown').removeClass('open');
        });
    }

}

$(document).ready(function() {
    toggleFullScreen();
    toggleSidebarView();
    navegationToggle();

});