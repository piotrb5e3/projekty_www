function showDialog(type, value, tt){
    $.get("seemore",{type: type, v: value}, function( data ) {
        $('#dialog').html(data);
    });
    $('#dialog').dialog({
        width: "50%",
        height: 500,
        modal: true,
        title: 'Gminy w ' + tt,
    });
}
