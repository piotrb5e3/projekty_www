function initialize(){
    load_from_ls();
    $.get("kandydaci", function(data){
        if (data instanceof Array){
            data.forEach(function(kand){
                if(kand["numer"] == 1)
                    localStorage.setItem("kand1", JSON.stringify(kand));
                else
                    localStorage.setItem("kand2", JSON.stringify(kand));
            });
        }
        $.get("gminy", function(data){
            if(data instanceof Array){
                localStorage.setItem("gminy", JSON.stringify(data));
            }
            $.get("users", function(data){
                if(data instanceof Array){
                    localStorage.setItem("users", JSON.stringify(data));
                }
                $.get("wojewodztwa", function(data){
                    if(data instanceof Array){
                        localStorage.setItem("wojewodztwa",
                                JSON.stringify(data));
                    }
                    $.get("rodzaje", function(data){
                        if(data instanceof Array){
                            localStorage.setItem("rodzaje",
                                    JSON.stringify(data));
                        }
                        load_from_ls();
                    });
                });
            });
        });
    });
}
