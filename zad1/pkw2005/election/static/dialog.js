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

function showEdit(gid) {
    //$.get("gedit", {gid: gid}, function( data ){
    //    $('#dialog').html(data);
    //});
    $('#dialog').load("gedit?gid=" + gid.toString() + " #content");
    $('#dialog').dialog({
        width: "50%",
        height: 500,
        modal: true,
        title: "Edycja"
    });
}

function submitEdit() {
    var fdata = {};
    $.each($('#geditid').serializeArray(), function(_, kv) {
        fdata[kv.name] = kv.value;
    });
    fdata['try'] = 'y';
    //alert(JSON.stringify(paramObj));
    $.post("gverify", fdata,function (data){
        if(data['ok']) {
            if( confirm("Ostatnia modyfikacja przez \"" + data["revuser"] +
                    "\" o godzinie " + data["revtime"] +
                    "\nZapisać?")) {
                fdata['try'] = 'n';
                $.post("gverify", fdata, function( data ) {
                    if(data['ok']) {
                        $('#dialog').dialog("close");
                        refresh_data();
                    } else {
                        alert("Concurrent modification :<");
                    }
                });
            }
        } else {
            $.post("gedit", fdata, function( data ) {
                $('#dialog').html(data);
            });
        }
     });
}

