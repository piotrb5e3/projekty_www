function drawmap( data ) {
    $(partname).highcharts('Map', {
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
    $.getJSON("stats", function( data ) {
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
    });
}

function refresh_data() {
    //request_drawmap("#mapbox");
    load_panels();
}


