
Utils = {
    getQueryObj(searchStr){
        var query_obj = {};
        var query_arr = searchStr.split('?');
        if(query_arr.length>1){
            query_arr[1].split('&').forEach((v)=>{
                var field_srt = v.split('=');
                query_obj[field_srt[0]] = field_srt[1];
            })
        }
        return query_obj
    }
}

global.Utils = Utils;