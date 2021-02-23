function netPatients(numpatients, duration, monincrease){
    if(duration/30>1){
        final_mth_patients=numpatients+(Math.round(duration/30)-1)*monincrease
        net_patients=((numpatients+final_mth_patients)*Math.round(duration/30))/2
    } else{
        net_patients=numpatients+monincrease 
    }
    return net_patients;
}

function estResults(net_patients, duration, frequency){
    return net_patients * duration * frequency;
}

function getPreview(){
    
    var formInst=$('input[id^=duration_]')
    
    for (var x=1; x<formInst.length+1; x++){
        
        var duration=parseInt($('input#duration_' +x).val()); 
        console.log(duration);
        var monincrease=parseInt($('input#monthly_increase_' +x).val()); 
        console.log(monincrease);
        var results=$('[id^=result_'+ x +']')
        for (var i=1; i<results.length+1; i++){ 
            console.log(i-1, results.eq(i-1))           
            var txt=results.eq(i-1).attr("id")
            var msfcode=txt.split("_")[2]            
            var frequency=parseInt($('select#frequency_'+ x +'_' + msfcode).val()); 
            console.log(frequency);
            var numpatients=parseInt($('input#num_patients_' + x +'_' + msfcode).val()); 
            console.log(numpatients);   

            estimate=estResults(netPatients(numpatients, duration, monincrease),duration, frequency);                 
            console.log(estimate);

            results.eq(i-1).text(estimate);
        }
    }       
}

