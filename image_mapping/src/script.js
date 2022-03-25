$(document).ready(function() {
    $('#floor-selection').on('change',function(){
        var demovalue=$(this).val();
        $("div.myfloor").hide();
        $("#show"+demovalue).show();
    });
});
