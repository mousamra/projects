$(document).ready(function()
{
    $(window).scroll(function(){
        var scroll = $(window).scrollTop();
        if(scroll > 100)
        {
            $(".netfix-navbar").css("background", "#0c0c0c");
        }
        else{
            $(".netfix-navbar").css("background", "transparent"); 
        }

    })
}
)