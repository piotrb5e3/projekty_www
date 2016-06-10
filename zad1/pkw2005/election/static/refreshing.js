function map(array, transform) {
    var mapped = [];
    for (var i = 0; i < array.length; i++)
        mapped.push(transform(array[i]));
    return mapped;
}

function sum(array) {
    var summ = 0;
    for (var i = 0; i < array.length; i++)
        summ += array[i]
    return summ;
}


function drawmap( data ) {
    $("#mapbox").highcharts('Map', {
        title : {
            text : null
        },

        mapNavigation: {
            enabled: false,
        },

        colors: [
            'rgb(206, 104, 0)',
            'rgb(231, 121, 0)',
            'rgb(255, 134, 9)',
            'rgb(254, 144, 32)',
            'rgb(255, 157, 57)',
            'rgb(255, 169, 81)',
            'rgb(255, 181, 84)',
            'rgb(255, 193, 94)',
            'rgb(255, 205, 112)',
            'rgb(255, 219, 112)',
            'rgb(190, 255, 167)',
            'rgb(204, 227, 255)',
            'rgb(180, 213, 253)',
            'rgb(153, 199, 255)',
            'rgb(125, 183, 254)',
            'rgb(90, 164, 254)',
            'rgb(53, 144, 255)',
            'rgb(2, 115, 253)',
            'rgb(2, 96, 212)',
            'rgb(1, 74, 163)',
            'rgb(0, 53, 117)',
            ],


        tooltip: {
            valueSuffix: "%"
        },
        colorAxis: {
            dataClassColor: 'category',
            dataClasses: [{
                to: 29.57
            }, {
                from: 29.57,
                to: 32.84
            }, {
                from: 32.84,
                to: 34.11
            }, {
                from: 34.11,
                to: 36.38
            }, {
                from: 36.38,
                to: 38.65
            }, {
                from: 38.65,
                to: 40.92
            }, {
                from: 40.92,
                to: 43.19
            }, {
                from: 43.19,
                to: 45.46
            }, {
                from: 45.46,
                to: 47.73
            }, {
                from:47.73,
                to: 49.99
            }, {
                from: 49.99,
                to: 50.01
            },  {
                from: 50.01,
                to: 52.27
            },  {
                from: 52.27,
                to: 54.54
            },  {
                from: 54.54,
                to: 56.81
            },  {
                from: 56.81,
                to: 59.08
            },  {
                from: 59.08,
                to: 61.35
            },  {
                from: 61.35,
                to: 63.62
            },  {
                from: 63.62,
                to: 65.89
            },  {
                from: 65.89,
                to: 68.16
            },  {
                from: 68.16,
                to: 70.43
            },  {
                from: 70.43
            }]
        },

        legend: {
            enabled: false
        },

        series : [{
            data : data,
            mapData: Highcharts.maps['countries/pl/pl-all'],
            joinBy: 'hc-key',
            name: 'Wynik kandydata nr 1',
            states: {
                hover: {
                    borderColor: 'rgb(255,255,0)',
                    color: null
                }
            },
        }]
    });
}

function load_panels() {
    k1 = JSON.parse(localStorage.getItem("kand1"));
    k2 = JSON.parse(localStorage.getItem("kand2"));
    data = [];
    listagmin = localStorage.getItem("gminy");
    data["c1p"] = "--.--";
    data["c2p"] = "--.--";
    data["upr"] = 0;
    data["wyd"] = 0;
    data["odd"] = 0;
    data["waz"] = 0;
    data["c1c"] = 0;
    data["c2c"] = 0;
    if(listagmin != null){
        listagmin = JSON.parse(listagmin);
        for(i = 0; i<listagmin.length; i++){
            data["upr"] += listagmin[i]["liczbaUprawnionych"];
            data["wyd"] += listagmin[i]["liczbaWydanychKart"];
            data["odd"] += listagmin[i]["liczbaGlosowOddanych"];
            data["waz"] += listagmin[i]["liczbaGlosowWaznych"];
            data["c1c"] += listagmin[i]["liczbaGlosowKand1"];
            data["c2c"] += listagmin[i]["liczbaGlosowKand2"];
        }
        if(data["waz"] > 0){
            data["c1p"] = (100 * data["c1c"] / data["waz"]).toFixed(2);
            data["c2p"] = (100 * data["c2c"] / data["waz"]).toFixed(2);
        }
    }
    if(k1 != null){
        data["c1n"] = k1["nazwisko"].toUpperCase() + " " + k1["imiona"];
    }else
        data["c1n"] = "Knadydat 1";
    if(k2 != null){
        data["c2n"] = k2["nazwisko"].toUpperCase() + " " + k2["imiona"];
    }else
        data["c2n"] = "Kandydat 2";
    $(".c1b").each(function(index) {
        $(this).css("width", data["c1p"] + "%");
    });
    $(".c2b").each(function(index) {
        $(this).css("width", data["c2p"] + "%");
    });
    $(".upr").each(function(index) {
        $(this).html(data["upr"]);
    });
    $(".wyd").each(function(index) {
        $(this).html(data["wyd"]);
    });
    $(".odd").each(function(index) {
        $(this).html(data["odd"]);
    });
    $(".waz").each(function(index) {
        $(this).html(data["waz"]);
    });
    $(".c1p").each(function(index) {
        $(this).html(data["c1p"]+"%");
    });
    $(".c2p").each(function(index) {
        $(this).html(data["c2p"]+"%");
    });
    $(".c1c").each(function(index) {
        $(this).html(data["c1c"]);
    });
    $(".c2c").each(function(index) {
        $(this).html(data["c2c"]);
    });
    $(".c1n").each(function(index) {
        $(this).html(data["c1n"]);
    });
    $(".c2n").each(function(index) {
        $(this).html(data["c2n"]);
    });

}

function load_wojewodztwa() {
    woj = localStorage.getItem("wojewodztwa");
    gm =  localStorage.getItem("gminy");
    if( gm != null && woj != null){
        woj = JSON.parse(woj);
        gm = JSON.parse(gm);
        data = [];
        map_data = [];
        for(i = 0; i < woj.length; i++){
            pk = woj[i]["pk"];
            dt = {}
            dt["nr"]  = woj[i]["numer"];
            dt["hc-key"] = woj[i]["hckey"];
            dt["nazwa"] = woj[i]["nazwa"];
            dt["waz"] = 0;
            dt["c1c"] = 0;
            dt["c2c"] = 0;
            data[pk] = dt;
        }
        for(i = 0; i < gm.length; i++){
            nr = gm[i]["wojewodztwo"];
            if(nr != null) {
                dt = data[nr];
                dt["waz"] += gm[i]["liczbaGlosowWaznych"];
                dt["c1c"] += gm[i]["liczbaGlosowKand1"];
                dt["c2c"] += gm[i]["liczbaGlosowKand2"];
                data[nr] = dt;
            }
        }
        $("#tabwoj").html("");
        data.forEach(function(elem){
            if(elem["waz"] > 0){
                elem["c1p"] = (100 * elem["c1c"] / elem["waz"]).toFixed(2);
                elem["c2p"] = (100 * elem["c2c"] / elem["waz"]).toFixed(2);
                dt = {};
                dt["hc-key"] = elem["hc-key"];
                dt["value"] = 100 * elem["c1c"] / elem["waz"];
                map_data.push(dt);
            } else {
                elem["c1p"] = "--.--";
                elem["c2p"] = "--.--";
            }
            newrow = "<tr>\n<td>"+elem["nr"]+"</td>\n" +
                "<td>\n<a onClick=\"showDialog('w', '"+elem["nr"]+"', '"+
                elem["nazwa"]+"')\">"+elem["nazwa"]+"</a>\n</td>\n"+
                "<td>"+elem["waz"]+"</td>\n<td>"+elem["c1c"]+"</td>\n"+
                "<td>"+elem["c1p"]+"%</td>\n<td class=\"tableruler\">\n"+
                ((elem["waz"]>0)?"<div><div style=\"width: "+
                 elem["c1p"]+"%;\">\n</div></div>":"")+
                "</td>\n<td>"+elem["c2p"]+"%</td>\n<td>"+elem["c2c"]+"</td>\n"+
                "</tr>";
            $("#tabwoj").append(newrow);
        });
        drawmap(map_data);
    }
}

function load_rodzaje() {
    rd = localStorage.getItem("rodzaje");
    gm =  localStorage.getItem("gminy");
    if( gm != null && rd != null){
        rd = JSON.parse(rd);
        gm = JSON.parse(gm);
        data = [];
        for(i = 0; i < rd.length; i++){
            pk = rd[i]["pk"];
            dt = {}
            dt["pk"] = pk;
            dt["nazwa"] = rd[i]["nazwa"];
            dt["waz"] = 0;
            dt["c1c"] = 0;
            dt["c2c"] = 0;
            data[pk] = dt;
        }
        for(i = 0; i < gm.length; i++){
            nr = gm[i]["rodzaj"];
            if(nr != null) {
                dt = data[nr];
                dt["waz"] += gm[i]["liczbaGlosowWaznych"];
                dt["c1c"] += gm[i]["liczbaGlosowKand1"];
                dt["c2c"] += gm[i]["liczbaGlosowKand2"];
                data[nr] = dt;
            }
        }
        $("#tabrodzaj").html("");
        data.forEach(function(elem){
            if(elem["waz"] > 0){
                elem["c1p"] = (100 * elem["c1c"] / elem["waz"]).toFixed(2);
                elem["c2p"] = (100 * elem["c2c"] / elem["waz"]).toFixed(2);
            } else {
                elem["c1p"] = "--.--";
                elem["c2p"] = "--.--";
            }
            newrow = "<tr>\n" +
                "<td>\n<a onClick=\"showDialog('r', '"+elem["pk"]+"', '"+
                elem["nazwa"]+"')\">"+elem["nazwa"]+"</a>\n</td>\n"+
                "<td>"+elem["waz"]+"</td>\n<td>"+elem["c1c"]+"</td>\n"+
                "<td>"+elem["c1p"]+"%</td>\n<td class=\"tableruler\">\n"+
                ((elem["waz"]>0)?"<div><div style=\"width: "+
                 elem["c1p"]+"%;\">\n</div></div>":"")+
                "</td>\n<td>"+elem["c2p"]+"%</td>\n<td>"+elem["c2c"]+"</td>\n"+
                "</tr>";
            $("#tabrodzaj").append(newrow);
        });
    }
}

function load_rozmiary() {
    gm =  localStorage.getItem("gminy");
    breaks = [5000,10000,20000,50000,100000,200000,500000];
    if( gm != null ){
        gm = JSON.parse(gm);

        data = [];
        dt = {};
        dt["nazwa"] = "do 5000";
        dt["num"] = 0;
        dt["waz"] = 0;
        dt["c1c"] = 0;
        dt["c2c"] = 0;
        data.push(dt);

        for(i = 0; i < breaks.length - 1; i++){
            dt = {};
            dt["nazwa"] = "od " + breaks[i] + " do " + breaks[i + 1];
            dt["num"] = i + 1;
            dt["waz"] = 0;
            dt["c1c"] = 0;
            dt["c2c"] = 0;
            data.push(dt);
        }

        dt = {};
        dt["nazwa"] = "pow 500000";
        dt["num"] = breaks.length;
        dt["waz"] = 0;
        dt["c1c"] = 0;
        dt["c2c"] = 0;
        data.push(dt);

        for(i = 0; i < gm.length; i++){
            nr = sum(map(breaks, function(x){
                if(x<gm[i]["liczbaMieszkancow"])
                    return 1;
                else
                    return 0;
            }));
            if(nr != null) {
                dt = data[nr];
                dt["waz"] += gm[i]["liczbaGlosowWaznych"];
                dt["c1c"] += gm[i]["liczbaGlosowKand1"];
                dt["c2c"] += gm[i]["liczbaGlosowKand2"];
                data[nr] = dt;
            }
        }
        $("#tabrozmiar").html("");
        data.forEach(function(elem){
            if(elem["waz"] > 0){
                elem["c1p"] = (100 * elem["c1c"] / elem["waz"]).toFixed(2);
                elem["c2p"] = (100 * elem["c2c"] / elem["waz"]).toFixed(2);
            } else {
                elem["c1p"] = "--.--";
                elem["c2p"] = "--.--";
            }
            newrow = "<tr>\n" +
                "<td>\n<a onClick=\"showDialog('s', '"+elem["num"]+"', '"+
                elem["nazwa"]+"')\">"+elem["nazwa"]+"</a>\n</td>\n"+
                "<td>"+elem["waz"]+"</td>\n<td>"+elem["c1c"]+"</td>\n"+
                "<td>"+elem["c1p"]+"%</td>\n<td class=\"tableruler\">\n"+
                ((elem["waz"]>0)?"<div><div style=\"width: "+
                 elem["c1p"]+"%;\">\n</div></div>":"")+
                "</td>\n<td>"+elem["c2p"]+"%</td>\n<td>"+elem["c2c"]+"</td>\n"+
                "</tr>";
            $("#tabrozmiar").append(newrow);
        });
    }
}

function load_from_ls() {
    set_logged_state();
    load_panels();
    load_wojewodztwa();
    load_rodzaje();
    load_rozmiary();
}

