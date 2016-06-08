var czy_zalogowany = false;
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function set_logged_state() {
    $.get("/uname/", function(data){
        if(data["id"] != null){
            czy_zalogowany = true;
            $("#uname").html('Zalogowany jako '+ data["username"] +
                    "    <a href=\"/logout/\">Wyloguj</a>");
        }
    });
}

function load_edit(gid) {
    gm = localStorage.getItem("gminy");
    usr = localStorage.getItem("users");
    if(gm != null && usr != null) {
        gm = JSON.parse(gm);
        usr = JSON.parse(usr);
        ind = 0;
        while(ind < gm.length && gm[ind]["pk"] != gid) ind++;
        if(ind >= gm.length)
            alert("BŁĄD!\nNie znaleziono gminy.");
        else{
            gmina = gm[ind];
            $("#K1input").val(gmina["liczbaGlosowKand1"]);
            $("#K2input").val(gmina["liczbaGlosowKand2"]);
            ind = 0;
            while(ind < usr.length && usr[ind]["id"] != gmina["revuser"]) ind++;
            if(ind >= usr.length)
                uname = "unknown";
            else
                uname = usr[ind]["username"];
            d = new Date(gmina["revtime"]);

            $("#gobutton").off("click");
            $("#gobutton").click(function() {
                $.getJSON("gminy/"+gid+"/", function(data) {
                    if(data["rev"] != gmina["rev"]){
                        alert("Dane zostały zmodyfikowane " +
                                "przez innego usera.\n" +
                                "Przeładuj stronę i spróbuj ponownie");
                    } else if(confirm("Ostatnia modyfikacja przez \"" +
                                uname + "\" o godzinie " +
                                d.toLocaleString() + "\nZapisać?")){
                        dt = {};
                        dt["rev"] = gmina["rev"];
                        dt["liczbaGlosowKand1"] = $("#K1input").val();
                        dt["liczbaGlosowKand2"] = $("#K2input").val();
                        $.ajax({
                            url: "gminy/"+gid+"/",
                            beforeSend: function (request){
                                csrf = getCookie("csrftoken");
                                if(csrf != "") {
                                    request.setRequestHeader(
                                        "X-CSRFToken",
                                        csrf);
                                }
                                        },
                            data: dt,
                            dataType: "json",
                            type: "PATCH",
                            success: function(data){
                                window.location.replace("/");
                            },
                            error:function(jqXHR, textStatus, errorThrown){
                                alert("Nastąpił błąd. Spróbuj ponownie\n" +
                                        JSON.stringify(jqXHR, null, 4));
                            }
                        });
                    }
                }).fail(function() {
                    alert("Could not get data from server. Try again later");    
                    });
            });
        }
    }
}

function load_seemore(type, value) {
    if(type == "w")
        selector = function(gmina) {
            return gmina["wojewodztwo"] == value;
        };
    else if(type == "r")
        selector = function(gmina) {
            return gmina["rodzaj"] == value;
        };
    else if(type == "s"){
        breaks = [5000,10000,20000,50000,100000,200000,500000];
        selector = function(gmina) {
            return (sum(map(breaks, function(x){
                if(x<gm[i]["liczbaMieszkancow"])
                    return 1;
                else
                    return 0;
            })) == value);
        };
    }
    gm = localStorage.getItem("gminy");
    if( gm != null ){
        gm = JSON.parse(gm);
        lg = [];
        for(i =0; i < gm.length; i++){
            if(selector(gm[i]))
                lg.push(gm[i]);
        }
        $("#listbody").html("");
        for(i=0;i<lg.length;i++){
            newrow = "<tr>\n" +
                "<td>"+lg[i]["nazwa"]+"</td>\n" +
                "<td>"+lg[i]["liczbaGlosowKand1"]+"</td>\n" +
                "<td>"+lg[i]["liczbaGlosowKand2"]+"</td>\n" +
                "<td><a onClick=\"showEdit("+lg[i]["pk"]+")\">Zmodyfikuj</a>" +
                "</td>\n" +
                "</tr>";
            $("#listbody").append(newrow);
        }
    }
}

function showDialog(type, value, tt) {
    load_seemore(type, value);
    $('#listdial').dialog({
        width: "50%",
        height: 500,
        modal: true,
        title: 'Gminy w "' + tt + '"',
    });
}

function showEdit(gid) {
    if(!czy_zalogowany)
        window.location.replace("/login/");
    else {
    load_edit(gid);
    $('#eddial').dialog({
        width: "50%",
        height: 500,
        modal: true,
        title: "Edycja"
    });}
}

